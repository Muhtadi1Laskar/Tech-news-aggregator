from configparser import ParsingError
from bs4 import BeautifulSoup
import json
from adapters.interface import BaseAdapted
from core.article import Article

class AmarDesh(BaseAdapted):
    SOURCE = "Amar Desh"
    BASE_URL = "https://www.dailyamardesh.com/sports"

    def _parse_json(self, payload):
        pass

    def parse(self, payload): 
        articles = []

        data = payload.get("stories", [])
        print(json.dumps(payload))

        for item in payload.get("stories", []):
            slug_link_code = item["news_slug"] 
            full_url = self.BASE_URL + slug_link_code
            articles.append(
                Article(
                    title=item["title"],
                    url=full_url,
                    published_at=item["meta"]["first_published_at"],
                    source=self.SOURCE
                )
            )

        return articles
    
    
