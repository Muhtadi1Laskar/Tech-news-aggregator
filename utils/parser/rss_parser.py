from configparser import ParsingError
from bs4 import BeautifulSoup
import lxml


def rss_parser(html_content, name, news_type="sports"):
    soup = BeautifulSoup(html_content, "lxml-xml")
    articles = []

    article_card = soup.find_all("item")

    if not article_card:
        raise ParsingError(f"{name} layout changed")

    for card in article_card:
        title = card.find("title").get_text(strip=True)
        link = card.find("link").get_text(strip=True)
        publish_date = card.find("pubDate").get_text(strip=True)
        paragraph = card.find("description").get_text(strip=True)

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

    return articles
