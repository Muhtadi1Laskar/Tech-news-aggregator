from configparser import ParsingError
from bs4 import BeautifulSoup

def parse_ars_technica(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")

    articles = []

    article_card = soup.select("article h2")

    if not article_card:
        raise ParsingError("Ars Technica layout changed")
    
    for card in article_card:
        title_tag = card.select_one("div h2 a")

        if not title_tag:
            continue

        title = title_tag.text.strip()
        link = title_tag["href"]
        
        articles.append({
            "title": title,
            "link": link,
            "publish_date": None,
            "news_type": "technology",
            "source": name
        })
    
    return articles
