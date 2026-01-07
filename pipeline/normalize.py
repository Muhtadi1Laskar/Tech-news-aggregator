import re
from core.utils import hash_data

def normalize_data(article_list):
    if not article_list or len(article_list) == 0:
        return {}
    
    result = []

    for article in article_list:
        title = article.title.strip()
        url = article.url
        published_at = article.published_at.strip()
        source = article.source.strip()

        article_id = hash_data(title + url  + published_at)

        result.append({
            "article_id": article_id,
            "title": title,
            "url": url,
            "published_at": published_at,
            "source": source
        })

    return result

def is_valid_url(url_string):
    regex_pattern = re.compile(
        r"^(https?://)?" # Optional http or https scheme
        r"(([-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6})|" # Domain name validation
        r"([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}))" # Optional IPv4 support
        r"([-a-zA-Z0-9@:%._\\+~#?&//=]*)$", re.IGNORECASE
    )

    if re.fullmatch(regex_pattern, url_string):
        return True
    return False