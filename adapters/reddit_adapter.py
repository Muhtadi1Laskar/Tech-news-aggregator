from bs4 import BeautifulSoup
import praw
import os
from dotenv import load_dotenv, dotenv_values 
from adapters.interface import WebsiteInfo

load_dotenv()

class RedditNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.reddit = praw.Reddit(
            client_id=os.getenv("CLIENTID"),
            client_secret=os.getenv("CLIENTSECRET"),
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
