from utils.parser.rss_parser import rss_parser
from utils.utils import EmptyArticleError

def parse_the_hacker_news(html_content, name, news_type = "sports"):
    articles = rss_parser(html_content, name, news_type)

    if len(articles) == 0:
        raise EmptyArticleError(name)

    return articles