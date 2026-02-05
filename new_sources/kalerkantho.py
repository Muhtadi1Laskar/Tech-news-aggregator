def parse_kalerkantho(json_data, name, news_type, selectors = None):
    articles = []
    stories = json_data.get("category") or {}
    baseURL = f"https://www.kalerkantho.com/online/{news_type}/"

    for story in stories["data"] or []:
        full_url = baseURL + f"{story["f_date"]}/{story["n_id"]}"

        articles.append(
            {
                "title": story["n_head"],
                "link": full_url,
                "publish_date": story["created_at"],
                "news_type": news_type,
                "source": name,
                # "paragraph": story.get("n_details", "")
            }
        )

    return articles
