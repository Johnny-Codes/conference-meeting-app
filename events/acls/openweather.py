import requests
from common.api_keys import OPENWEATHER_API_KEY


def get_lat_lon(city, state):
    limit = 1
    params = {
        "q": f"{city}, {state}, USA",
        "appid": OPENWEATHER_API_KEY,
        "limit": limit,
    }

    url = "http://api.openweathermap.org/geo/1.0/direct?"
    r = requests.get(url, params)
    lat = r.json()[0]["lat"]
    lon = r.json()[0]["lon"]
    return {
        "lat": lat,
        "lon": lon,
    }


def get_weather_data(city, state):
    ll = get_lat_lon(city, state)
    params = {
        "lat": ll["lat"],
        "lon": ll["lon"],
        "appid": OPENWEATHER_API_KEY,
        "units": "imperial",
    }

    url = "https://api.openweathermap.org/data/2.5/weather?"
    r = requests.get(url, params)
    temp = r.json()["main"]["temp"]
    description = r.json()["weather"][0]["description"]
    return {
        "temp": temp,
        "description": description.title(),
    }
