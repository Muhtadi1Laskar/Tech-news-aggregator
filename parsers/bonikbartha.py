from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def parse_bonikbartha(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    base_url = "https://bonikbarta.com" if name == "Bonik Bartha (Bangla)" else "https://en.bonikbarta.com"
    
    article_card = soup.select("div[class='@container/card flex']")

    if not article_card:
        raise ParsingError("Bonik Bartha layout changed")
    
    for card in article_card:
        title_tag = card.select_one("div h3 a")
        date_time_tag  = card.select_one("div div p")

        if not title_tag:
            continue

        full_url = base_url + title_tag["href"]

        # try:
        #     text = parse_article(name, full_url) if name == "Bonik Bartha (Bangla)" else ""
        # except Exception as e:
        #     text = ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": full_url,
            "publish_date": date_time_tag.get_text(strip=True),
            "news_type": news_type,
            "source": name,
            # "paragraph": text
        })

    return articles
    