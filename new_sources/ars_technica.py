from configparser import ParsingError
from bs4 import BeautifulSoup

def parse_ars_technica(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "lxml-xml")

    articles = []

    article_card = soup.select("item")

    if not article_card:
        raise ParsingError("Ars Technica layout changed")
    
    for card in article_card:
        title = card.find("title").get_text(strip=True)
        link = card.find("link").get_text(strip=True)
        publish_date = card.find("pubDate").get_text(strip=True)

        if not title or not link:
            continue

        articles.append(
            {
                "title": title,
                "link": link,
                "publish_date": publish_date,
                "news_type": "technology",
                "source": name,
                "paragraph": None,
            }
        )
    
    return articles
