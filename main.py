import requests
from bs4 import BeautifulSoup

from pipeline.fetch import make_requests
from pipeline.normalize import normalize_data
from adapters import (
    dailystarnews_adapter,
    amardesh
)

from core.utils import save_data

def run_site_pipeline(site_config):
    all_articles = []

    

def get_articles_and_save(url, adapter_class, website_name):
    response = make_requests(url)
    soup = BeautifulSoup(response.content, "html.parser")
    adapter = adapter_class()

    raw_articles = adapter.parse(soup)
    articles = normalize_data(raw_articles)

    if articles:
        save_data(articles, website_name)

    return articles

def scrape_multiple_pages(config):
    for i in range(1, config['total_pages']+1):
        url = config['base_url'].format(i)
        get_articles_and_save(url, config['adapter'], config['website_name'])

site_config = [
    # {
    #     'base_url': 'https://www.thedailystar.net/tech-startup/latest?page={}',
    #     'adapter': dailystarnews_adapter.DailyStarAdapter,
    #     'website_name': 'dailystar',
    #     'total_pages': 1
    # },
    {
        'base_url': 'https://www.dailyamardesh.com/api/stories?page=1&slug=world',
        'adapter': amardesh.AmarDesh,
        'website_name': 'amardesh',
        'total_pages': 1
    }
]

if __name__ == "__main__":
    total_pages = 6

    print("Started Scraping")

    for data in site_config:
        scrape_multiple_pages(data)

    # reddit_url = "https://www.reddit.com/r/technews/"
    # get_articles_and_save(reddit_url, reddit_adapter.RedditNews, "redditnews")
    
    # print("Done Scraping")
    # get_articles_and_save("https://www.prothomalo.com/api/v1/collections/bangladesh-all?item-type=story&offset=15&limit=10", prothomalo_adapter.ProthomAlo, "prothomalo")
    