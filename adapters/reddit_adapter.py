from bs4 import BeautifulSoup
import praw
from adapters.interface import WebsiteInfo


class RedditNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.reddit = praw.Reddit(
            client_id="YHc0g9_loGRhyY2YO538Tw",
            client_secret="IwYpWUo3YaLLcMrDdbjHeF2JTGcR7g",
            user_agent="tutorial",
        )
        self.subreddit = self.reddit.subreddit('technews')
        self.top_posts = self.subreddit.top(limit=50)
        self.data = []

    def get_articles(self):
        for post in self.top_posts:
            self.data.append({
                'title': post.title,
                'link': post.url,
                'score': post.score
            })
        return self.data

    def get_links(self):
        pass

    def get_time(self):
        pass

    def get_description(self):
        pass
