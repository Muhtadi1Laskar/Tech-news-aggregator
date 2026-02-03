from utils.parser.rss_parser import rss_parser
from utils.utils import EmptyArticleError

def parse_dhaka_tribune(html_content, name, news_type="sports"):
    articles = rss_parser(html_content, name, news_type)

    if len(articles) == 0:
        raise EmptyArticleError(name)
        
    total_articles_to_save = len(articles) // 2 if len(articles) > 50 else len(articles)

    return articles[:total_articles_to_save]
