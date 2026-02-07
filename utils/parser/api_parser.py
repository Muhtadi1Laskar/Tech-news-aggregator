def parse_api(json_data, name, new_type, selectors):
    articles = []
    stories = json_data.get("story") or []
    base_url = selectors.get("base_url") if "base_url" in selectors else ""

    for story in stories:
        articles.append(
            {
                "title": story["title"],
                "link": base_url + story["link"],
                "publish_date": story["publish_date"],
                "news_type": new_type,
                "source": name,
            }
        )

    return articles


def extract_nested_item(key_string, data):
    if not key_string or not isinstance(data, dict):
        return None

    keys = key_string.split(".")
    current = data

    for key in keys:
        if not isinstance(current, dict):
            return None

        if not key in current:
            return None

        current = current[key]

    return current
