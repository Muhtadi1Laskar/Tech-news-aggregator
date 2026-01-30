import concurrent.futures
import time
from typing import List, Dict, Any
from collections import defaultdict
from urllib.parse import urlparse
from functools import partial  # ADD THIS IMPORT
from threading import Lock
from config.sites import SITES
from config.worker_config import site_configs
from utils.utils import save_to_json, dedupe, get_last_run_index
from utils.cleaner import clean_and_process_articles
from model.database import save_to_database

def run_site_with_rate_limit(
    site: Dict[str, Any],
    total_pages: int = 1,
    max_workers: int = 10,
    delay: float = 1.0,
) -> List[Dict]:
    """Run site scraping with parallel page fetching AND rate limiting."""
    all_articles = []
    news_types = site["params"]["news_types"]
    language = site["language"]
    source_name = site["name"]

    stats = {
        "site_name": source_name,
        "successful_fetches": 0,
        "failed_fetches": 0
    }

    # Track last request time per domain for rate limiting
    last_request_time = defaultdict(float)
    time_lock = Lock()

    # Create all URLs to fetch
    urls_to_fetch = []
    for key, value in news_types.items():
        for i in range(1, total_pages + 1):
            url = site["build_url"](i, value)
            urls_to_fetch.append((url, key))
    
    stats["total_urls_attempted"] = len(urls_to_fetch)

    def fetch_with_rate_limit(
        site_info: Dict,
        url: str,
        key: str,
        source: str,
        last_times: dict,
        min_delay: float,
    ) -> List[Dict]:
        """Fetch a single URL with rate limiting."""
        # Extract domain for rate limiting
        # domain = urlparse(url).netloc

        # # Calculate time since last request to this domain
        # current_time = time.time()
        # time_since_last = current_time - last_times[domain]

        # # Apply rate limiting
        # if time_since_last < min_delay:
        #     sleep_time = min_delay - time_since_last
        #     time.sleep(sleep_time)

        # # Make the request
        # try:
        #     raw = site_info["fetch"](url) # Scraping function
        #     # Update last request time for this domain
        #     last_times[domain] = time.time()
        #     articles = site_info["parse"](raw, source, key)
        #     return articles
        # except Exception as e:
        #     print(f"[ERROR FETCHING] {url}: {e}")
        #     return []

        domain = urlparse(url).netloc
        with time_lock:  # ← PROTECT ACCESS
            current_time = time.time()
            time_since_last = current_time - last_times[domain]
            if time_since_last < min_delay:
                sleep_time = min_delay - time_since_last
                time.sleep(sleep_time)
            # Update AFTER sleep, still under lock
            last_times[domain] = time.time()

        # Now do the actual request OUTSIDE the lock
        try:
            raw = site_info["fetch"](url)
            articles = site_info["parse"](raw, source, key)
            return articles
        except Exception as e:
            print(f"[ERROR FETCHING] {url}: {e}")
            return []

    # Create a partial function with rate limiting parameters
    fetch_func = partial(
        fetch_with_rate_limit, site, last_times=last_request_time, min_delay=delay
    )

    # Fetch pages in parallel with rate limiting
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Prepare futures
        future_to_url = {}
        for url, key in urls_to_fetch:
            # Pass key and source_name as additional arguments
            future = executor.submit(fetch_func, url=url, key=key, source=source_name)
            future_to_url[future] = url

        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                articles = future.result(timeout=30)
                if articles:
                    all_articles.extend(articles)
                    if len(articles) > 0:
                        stats["successful_fetches"] += 1 # Fix this 
                else:
                    stats["failed_fetches"] += 1

            except concurrent.futures.TimeoutError:
                print(
                    f"[TIMEOUT] {site['name']} {url}: Request timed out after 30 seconds"
                )
                stats["failed_fetches"] += 1
            except Exception as e:
                print(f"[ERROR] {site['name']} {url}: {e}")
                stats["failed_fetches"] += 1

    # Process collected articles
    if all_articles:
        cleaned_articles = clean_and_process_articles(all_articles, language)
        final_articles = dedupe(cleaned_articles)
        run_stats = save_to_database(final_articles)

        stats["new_created_articles"] = run_stats.get("inserted", "")
        stats["updated_existing_articles"] = run_stats.get("updated", "")
        stats["duplicate_articles"] = run_stats.get("matched", "")

    return stats


def main_with_rate_limit():
    """Main function with rate limiting."""
    print("Started Scraping")

    stats_list = []

    run_index = get_last_run_index() + 1 


    for site in SITES:
        site_name = site.get("name", "")
        total_pages = site.get("params", {}).get("total_pages", 0)

        # Get site-specific config or use defaults
        config = site_configs.get(site_name, {})
        max_workers = config.get("max_workers", 3)
        delay = config.get("delay", 1.0)  # 1 second between requests to same domain
        timeout = config.get('timeout', 30)

        print(f"\n📰 Scraping {site_name}")
        print(f"   Config: {max_workers} workers, {delay}s delay, {timeout}s timeout")

        try:
            stats = run_site_with_rate_limit(
                site,
                total_pages=total_pages,
                max_workers=max_workers,
                delay=delay,
            )
            stats["run_index"] = run_index
            stats_list.append(stats)

            
        except Exception as e:
            print(f"[SITE ERROR] {site_name}: {e}")

    print("Finished Scraping")
    save_to_json(stats_list, "runStats")


if __name__ == "__main__":
    main_with_rate_limit()
