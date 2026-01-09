from configparser import ParsingError
from bs4 import BeautifulSoup


def parse_jaijaidin(xml_content, url, news_type = "sports"):
    soup = BeautifulSoup(xml_content, "xml")
    articles = []
    base_url = "https://www.jaijaidinbd.com/"

    print(soup)
    
    # article_card = soup.select("article")

    # if not article_card:
    #     raise ParsingError("Daily Sangram layout changed")
    
    # for card in article_card:
    #     title_tag = card.select_one("div.card-content a")
    #     full_url = base_url + title_tag["href"]

    #     if not title_tag:
    #         continue

    #     articles.append({
    #         "title": title_tag.get_text(strip=True),
    #         "link": full_url,
    #         "published_at": "",
    #         "news_type": news_type
    #     })

    return articles
    