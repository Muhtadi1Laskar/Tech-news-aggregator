from fetch import fetch_html, fetch_json
from parsers import (
    amardesh, 
    prothomalo, 
    kalerkantho, 
    noyadigantho, 
    jugantor, 
    dailysangram
)

SITES = [
    {
        "name": "AmarDesh",
        "fetch": fetch_json,
        "parse": amardesh.parse_amardesh,
        "build_url": lambda page, t: f"https://www.dailyamardesh.com/api/stories?page={page}&slug={t}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "world",
                "sports": "sports",
            },
            "total_pages": 5,
        },
        "language": "BN"
    },
    {
        "name": "ProthomAlo",
        "fetch": fetch_json,
        "parse": prothomalo.parse_prothomalo,
        "build_url": lambda page, t: f"https://www.prothomalo.com/api/v1/collections/{t}-all?item-type=story&offset={page}&limit=10",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "world",
                "sports": "sports",
            },
            "total_pages": 5,
        },
        "language": "BN"
    },
    {
        "name": "KalerKantho",
        "fetch": fetch_json,
        "parse": kalerkantho.parse_kalerkantho,
        "build_url": lambda page, t: f"https://bn.api-kalerkantho.com/api/online/{t}?page={page}",
        "params": {
            "news_types": {
                "national": "national",
                "international": "world",
                "sports": "sport",
            },
            "total_pages": 5,
        },
        "language": "BN"
    },
    {
        "name": "DailyNoyaDiganta",
        "fetch": fetch_html,
        "parse": noyadigantho.parse_dailynoyadiganta,
        "build_url": lambda page, t: f"https://dailynayadiganta.com/{t}?page={page}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 5,
        },
        "language": "BN"
    },
    {
        "name": "Jugantor",
        "fetch": fetch_json,
        "parse": jugantor.parse_jugantor,
        "build_url": lambda page, t: f"https://www.jugantor.com/ajax/load/categorynews/{t}/20/{page}/10",
        "params": {
            "news_types": {
                "national": '5',
                "international": '6',
                "sports": '8',
            },
            "total_pages": 5,
        },
        "language": "BN"
    },
    {
        "name": "DailySangram",
        "fetch": fetch_html,
        "parse": dailysangram.parse_dailysangram,
        "build_url": lambda page, t: f"https://dailysangram.com/{t}/?page={page}",
        "params": {
            "news_types": {
                "national": "bangladesh",
                "international": "international",
                "sports": "sports",
            },
            "total_pages": 5,
        },
        "language": "BN"
    }
]
