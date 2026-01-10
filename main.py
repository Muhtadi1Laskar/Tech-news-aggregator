# from config.sites import SITES
# from utils.utils import save_to_json, dedupe
# from utils.cleaner import clean_and_process_articles
# from model.database import save_to_database

# def run_site(site, total_pages=1):
#     all_articles = []
#     news_types = site["params"]["news_types"]
#     language = site["language"]
#     source_name = site["name"]

#     for key, value in news_types.items():
#         for i in range(1, total_pages + 1):
#             try:
#                 url = site["build_url"](i, value)
#                 raw = site["fetch"](url)
#                 articles = site["parse"](raw, source_name, key)

#                 all_articles.extend(articles)


#             except Exception as e:
#                 print(f"[ERROR] {site['name']} {url}: {e}")

#     clearned_articles = clean_and_process_articles(all_articles, language)
#     final_articles = dedupe(clearned_articles)

#     save_to_database(final_articles) # Saved the list of scraped data to mongoDB database


# def main():
#     print("Started Scraping")

#     for site in SITES:
#         run_site(site, site["params"]["total_pages"])

#     print("Finished Scraping")


# main()


import concurrent.futures
import time
from typing import List, Dict, Any
from collections import defaultdict
from urllib.parse import urlparse
from functools import partial  # ADD THIS IMPORT
from config.sites import SITES
from utils.utils import save_to_json, dedupe
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

    # Track last request time per domain for rate limiting
    last_request_time = defaultdict(float)

    # Create all URLs to fetch
    urls_to_fetch = []
    for key, value in news_types.items():
        for i in range(1, total_pages + 1):
            url = site["build_url"](i, value)
            urls_to_fetch.append((url, key))

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
        domain = urlparse(url).netloc

        # Calculate time since last request to this domain
        current_time = time.time()
        time_since_last = current_time - last_times[domain]

        # Apply rate limiting
        if time_since_last < min_delay:
            sleep_time = min_delay - time_since_last
            time.sleep(sleep_time)

        # Make the request
        try:
            raw = site_info["fetch"](url)
            # Update last request time for this domain
            last_times[domain] = time.time()
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
            except concurrent.futures.TimeoutError:
                print(
                    f"[TIMEOUT] {site['name']} {url}: Request timed out after 30 seconds"
                )
            except Exception as e:
                print(f"[ERROR] {site['name']} {url}: {e}")

    # Process collected articles
    if all_articles:
        cleaned_articles = clean_and_process_articles(all_articles, language)
        final_articles = dedupe(cleaned_articles)
        save_to_database(final_articles)

    return all_articles


def main_with_rate_limit():
    """Main function with rate limiting."""
    print("Started Scraping")

    # Configure rate limiting per site if needed
    site_configs = {
        "AmarDesh": {
            "max_workers": 5,
            "delay": 1.5,  # API endpoint, can be faster
            "timeout": 15,  # Added timeout parameter
        },
        "ProthomAlo": {
            "max_workers": 3,  # Conservative - major site with protection
            "delay": 2.5,
            "timeout": 20,
            "retries": 2,  # Add retry for robustness
        },
        "KalerKantho": {"max_workers": 4, "delay": 2.0, "timeout": 15},
        "DailyNoyaDiganta": {
            "max_workers": 3,  # HTML parsing might be slower
            "delay": 2.0,
            "timeout": 15,
        },
        "Jugantor": {
            "max_workers": 2,  # Very conservative - AJAX endpoint
            "delay": 3.0,  # Longer delay for safety
            "timeout": 20,
            "retries": 3,
        },
        "DailySangram": {"max_workers": 3, "delay": 2.0, "timeout": 15},
    }

    for site in SITES:
        site_name = site["name"]

        # Get site-specific config or use defaults
        config = site_configs.get(site_name, {})
        max_workers = config.get("max_workers", 3)
        delay = config.get("delay", 1.0)  # 1 second between requests to same domain
        timeout = config.get('timeout', 30)

        print(f"\n📰 Scraping {site_name}")
        print(f"   Config: {max_workers} workers, {delay}s delay, {timeout}s timeout")

        try:
            run_site_with_rate_limit(
                site,
                total_pages=site["params"]["total_pages"],
                max_workers=max_workers,
                delay=delay,
            )
        except Exception as e:
            print(f"[SITE ERROR] {site_name}: {e}")

    print("Finished Scraping")


main_with_rate_limit()
