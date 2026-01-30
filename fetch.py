import requests
import time


def fetch_html(url):
    response = fetch_function(url)

    if response is None:
        return None
    elif response.status_code == 200:
        return response.content
    else:
        print(f"Got status: {response.status_code} for {url}")
        return None


def fetch_json(url):
    response = fetch_function(url)

    if response is not None:
        try:
            return response.json()
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")
    return None


def fetch_function(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "bn-BD,bn;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
    }

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occured: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occured: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Requests error occured: {req_err}")
    return None

