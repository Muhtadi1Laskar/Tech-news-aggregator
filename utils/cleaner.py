import hashlib
from urllib.parse import urlparse, urlunparse
from datetime import datetime, timezone
from utils.utils import convert_to_epoch, get_epoch_time


def hash_data(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def generate_id(source, url):
    key = f"{source}:{url}"
    return hash_data(key)


def clean_text(text):
    return " ".join(text.split())


def canonicalize_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))


def clean_and_process_articles(articles, news_language):
    if not articles or len(articles) == 0:
        return []

    clean_articles = []

    for article in articles:
        normalized = normalize_article(article, news_language)

        if normalized:
            clean_articles.append(normalized)

    return clean_articles


def normalize_article(data, news_language="BN"):
    title = clean_text(data.get("title", ""))
    raw_url = data.get("link")
    raw_published_date  = data.get("publish_date", "")
    category = data.get("news_type")
    source = data.get("source", "")

    fetchedDate = get_epoch_time()
    url = canonicalize_url(raw_url)
    contentHashString = f"title:{title}|url:{url}|category:{category}|source:{source}|language:{news_language}"
    
    publishedDate = convert_to_epoch(raw_published_date)
    sortDate = publishedDate if publishedDate else fetchedDate

    article = {
        "id": generate_id(source, url),
        "title": title,
        "url": url,
        "category": category,
        "source": source,
        "language": news_language,
        "contentHash": hash_data(contentHashString),
        "publishedDate": convert_to_epoch(publishedDate),
        "fetchedDate": fetchedDate,
        "sortDate": sortDate
    }

    return article



