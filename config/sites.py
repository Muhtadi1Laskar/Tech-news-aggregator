from fetch import fetch_html, fetch_json
from new_sources import (
    amardesh,
    prothomalo,
    kalerkantho,
    jugantor,
    the_financial_times,
    jagonews24
)

from utils.parser.rss_parser import rss_parser
from utils.parser.html_parser import html_parser

SITES = [
    # {
    #     "name": "Prothom Alo (English)",
    #     "fetch": fetch_json,
    #     "parse": prothomalo.parse_prothomalo,
    #     "build_url": lambda page, t: f"https://en.prothomalo.com/api/v1/collections/{t}?offset={(page*10)}&limit=10",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "EN",
    #     "parseParagraph": False
    # },
    # {
    #     "name": "Bonik Bartha (English)",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://en.bonikbarta.com/{t}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "card_tag": "div[class='@container/card flex']",
    #         "title_tag": "div h3 a",
    #         "link_tag": "div h3 a",
    #         "publish_date_tag": "div div p",
    #         "base_url": "https://en.bonikbarta.com",
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "Ars Technica",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://arstechnica.com/{t}/feed/",
    #     "params": {
    #         "news_types": {
    #             "technology-ai": "ai",
    #             "technology-gadets": "gadgets",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Business Standard (English)",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://www.tbsnews.net/{t}?page={page-1}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #             "technology": "tech",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "card_tag": "h3[class='card-title']",
    #         "title_tag": "a",
    #         "link_tag": "a",
    #         "publish_date_tag": None,
    #         "base_url": "https://www.tbsnews.net"
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Daily Star",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://www.thedailystar.net/{t}?page={page-1}",
    #     "params": {
    #         "news_types": {
    #             "national": "news/bangladesh/politics",
    #             "international": "news/world",
    #             "sports": "sports/cricket",
    #             "technology": "tech-startup",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "card_tag": "h3[class='card-title']",
    #         "title_tag": "a",
    #         "link_tag": "a",
    #         "publish_date_tag": None,
    #         "base_url": "https://www.thedailystar.net"
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Financial Times",
    #     "fetch": fetch_json,
    #     "parse": the_financial_times.parse_the_financial_times,
    #     "build_url": lambda page, t: f"https://api.thefinancialexpress.com.bd/api/en/category/{t}/more?page={page}",
    #     "params": {
    #         "news_types": {
    #             "national": "national",
    #             "international": "world",
    #             "sports": "sports",
    #             "technology": "sci-tech",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "EN",
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Daily Observer",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://www.observerbd.com/menu/{t}/{page}",
    #     "params": {
    #         "news_types": {
    #             "national": "186",
    #             "international": "187",
    #             "sports": "185",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "card_tag": "div.title_inner",
    #         "title_tag": "a",
    #         "link_tag": "a",
    #         "publish_date_tag": None,
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "Amar Desh",
    #     "fetch": fetch_json,
    #     "parse": amardesh.parse_amardesh,
    #     "build_url": lambda page, t: f"https://www.dailyamardesh.com/api/stories?page={page}&slug={t}",
    #     "params": {
    #         "news_types": {
    #             "national": "national",
    #             "international": "world",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Kaler Kantho",
    #     "fetch": fetch_json,
    #     "parse": kalerkantho.parse_kalerkantho,
    #     "build_url": lambda page, t: f"https://bn.api-kalerkantho.com/api/online/{t}?page={page}",
    #     "params": {
    #         "news_types": {
    #             "national": "national",
    #             "international": "world",
    #             "sports": "sport",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Daily Noya Diganta",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://dailynayadiganta.com/{t}?page={page}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "card_tag": "article.p-4",
    #         "title_tag": "div h3 a",
    #         "link_tag": "div h3 a",
    #         "publish_date_tag": None,
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Jugantor",
    #     "fetch": fetch_json,
    #     "parse": jugantor.parse_jugantor,
    #     "build_url": lambda page, t: f"https://www.jugantor.com/ajax/load/categorynews/{t}/20/{page}/10",
    #     "params": {
    #         "news_types": {
    #             "national": "5",
    #             "international": "6",
    #             "sports": "8",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Daily Sangram",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://dailysangram.com/{t}/?page={page}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "card_tag": "article",
    #         "title_tag": "div.card-content a",
    #         "link_tag": "div.card-content a",
    #         "publish_date_tag": None,
    #         "base_url": "https://dailysangram.com"
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Bonik Bartha (Bangla)",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://bonikbarta.com/{t}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "card_tag": "div[class='@container/card flex']",
    #         "title_tag": "div h3 a",
    #         "link_tag": "div h3 a",
    #         "publish_date_tag": "div div p",
    #         "base_url": "https://bonikbarta.com",
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Prothom Alo",
    #     "fetch": fetch_json,
    #     "parse": prothomalo.parse_prothomalo,
    #     "build_url": lambda page, t: f"https://www.prothomalo.com/api/v1/collections/{t}-all?item-type=story&offset={(page*10)-5}&limit=10",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "world",
    #             "sports": "sports",
    #             "technology": "technology",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "parseParagraph": True
    # },
    # {
    #     "name": "The Business Standard (Bangla)",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://www.tbsnews.net/bangla/{t}?page={page-1}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "card_tag": "h3[class='card-title']",
    #         "title_tag": "a",
    #         "link_tag": "a",
    #         "publish_date_tag": None,
    #         "base_url": "https://www.tbsnews.net"
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Bangladesh Pratidin",
    #     "fetch": fetch_html,
    #     "parse": html_parser,
    #     "build_url": lambda page, t: f"https://www.bd-pratidin.com/{t}/page={page}",
    #     "params": {
    #         "news_types": {
    #             "national": "national",
    #             "international": "international-news",
    #             "sports": "sports",
    #         },
    #         "total_pages": 3,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "card_tag": "div.col-6",
    #         "title_tag": "h5",
    #         "link_tag": "div a.stretched-link",
    #         "publish_date_tag": None,
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "investinglive.com",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://investinglive.com/feed/news",
    #     "params": {
    #         "news_types": {"international": "international"},
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Daily Ittefaq",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://www.ittefaq.com.bd/feed/{t}",
    #     "params": {
    #         "news_types": {
    #             "national": "national",
    #             "international": "world-news",
    #             "sports": "sports",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Dhaka Tribune",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://bangla.dhakatribune.com/feed/{t}",
    #     "params": {
    #         "news_types": {
    #             "national": "bangladesh",
    #             "international": "international",
    #             "sports": "sport",
    #             "technology": "technology",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "BN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "Tech Crunch",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://techcrunch.com/feed/",
    #     "params": {
    #         "news_types": {"technology": "technology"},
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "Wired",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://www.wired.com/feed/rss",
    #     "params": {
    #         "news_types": {"international": "international"},
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": True
    # },
    # {
    #     "name": "The Hacker News",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://feeds.feedburner.com/TheHackersNews",
    #     "params": {
    #         "news_types": {"technology": "technology"},
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "item",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "pubDate",
    #         "paragraph_selector": "description",
    #     },
    #     "parseParagraph": False
    # },
    # {
    #     "name": "The Verge",
    #     "fetch": fetch_html,
    #     "parse": rss_parser,
    #     "build_url": lambda page, t: f"https://www.theverge.com/rss/{t}/index.xml",
    #     "params": {
    #         "news_types": {
    #             "technology": "tech",
    #         },
    #         "total_pages": 1,
    #     },
    #     "language": "EN",
    #     "selector": {
    #         "item_selector": "entry",
    #         "title_selector": "title",
    #         "link_selector": "link",
    #         "pub_date_selector": "published",
    #         "paragraph_selector": "summary",
    #     },
    #     "parseParagraph": False
    # },
    {
        "name": "Jagonews24",
        "fetch": fetch_html,
        "parse": jagonews24.jagonew24_parser,
        "build_url": lambda page, t: f"https://www.jagonews24.com/rss/rss.xml",
        "params": {
            "news_types": {
                "national": "national",
            },
            "total_pages": 1,
        },
        "language": "EN",
        "selector": {
            "item_selector": "item",
            "title_selector": "title",
            "link_selector": "link",
            "pub_date_selector": "pubDate",
            "paragraph_selector": "description",
        },
        "parseParagraph": True
    },
]
