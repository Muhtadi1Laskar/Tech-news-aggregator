from configparser import ParsingError
from bs4 import BeautifulSoup

from utils.utils import parse_article

def parse_the_daily_sun(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data

    for story in stories:
        full_url = story["url"]

        try:
            text = parse_article(name, full_url)
        except Exception as e:
            text = None

        articles.append({
            "title": story["fullheadline"],
            "link": full_url,
            "publish_date": story["created_at"],
            "news_type": news_type,
            "source": name,
            "paragraph": text
        })
    
    return articles
