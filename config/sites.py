from fetch import fetch_html, fetch_json
from new_sources import (
    amardesh,
    prothomalo,
    kalerkantho,
    noyadigantho,
    jugantor,
    dailysangram,
    bonikbartha,
    the_business_standard,
    the_daily_star,
    the_financial_times,
    the_daily_observer,
    ars_technica,
    bangladesh_protidin,
    investing_live_dotcom,
    daily_ittefaq,
    dhaka_tribune,
    daily_inqilab,
    tech_crunch,
    wired
)

SITES = [
    {
        "name": "Prothom Alo (English)",
        "fetch": fetch_json,
        "parse": prothomalo.parse_prothomalo,
        "build_url": lambda page, t: f"https://en.prothomalo.com/api/v1/collections/{t}?offset={(page*10)}&limit=10",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "EN",
    },
    {
        "name": "Bonik Bartha (English)",
        "fetch": fetch_html,
        "parse": bonikbartha.parse_bonikbartha,
        "build_url": lambda page, t: f"https://en.bonikbarta.com/{t}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 1,
        },
        "language": "EN",
    },
    {
        "name": "Ars Technica",
        "fetch": fetch_html,
        "parse": ars_technica.parse_ars_technica,
        "build_url": lambda page, t: f"https://arstechnica.com/{t}/feed/",
        "params": {
            "news_types": {
                "technology-ai": "ai",
                "technology-gadets": "gadgets",
            },
            "total_pages": 1,
        },
        "language": "EN",
    },
    {
        "name": "The Business Standard (English)",
        "fetch": fetch_html,
        "parse": the_business_standard.parse_the_daily_standared,
        "build_url": lambda page, t: f"https://www.tbsnews.net/{t}?page={page-1}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
                "technology": "tech",
            },
            "total_pages": 3,
        },
        "language": "EN",
    },
    {
        "name": "The Daily Star",
        "fetch": fetch_html,
        "parse": the_daily_star.parse_the_daily_star,
        "build_url": lambda page, t: f"https://www.thedailystar.net/{t}?page={page-1}",
        "params": {
            "news_types": {
                "national": "news/bangladesh/politics",
                "international": "news/world",
                "sports": "sports/cricket",
                "technology": "tech-startup",
            },
            "total_pages": 2,
        },
        "language": "EN",
    },
    {
        "name": "The Financial Times",
        "fetch": fetch_json,
        "parse": the_financial_times.parse_the_financial_times,
        "build_url": lambda page, t: f"https://api.thefinancialexpress.com.bd/api/en/category/{t}/more?page={page}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "world",
                "sports": "sports",
                "technology": "sci-tech",
            },
            "total_pages": 3,
        },
        "language": "EN",
    },
    {
        "name": "The Daily Observer",
        "fetch": fetch_html,
        "parse": the_daily_observer.parse_the_daily_observer,
        "build_url": lambda page, t: f"https://www.observerbd.com/menu/{t}/{page}",
        "params": {
            "news_types": {
                "national": "186",
                "international": "187",
                "sports": "185",
            },
            "total_pages": 3,
        },
        "language": "EN",
    },
    {
        "name": "Amar Desh",
        "fetch": fetch_json,
        "parse": amardesh.parse_amardesh,
        "build_url": lambda page, t: f"https://www.dailyamardesh.com/api/stories?page={page}&slug={t}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "world",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Kaler Kantho",
        "fetch": fetch_json,
        "parse": kalerkantho.parse_kalerkantho,
        "build_url": lambda page, t: f"https://bn.api-kalerkantho.com/api/online/{t}?page={page}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "world",
                "sports": "sport",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Daily Noya Diganta",
        "fetch": fetch_html,
        "parse": noyadigantho.parse_dailynoyadiganta,
        "build_url": lambda page, t: f"https://dailynayadiganta.com/{t}?page={page}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Jugantor",
        "fetch": fetch_json,
        "parse": jugantor.parse_jugantor,
        "build_url": lambda page, t: f"https://www.jugantor.com/ajax/load/categorynews/{t}/20/{page}/10",
        "params": {
            "news_types": {
                "national": "5",
                "international": "6",
                "sports": "8",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Daily Sangram",
        "fetch": fetch_html,
        "parse": dailysangram.parse_dailysangram,
        "build_url": lambda page, t: f"https://dailysangram.com/{t}/?page={page}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Bonik Bartha (Bangla)",
        "fetch": fetch_html,
        "parse": bonikbartha.parse_bonikbartha,
        "build_url": lambda page, t: f"https://bonikbarta.com/{t}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 1,
        },
        "language": "BN",
    },
    {
        "name": "Prothom Alo",
        "fetch": fetch_json,
        "parse": prothomalo.parse_prothomalo,
        "build_url": lambda page, t: f"https://www.prothomalo.com/api/v1/collections/{t}-all?item-type=story&offset={(page*10)-5}&limit=10",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "world",
                "sports": "sports",
                "technology": "technology",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "The Business Standard (Bangla)",
        "fetch": fetch_html,
        "parse": the_business_standard.parse_the_daily_standared,
        "build_url": lambda page, t: f"https://www.tbsnews.net/bangla/{t}?page={page-1}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Bangladesh Pratidin",
        "fetch": fetch_html,
        "parse": bangladesh_protidin.parse_bangladesh_protindin,
        "build_url": lambda page, t: f"https://www.bd-pratidin.com/{t}/page={page}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "international-news",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "investinglive.com",
        "fetch": fetch_html,
        "parse": investing_live_dotcom.parse_investing_livedotcom,
        "build_url": lambda page, t: f"https://investinglive.com/feed/news",
        "params": {
            "news_types": {"international": "international"},
            "total_pages": 1,
        },
        "language": "EN",
    },
    {
        "name": "The Daily Ittefaq",
        "fetch": fetch_html,
        "parse": daily_ittefaq.parse_daily_ittefaq,
        "build_url": lambda page, t: f"https://www.ittefaq.com.bd/feed/{t}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "world-news",
                "sports": "sports",
            },
            "total_pages": 1,
        },
        "language": "BN",
    },
    {
        "name": "Dhaka Tribune",
        "fetch": fetch_html,
        "parse": dhaka_tribune.parse_dhaka_tribune,
        "build_url": lambda page, t: f"https://bangla.dhakatribune.com/feed/{t}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sport",
                "technology": "technology",
            },
            "total_pages": 1,
        },
        "language": "BN",
    },
    {
        "name": "The Daily Inquilab",
        "fetch": fetch_html,
        "parse": daily_inqilab.parse_daily_inqilab,
        "build_url": lambda page, t: f"https://dailyinqilab.com/{t}?page={page}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 3,
        },
        "language": "BN",
    },
    {
        "name": "Tech Crunch",
        "fetch": fetch_html,
        "parse": tech_crunch.parse_tech_crunch,
        "build_url": lambda page, t: f"https://techcrunch.com/feed/",
        "params": {
            "news_types": {"technology": "technology"},
            "total_pages": 1,
        },
        "language": "EN",
    },
    {
        "name": "Wired",
        "fetch": fetch_html,
        "parse": wired.parse_wired,
        "build_url": lambda page, t: f"https://www.wired.com/feed/rss",
        "params": {
            "news_types": {"international": "international"},
            "total_pages": 1,
        },
        "language": "EN",
    },
]
