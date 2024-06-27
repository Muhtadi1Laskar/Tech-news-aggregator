from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo


class RadarNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.data = []

    def get_articles(self):
        parent_div_selector = "div[class*='listingResult small']"
        parent_div = self.soup.select(parent_div_selector)

        if parent_div:
            for tags in parent_div:
                header_tag = tags.find("h3", "article-name")
                time_tag = tags.find("time")
                paragraph_tag = tags.find("p", "synopsis")
                link_tag = tags.find("a", class_="article-link")

                if header_tag:
                    title = header_tag.text.strip() if header_tag else None
                    time = time_tag.text.strip() if time_tag else None
                    description = paragraph_tag.text.strip() if paragraph_tag else None
                    link = link_tag["href"] if link_tag else None

                    self.data.append(
                        {
                            "title": title,
                            "description": description,
                            "link": link,
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
