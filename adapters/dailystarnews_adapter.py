from configparser import ParsingError
from bs4 import BeautifulSoup
from adapters.interface import WebsiteInfo
from adapters.interface import BaseAdapted
from core.article import Article


class DailyStarAdapter(BaseAdapted):
    SOURCE = "The Daily STAR"
    BASE_URL = "https://www.thedailystar.net"

    def parse(self, soup: BeautifulSoup):
        articles = []

        print(soup)

        cards = soup.findAll("div", class_="card-content card-content columns")

        if not cards:
            raise ParsingError("Daily Star layout changed")
        
        
        for card in cards:
            title_tag = card.select_one("h3.title a")
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            url = self.BASE_URL + title_tag["href"]

            description_tag = card.select_one("p.intro")
            description = description_tag.get_text(strip=True) if description_tag else None

            time_tag = card.select_one("span.interval")
            published_at = time_tag.get_text(strip=True)

            articles.append(
                Article(
                    title=title,
                    url=url,
                    description=description,
                    published_at=published_at,
                    source=self.SOURCE
                )
            )

        return articles
