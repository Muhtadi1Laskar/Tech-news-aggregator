import requests
import time
import random


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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }

    # time.sleep(random.uniform(1, 3))

    try:
        response = requests.get(
            url,
            headers=header
        )
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


def debug_403(url):
    # Try with session
    session = requests.Session()

    # Try different approaches
    approaches = [
        ("Default", lambda: requests.get(url)),
        (
            "With Browser Headers",
            lambda: requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                },
            ),
        ),
        ("With Session", lambda: session.get(url)),
        (
            "With Session + Headers",
            lambda: session.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Accept": "application/json, text/plain, */*",
                },
            ),
        ),
    ]

    for name, request_func in approaches:
        try:
            response = request_func()
            print(f"\n{name}: Status {response.status_code}")
            if response.status_code == 200:
                print("SUCCESS!", name)
                return response
        except Exception as e:
            print(f"{name}: Error - {e}")

    return None


# Call this with your URL
# debug_request("your_url_here")

# print(debug_403("https://www.jugantor.com/ajax/load/categorynews/5/20/1/20"))


# print(fetch_json("https://www.jugantor.com/ajax/load/categorynews/5/20/1/20", True))
