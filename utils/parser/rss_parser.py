from configparser import ParsingError
from bs4 import BeautifulSoup
import lxml

from utils.utils import EmptyArticleError


def rss_parser(html_content, name, news_type, selector={}):
    item_selector = selector.get("item_selector")
    title_selector = selector.get("title_selector")
    link_selector = selector.get("link_selector")
    publish_date_selector = selector.get("pub_date_selector")
    paragraph_selector = selector.get("paragraph_selector")

    soup = BeautifulSoup(html_content, "lxml-xml")
    articles = []

    article_card = soup.find_all(item_selector)

    if not article_card:
        raise ParsingError(f"{name} layout changed")

    for card in article_card:
        title = card.find(title_selector).get_text(strip=True)
        link = card.find(link_selector).get_text(strip=True)
        publish_date = card.find(publish_date_selector).get_text(strip=True)
        paragraph = card.find(paragraph_selector).get_text(strip=True)

        if not title or not link:
            continue

        articles.append(
            {
                "title": title,
                "link": link,
                "publish_date": publish_date,
                "news_type": news_type,
                "source": name,
                "paragraph": None,
            }
        )

    if len(articles) == 0:
        raise EmptyArticleError(name)

    total_articles_index = len(articles) // 2 if len(articles) > 50 else len(articles)

    return articles[:total_articles_index]
