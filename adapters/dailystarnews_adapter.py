from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo


class DailyStarNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.data = []

    def get_articles(self):
        parent_tag = self.soup.findAll("div", class_="card-content card-content columns")

        if parent_tag:
            for tag in parent_tag:
                heading_tag = tag.find("h3", class_="title")
                paragraph_tag = tag.find("p", class_="intro")
                time_tag = tag.find("span", class_="interval")

                heading = heading_tag.a.text.strip() if heading_tag else None
                link = heading_tag.a["href"] if heading_tag else None
                paragraph = paragraph_tag.text.strip() if heading_tag else None
                time = time_tag.text.strip() if time_tag else None

                self.data.append(
                    {
                        "heading": heading,
                        "link": link,
                        "description": paragraph,
                        "time": time,
                    }
                )

        return self.data

    def get_links(self):
        pass

    def get_time(self):
        pass

    def get_description(self):
        pass
