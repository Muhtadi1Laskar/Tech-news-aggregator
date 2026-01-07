from dataclasses import dataclass
from datetime import date

@dataclass
class Article:
    title: str
    url: str
    published_at: date | None
    description: str | None
    source: str
