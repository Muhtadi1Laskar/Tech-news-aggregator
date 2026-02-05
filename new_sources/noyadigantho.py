from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def parse_dailynoyadiganta(html_content, name, news_type, selectors = None):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    
    article_card = soup.select("article.p-4")

    if not article_card:
        raise ParsingError("Daily Noya Digantha layout changed")
    
    for card in article_card:
        title_tag = card.select_one("div h3 a")
        

        if not title_tag:
            continue

        link = title_tag["href"]
        
        # try:
        #     text = parse_article(name, link)
        # except Exception as e:
        #     text = ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": link,
            "publish_date": None,
            "news_type": news_type,
            "source": name,
            # "paragraph": text
        })

    return articles
    