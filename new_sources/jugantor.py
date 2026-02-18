def parse_jugantor(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data or []

    
    for story in stories:
        text = story.get("description", "") if parseParagraph else ""
            
        articles.append({
            "title": story["headline"],
            "link": story["url"],
            "publish_date": story["created_at"],
            "news_type": news_type,
            "source": name,
            "paragraph": text
        })
    
    return articles