from configparser import ParsingError
from bs4 import BeautifulSoup
import lxml

def parse_dhaka_tribune(html_content, name, news_type="sports"):
    soup = BeautifulSoup(html_content, "lxml-xml")
    articles = []

    article_card = soup.find_all("item")

    if not article_card:
        raise ParsingError("Dhaka Tribune layout changed")
    
    if len(article_card) == 0:
        return "No article found"
    
    total_article_cards = len(article_card) // 2

    for index in range(0, total_article_cards+1):
        card = article_card[index]
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
