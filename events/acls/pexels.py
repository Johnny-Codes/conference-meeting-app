import requests
from ..api_keys import PEXELS_API_KEY


def get_picture_url(city, state):
    url = "https://api.pexels.com/v1/search?query="
    query_set = f"{city} {state}"
    headers = {"Authorization": PEXELS_API_KEY}
    r = requests.get(f"{url}{query_set}", headers=headers)
    picture_url = r.json()["photos"][0]["src"]["original"]
    print("picture", picture_url)
    return {"picture_url": picture_url}
