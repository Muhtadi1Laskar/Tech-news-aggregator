def parse_amardesh(json_data, name, news_type = "sports"):
    articles = []
    stories = json_data.get("stories") or []
    baseURL = f"https://www.dailyamardesh.com/{news_type}/"

    for story in stories:
        full_url = baseURL + story["news_slug"]

        articles.append({
            "title": story["title"],
            "link": full_url,
            "publish_date": story["meta"]["first_published_at"],
            "news_type": news_type,
            "source": name
        })
    
    return articles
