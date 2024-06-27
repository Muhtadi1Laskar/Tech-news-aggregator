import requests
from bs4 import BeautifulSoup

from adapters import (
    hackernews_adapter,
    techcrunch_adapter,
    reddit_adapter,
    dailystarnews_adapter,
    vergenews_adapter,
    techradarnews_adapter
)
from core.utils import save_data


def get_articles_and_save(url, adapter_class, website_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    adapter = adapter_class(soup)

    articles = adapter.get_articles()

    if articles:
        save_data(articles, website_name)

    return articles

def scrape_multiple_pages(config):
    for i in range(1, config['total_pages']+1):
        url = config['base_url'].format(i)
        get_articles_and_save(url, config['adapter'], config['website_name'])

site_config = [
    {
        'base_url': 'https://news.ycombinator.com/?p={}',
        'adapter': hackernews_adapter.HackerNews,
        'website_name': 'hackernews',
        'total_pages': 5
    },
    {
        'base_url': 'https://techcrunch.com/category/startups/page/{}',
        'adapter': techcrunch_adapter.TechCrunch,
        'website_name': 'techcrunch',
        'total_pages': 5
    },
    {
        'base_url': 'https://www.thedailystar.net/tech-startup/latest?page={}',
        'adapter': dailystarnews_adapter.DailyStarNews,
        'website_name': 'dailystar',
        'total_pages': 5
    },
    {
        'base_url': 'https://www.theverge.com/tech/archives/{}',
        'adapter': vergenews_adapter.VergeNews,
        'website_name': 'vergenews',
        'total_pages': 5
    },
    {
        'base_url': 'https://www.techradar.com/computing/software/artificial-intelligence/{}',
        'adapter': techradarnews_adapter.RadarNews,
        'website_name': 'techradar',
        'total_pages': 5
    }
]

if __name__ == "__main__":
    total_pages = 6

    print("Started Scraping")

    for data in site_config:
        scrape_multiple_pages(data)

    reddit_url = "https://www.reddit.com/r/technews/"
    get_articles_and_save(reddit_url, reddit_adapter.RedditNews, "redditnews")
    
    print("Done Scraping")
    
