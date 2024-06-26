from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo


class HackerNews(WebsiteInfo):
    def __init__(self, soup):
        self.soup = soup
        self.data = []

    def get_articles(self):
        title_tags = self.soup.findAll("span", class_="titleline")

        if title_tags:
            for elem in title_tags:
                title = elem.a.text.strip()
                link = elem.a["href"]

                self.data.append({"title": title, "link": link})

        self.get_time()
        return self.data

    def get_links(self):
        title_element = self.soup.findAll("span", class_="titleline")

        if title_element:
            links = [elem.a["href"] for elem in title_element]
            return links
        return []

    def get_time(self):
        span_tag = self.soup.findAll("span", "age")

        if span_tag:
            time = [elem.a.text for elem in span_tag]

        for index, item in enumerate(self.data):
            if index < len(time):
                self.data[index]["time"] = time[index]

    def get_description(self):
        pass
