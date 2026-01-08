import requests

def fetch_html(url):
    return requests.get(url).content

def fetch_json(url):
    return requests.get(url).json()