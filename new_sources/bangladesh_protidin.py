from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def parse_bangladesh_protindin(html_content, name, news_type, selectors = None):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []

    article_card = soup.select("div.col-6")

    if not article_card:
        raise ParsingError("Bangladesh Protiin layout changed")

    first_title_tag = soup.select_one("div.col-12 div.card h1")
    first_link = soup.select_one("div.col-12 div.card a.stretched-link")

    if first_title_tag and first_link:
        articles.append(
            {
                "title": first_title_tag.get_text(strip=True),
                "link": first_link["href"],
                "publish_date": None,
                "news_type": news_type,
                "source": name,
                "paragraph": None,
            }
        )

    for index, card in enumerate(article_card):
        title_selector = "h5"
        title_tag = card.select_one(title_selector)
        link_tag = card.select_one("div a.stretched-link")

        if not title_tag or not link_tag:
            continue

        articles.append(
            {
                "title": title_tag.get_text(strip=True),
                "link": link_tag["href"],
                "publish_date": None,
                "news_type": news_type,
                "source": name,
                "paragraph": None,
            }
        )

    return articles
