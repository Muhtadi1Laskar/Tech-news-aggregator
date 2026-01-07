import requests
import json
from adapters.interface import WebsiteInfo


class ProthomAlo(WebsiteInfo):
    def __init__(self, soup):
        self.data = []
        self.url = "https://www.prothomalo.com/api/v1/collections/bangladesh-all?item-type=story&offset=2&limit=15"

    def get_articles(self):
        try:
            response = requests.get(self.url)

            if response.status_code == 200:
                data = response.json()
                news_articles_list = data["items"]

                for article in news_articles_list:
                    print(article["story"]["headline"], article["story"]["slug"])

        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")

    def get_links(self):
        pass

    def get_time(self):
        pass

    def get_description(self):
        pass
