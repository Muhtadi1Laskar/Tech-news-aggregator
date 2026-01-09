from config.sites import SITES
from utils.utils import save_to_json, dedupe
from utils.cleaner import clean_and_process_articles


def run_site(site, total_pages=1):
    all_articles = []
    news_types = site["params"]["news_types"]
    language = site["language"]
    source_name = site["name"]

    for key, value in news_types.items():
        for i in range(1, total_pages + 1):
            try:
                url = site["build_url"](i, value)
                raw = site["fetch"](url)
                articles = site["parse"](raw, source_name, key)

                all_articles.extend(articles)


            except Exception as e:
                print(f"[ERROR] {site['name']} {url}: {e}")

    clearned_articles = clean_and_process_articles(all_articles, language)
    final_articles = dedupe(clearned_articles)

    save_to_json(final_articles, site["name"])


def main():
    print("Started Scraping")

    for site in SITES:
        run_site(site, site["params"]["total_pages"])

    print("Finished Scraping")


main()
