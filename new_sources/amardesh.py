from configparser import ParsingError
from bs4 import BeautifulSoup

from utils.utils import parse_article

def parse_amardesh(json_data, name, news_type, selectors = None):
    articles = []
    stories = json_data.get("stories") or []
    baseURL = f"https://www.dailyamardesh.com/{news_type}/"

    for story in stories:
        full_url = baseURL + story["news_slug"]

        # try:
        #     text = parse_article(name, full_url)
        # except Exception as e:
        #     text = None

        articles.append({
            "title": story["title"],
            "link": full_url,
            "publish_date": story["meta"]["first_published_at"],
            "news_type": news_type,
            "source": name,
            # "paragraph": text
        })
    
    return articles
