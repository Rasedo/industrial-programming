import requests


def fetch_data(url: str) -> dict:
    response = requests.get(url)
    return response.json()
