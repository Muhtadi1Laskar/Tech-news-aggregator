from configparser import ParsingError
from bs4 import BeautifulSoup


def parse_dailynoyadiganta(html_content, url, news_type = "sports"):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []

    # print(html_content)

    article_card = soup.select("article.p-4")

    print("Article Card: ", len(article_card))

    if not article_card:
        raise ParsingError("Daily Noya Digana layout changed")
    
    for card in article_card:
        title_tag = card.select_one("div h3 a")

        if not title_tag:
            continue

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": title_tag["href"],
            "published_at": "",
            "news_type": news_type
        })

    return articles
    