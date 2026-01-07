from abc import ABC, abstractmethod

class FetchStrategy(ABC):
    @abstractmethod
    def fetch(self):
        yield payload