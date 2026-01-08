from config.sites import SITES
from utils.utils import save_to_json, dedupe


def run_site(site, total_pages=1):
    all_articles = []
    news_types = site["params"]["news_types"]

    for key, value in news_types.items():
        for i in range(1, total_pages + 1):
            try:
                url = site["build_url"](i, value)
                raw = site["fetch"](url)
                articles = site["parse"](raw, url, key)

                all_articles.extend(articles)

            except Exception as e:
                print(f"[ERROR] {site['name']} {url}: {e}")

    all_articles = dedupe(all_articles)

    save_to_json(all_articles, site["name"])


def main():
    print("Started Scraping")

    for site in SITES:
        run_site(site, site["params"]["total_pages"])

    print("Finished Scraping")


main()
