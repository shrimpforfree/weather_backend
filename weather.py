import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHERAPI_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def fetch_weather_by_city(city: str):
    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.json().get('error', {}).get('message', 'Unknown error')}")

    data = response.json()
    location_name = f"{data['location']['name']}, {data['location']['country']}"
    query_for_map = location_name.replace(" ", "+")

    result = {
        "temperature": data["current"]["temp_c"],
        "description": data["current"]["condition"]["text"],
        "location": location_name,
        "map_url": f"https://www.google.com/maps/search/?api=1&query={query_for_map}"
    }
    return result

def fetch_youtube_videos(query: str, max_results: int = 3):
    YT_API_KEY = os.getenv("YOUTUBE_API_KEY")
    YT_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": f"weather in {query}",
        "key": YT_API_KEY,
        "type": "video",
        "maxResults": max_results
    }

    response = requests.get(YT_SEARCH_URL, params=params)
    if response.status_code != 200:
        return []

    videos = response.json().get("items", [])
    return [
        {
            "title": video["snippet"]["title"],
            "video_url": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        }
        for video in videos
    ]

