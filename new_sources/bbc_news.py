from configparser import ParsingError
from bs4 import BeautifulSoup


def parse_bbc_news(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data.get("data", [])
    base_url = "https://www.bbc.com"

    for story in stories:
        url_path = story.get("path", None)

        if not url_path:
            continue

        full_url = base_url + url_path

        articles.append({
            "title": story.get("title"),
            "link": full_url,
            "publish_date": story["firstPublishedAt"],
            "news_type": news_type,
            "source": name,
            "paragraph": story.get("summary", "")
        })
    
    return articles
