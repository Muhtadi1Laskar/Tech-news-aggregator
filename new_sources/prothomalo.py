from utils.utils import remove_tag_from_text

def parse_prothomalo(json_data, name, news_type, selectors = None, parseParagraph = False):
    articles = []
    stories = json_data.get("items") or []

    for story in stories:
        single_story = story["story"]
        text = single_story.get("cards", "")[0].get("story-elements", "")[0].get("text", "") if parseParagraph else None
        cleaned_text = remove_tag_from_text(text) if text else None
            

        articles.append({
            "title": single_story["headline"],
            "link": single_story["url"],
            "publish_date": f"{single_story["content-created-at"]}",
            "news_type": news_type,
            "source": name,
            "paragraph": cleaned_text
        })
    
    return articles
