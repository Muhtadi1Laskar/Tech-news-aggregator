def parse_prothomalo(json_data, name, news_type = "sports"):
    articles = []
    stories = json_data.get("items") or []

    for story in stories:
        single_story = story["story"]
        articles.append({
            "title": single_story["headline"],
            "link": single_story["url"],
            "publish_date": f"{single_story["content-created-at"]}",
            "news_type": news_type,
            "source": name
        })
    
    return articles
