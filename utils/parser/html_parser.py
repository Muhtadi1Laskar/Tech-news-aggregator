from configparser import ParsingError
from bs4 import BeautifulSoup
from utils.utils import parse_article


def html_parser(html_content, name, news_type, selectors = None, parseParagraph = False):
    main_card_selector = selectors.get("card_tag")
    title_tag_selector = selectors.get("title_tag")
    link_tag_selector = selectors.get("link_tag")
    publish_date_selector = selectors.get("publish_date_tag")
    base_url = selectors.get("base_url") if "base_url" in selectors else ""

    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    text = ''
    
    article_card = soup.select(main_card_selector)

    if not article_card:
        raise ParsingError(f"{name} layout changed")
    
    for card in article_card:
        title_tag = card.select_one(title_tag_selector)
        link_tag = card.select_one(link_tag_selector)
        date_time_tag  = card.select_one(publish_date_selector) if publish_date_selector else None

        if not title_tag:
            continue

        full_url = base_url + link_tag["href"]
        publish_date = date_time_tag.get_text(strip=True) if date_time_tag else None

        if parseParagraph:
            try:
                text = parse_article(name, full_url)
            except Exception as e:
                text = ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "link": full_url,
            "publish_date": publish_date,
            "news_type": news_type,
            "source": name,
            "paragraph": text
        })

    return articles
    