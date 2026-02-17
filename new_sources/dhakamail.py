from configparser import ParsingError
from bs4 import BeautifulSoup

from utils.utils import parse_article

def parse_dhaka_mail(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data.get("model", []);
    base_url = f"https://www.banglanews24.com/{news_type}/news/bd/"

    for story in stories:
        full_url = story["canonicalUrl"]

        articles.append({
            "title": story["mainTitle"],
            "link": full_url,
            "publish_date": story["datePublished"],
            "news_type": news_type,
            "source": name,
            "paragraph": story["subtitle"]
        })
    
    return articles
