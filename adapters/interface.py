from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class WebsiteInfo(ABC):
    @abstractmethod
    def get_articles(self):
        pass

    @abstractmethod
    def get_links(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class BaseAdapted(ABC):
    @abstractmethod
    def parse(self, soup: BeautifulSoup):
        pass