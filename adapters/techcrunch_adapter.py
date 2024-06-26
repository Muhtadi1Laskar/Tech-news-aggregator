from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo

class TechCrunch(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.data = []
    
    def get_articles(self):
        parent_div = self.soup.findAll('div', class_='wp-block-tc23-post-picker')

        if parent_div:
            for tags in parent_div:
                heading_tag = tags.find('h2')
                paragraph_tag = tags.find('p', class_='wp-block-post-excerpt__excerpt')
                time_tag = tags.find('div', class_='has-text-color has-grey-500-color wp-block-tc23-post-time-ago has-small-font-size')

                title = heading_tag.a.text if heading_tag and heading_tag.a else None
                link = heading_tag.a['href'] if heading_tag and heading_tag.a else None
                description = paragraph_tag.text if paragraph_tag else None
                time = time_tag.text.strip() if time_tag else None

                if title and link:
                    self.data.append({
                    'title': title,
                    'link': link,
                    'description': description,
                    'time': time
                })
                    
        return self.data

    def get_links(self):
        pass

    def get_time(self):
        pass

    def get_description(self):
        pass