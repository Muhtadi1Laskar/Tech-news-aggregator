from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo

class VergeNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.data = []
    
    def get_articles(self):
        parent_div_selector = "div[class*='max-w-content-block-mobile']"
        parent_div = self.soup.select(parent_div_selector)

        if parent_div:
            for tags in parent_div:
                heading_tag = tags.find('h2')
                time_tag = tags.find('time')

                title = heading_tag.a.text.strip() if heading_tag else None
                partial_links = heading_tag.a['href'] if heading_tag else None
                time = time_tag.text.strip() if time_tag else None

                links = f"https://www.theverge.com/{partial_links}"

                self.data.append({
                    'title': title,
                    'links': links,
                    'time': time
                })

            return self.data
        return []

    def get_links(self):
        pass

    def get_time(self):
        pass

    def get_description(self):
        pass
