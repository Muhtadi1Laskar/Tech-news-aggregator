import requests

def make_requests(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as https_err:
        print(https_err)
    except requests.exceptions.ConnectionError as conn_err:
        print(conn_err)
    except requests.exceptions.Timeout as timeout_err:
        print(timeout_err)
    except requests.exceptions.RequestException as req_err:
        print(req_err)
