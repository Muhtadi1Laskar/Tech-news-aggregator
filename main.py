from config.sites import SITES
from utils.utils import save_to_json, dedupe

def run_site(site, total_pages = 1):
    all_articles = []
    new_types = site["new_types"]

    for type in new_types:
        for i in range(1, total_pages + 1):
            try:
                url = site["build_url"](i, type)
                raw = site["fetch"](url)
                articles = site["parse"](raw, url, type)

                all_articles.extend(articles)

            except Exception as e:
                print(f"[ERROR] {site['name']} {url}: {e}")
    
    all_articles = dedupe(all_articles)

    save_to_json(all_articles, site["name"])

def main():
    print("Started Scraping")

    for site in SITES:
        run_site(site, site["total_pages"])
    
    print("Finished Scraping")

main()