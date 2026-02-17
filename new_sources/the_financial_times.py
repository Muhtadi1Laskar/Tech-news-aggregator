from utils.utils import parse_article

def parse_the_financial_times(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data.get("items") or json_data.get("posts")
    baseURL = f"https://thefinancialexpress.com.bd"

    for story in stories:
        full_url = baseURL + story["slug"]


        try:
            text = parse_article(name, full_url)
        except Exception as e:
            text = None

        articles.append({
            "title": story["title"],
            "link": full_url,
            "publish_date": story["datetime"],
            "news_type": news_type,
            "source": name,
            "paragraph": text
        })
    
    return articles
