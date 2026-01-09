import hashlib
from urllib.parse import urlparse, urlunparse
from datetime import datetime, timezone

def hash_data(source, url):
    key = f"{source}:{url}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()

def clean_text(text):
    return " ".join(text.split())

def cannonicalize_url(url):
    parsed = urlparse(url)
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, "", "", "")
    )

def clean_and_process_articles(articles, news_language):
    if not articles or len(articles) == 0:
        return []
    
    clean_articles = []
    
    for article in articles:
        normalized = normalize_article(article, news_language)

        if normalized:
            clean_articles.append(normalized)
    
    return clean_articles

def normalize_article(data_collection, news_language = "BN"):
    title = clean_text(data_collection.get("title", ""))
    url = cannonicalize_url(data_collection.get("link"))
    published_date = data_collection.get("publish_date", "")
    category = data_collection.get("news_type")
    source = data_collection.get("source", "")
    
    article = {
        "id": hash_data(source, url),
        "title": title,
        "url": url,
        "publishedData": published_date,
        "category": category,
        "source": source,
        "fetchedDate": datetime.now(timezone.utc).isoformat(),
        "language": news_language
    }

    return article
        