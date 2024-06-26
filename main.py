import requests
from bs4 import BeautifulSoup

from adapters import (
    hackernews_adapter,
    techcrunch_adapter,
    reddit_adapter,
    dailystarnews_adapter,
    vergenews_adapter
)
from core.utils import save_data, print_message


def get_articles_and_save(url, adapter_class, website_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    adapter = adapter_class(soup)

    articles = adapter.get_articles()

    if articles:
        save_data(articles, website_name)

    return articles


if __name__ == "__main__":
    print_message("hackernews", "start")
    for i in range(1, 50):

        hackernews_url = f"https://news.ycombinator.com/?p={i}"
        get_articles_and_save(
            hackernews_url, hackernews_adapter.HackerNews, "hackernews"
        )
    print_message("hackernews", "end")
        
    print_message("techcrunch", "start")
    for i in range(1, 50):
        tech_crunch_url = f"https://techcrunch.com/category/startups/page/{i}"
        get_articles_and_save(
            tech_crunch_url, techcrunch_adapter.TechCrunch, "techcrunch"
        )
    print_message("techcrunch", "end")

    print_message("dailystar", "start")
    for i in range(1, 50):
        daily_star_url = f"https://www.thedailystar.net/tech-startup/latest?page={i}"
        get_articles_and_save(
            daily_star_url, dailystarnews_adapter.DailyStarNews, "dailystar"
        )
    print_message("dailystar", "end")

    print_message("vergenews", "start")
    for i in range(1, 15):
        verge_news_url = f"https://www.theverge.com/tech/archives/{i}"
        get_articles_and_save(verge_news_url, vergenews_adapter.VergeNews, "vergenews")
    print_message("vergenews", "end")

    print_message("hackernews", "start")
    reddit_url = "https://www.reddit.com/r/technews/"
    get_articles_and_save(reddit_url, reddit_adapter.RedditNews, "redditnews")
    print_message("hackernews", "end")
    
