def parse_jugantor(json_data, url, news_type = "sports"):
    articles = []
    stories = json_data or []

    for story in stories:
        articles.append({
            "title": story["fullheadline"],
            "link": story["url"],
            "publish_date": story["created_at"],
            "news_type": news_type
        })
    
    return articles