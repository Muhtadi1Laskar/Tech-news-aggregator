from configparser import ParsingError
from bs4 import BeautifulSoup


def parse_the_daily_observer(html_content, name, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []

    print(soup)
    
    article_card = soup.select("div.title_inner")

    if not article_card:
        raise ParsingError("The Daily Observer layout changed")
    
    for card in article_card:
        title_tag = card.select_one("a")

        if not title_tag:
            continue

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": title_tag["href"],
            "publish_date": None,
            "news_type": news_type,
            "source": name
        })

    return articles