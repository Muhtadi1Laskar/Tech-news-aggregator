from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def parse_the_daily_standared(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    base_url = f"https://www.tbsnews.net"
    
    article_card = soup.select("h3[class='card-title']")

    if not article_card:
        raise ParsingError("The Business Standard layout changed")
    
    for card in article_card:
        title_tag = card.select_one("a")

        if not title_tag:
            continue

        full_url = base_url + title_tag["href"]

        # try:
        #     text = parse_article(name, full_url) if name == "The Business Standard (Bangla)" else ""
        # except Exception as e:
        #     text = ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": full_url,
            "publish_date": None,
            "news_type": news_type,
            "source": name,
            # "paragraph": text
        })

    return articles