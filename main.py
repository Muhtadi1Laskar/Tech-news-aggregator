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


if __name__ == "__main__":
    total_pages = 6

    print("Started Scraping")

    for i in range(1, total_pages):
        hackernews_url = f"https://news.ycombinator.com/?p={i}"
        get_articles_and_save(
            hackernews_url, hackernews_adapter.HackerNews, "hackernews"
        )


    for i in range(1, total_pages):
        tech_crunch_url = f"https://techcrunch.com/category/startups/page/{i}"
        get_articles_and_save(
            tech_crunch_url, techcrunch_adapter.TechCrunch, "techcrunch"
        )

    for i in range(1, 50):
        daily_star_url = f"https://www.thedailystar.net/tech-startup/latest?page={i}"
        get_articles_and_save(
            daily_star_url, dailystarnews_adapter.DailyStarNews, "dailystar"
        )

    for i in range(1, 15):
        verge_news_url = f"https://www.theverge.com/tech/archives/{i}"
        get_articles_and_save(verge_news_url, vergenews_adapter.VergeNews, "vergenews")
    
    for i in range(1, 6):
        tech_radar_url = f"https://www.techradar.com/computing/software/artificial-intelligence/{i}"
        get_articles_and_save(tech_radar_url, techradarnews_adapter.RadarNews, "techradar")

    reddit_url = "https://www.reddit.com/r/technews/"
    get_articles_and_save(reddit_url, reddit_adapter.RedditNews, "redditnews")
    
    print("Done Scraping")
    
