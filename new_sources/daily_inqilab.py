from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def parse_daily_inqilab(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    
    article_card = soup.select("div.col-md-6 a")

    if not article_card:
        raise ParsingError("Daily Inquilab layout changed")
    
    for card in article_card:
        title_tag = card.select_one("p")
        publish_date_tag = card.select_one("section.news-date-time")

        if not title_tag:
            continue

        link = card["href"]
        
        # try:
        #     text = parse_article(name, link)
        # except Exception as e:
        #     text = ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": link,
            "publish_date": publish_date_tag.get_text(strip=True),
            "news_type": news_type,
            "source": name,
            # "paragraph": text
        })

    return articles
    