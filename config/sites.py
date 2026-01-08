from fetch import fetch_html, fetch_json
from parsers import (
    amardesh,
    prothomalo,
    kalerkantho
)

SITES = [
    # {
    #     "name": "AmarDesh",
    #     "fetch": fetch_json,
    #     "parse": amardesh.parse_amardesh,
    #     "new_types": ["national", "world", "sports"],
    #     "total_pages": 2,
    #     "build_url": lambda page, t: f"https://www.dailyamardesh.com/api/stories?page={page}&slug={t}"
    # },
    # {
    #     "name": "ProthomAlo",
    #     "fetch": fetch_json,
    #     "parse": prothomalo.parse_prothomalo,
    #     "new_types": ["bangladesh", "world", "sports"],
    #     "total_pages": 2,
    #     "build_url": lambda page, t: f"https://www.prothomalo.com/api/v1/collections/{t}-all?item-type=story&offset={page}&limit=10"
    # },
    {
        "name": "KalerKantho",
        "fetch": fetch_json,
        "parse": kalerkantho.parse_kalerkantho,
        "new_types": ["national", "world", "sport"],
        "total_pages": 2,
        "build_url": lambda page, t: f"https://bn.api-kalerkantho.com/api/online/{t}?page={page}"
    }
]