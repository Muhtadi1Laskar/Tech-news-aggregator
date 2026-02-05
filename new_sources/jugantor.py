def parse_jugantor(json_data, name, news_type, selectors = None):
    articles = []
    stories = json_data or []

    for story in stories:
        articles.append({
            "title": story["headline"],
            "link": story["url"],
            "publish_date": story["created_at"],
            "news_type": news_type,
            "source": name,
            # "paragraph": story.get("description", "")
        })
    
    return articles