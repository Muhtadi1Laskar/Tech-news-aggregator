from fetch import fetch_html, fetch_json
from parsers import (
    amardesh,
    prothomalo
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
    {
        "name": "ProthomAlo",
        "fetch": fetch_json,
        "parse": prothomalo.parse_prothomalo,
        "new_types": ["bangladesh", "world", "sports"],
        "total_pages": 2,
        "build_url": lambda page, t: f"https://www.prothomalo.com/api/v1/collections/{t}-all?item-type=story&offset={page}&limit=10"
    }
]