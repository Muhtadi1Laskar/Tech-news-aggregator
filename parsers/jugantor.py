def parse_jugantor(json_data, name, news_type = "sports"):
    articles = []
    stories = json_data or []

    for story in stories:
        articles.append({
            "title": story["fullheadline"],
            "link": story["url"],
            "published_at": story["created_at"],
            "news_type": news_type,
            "source": name
        })
    
    return articles