from configparser import ParsingError
from bs4 import BeautifulSoup
import lxml

from utils.utils import EmptyArticleError, clean_rss_paragraph_text

def check_news_category(url):
    category_mapping = {
        'national': 'national',
        'country': 'national',
        'politics': 'national',
        'bangladesh': 'national',
        'sodesh': 'national',
        'international': 'international',
        'sports': 'sports'
    }
    
    for part in url.split('/'):
        part_lower = part.lower()
        if part_lower in category_mapping:
            return category_mapping[part_lower]

def rss_parser(html_content, name, news_type, selector={}, parseParagraph = True):
    item_selector = selector.get("item_selector")
    title_selector = selector.get("title_selector")
    link_selector = selector.get("link_selector")
    publish_date_selector = selector.get("pub_date_selector")
    paragraph_selector = selector.get("paragraph_selector")

    soup = BeautifulSoup(html_content, "lxml-xml")
    articles = []

    article_card = soup.find_all(item_selector)

    if not article_card:
        raise ParsingError(f"{name} layout changed")

    for card in article_card:
        title = card.find(title_selector).get_text(strip=True)
        link = (
            card.find(link_selector).get_text(strip=True)
            or card.find(link_selector)["href"]
        )
        publish_date = card.find(publish_date_selector).get_text(strip=True)
        paragraph = card.find(paragraph_selector).get_text(strip=True) if parseParagraph else None
        cleaned_paragraph = clean_rss_paragraph_text(paragraph) if paragraph else None


        if not title or not link:
            continue

        extracted_news_type = check_news_category(link) if news_type == "extract_from_url" else news_type

        if extracted_news_type == None:
            continue


        articles.append(
            {
                "title": title,
                "link": link,
                "publish_date": publish_date,
                "news_type": extracted_news_type,
                "source": name,
                "paragraph": cleaned_paragraph,
            }
        )

    if len(articles) == 0:
        raise EmptyArticleError(name)

    return articles
