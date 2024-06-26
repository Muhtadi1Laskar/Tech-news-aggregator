from abc import ABC, abstractmethod

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

