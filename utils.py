import pandas as pd
from models import WeatherRecord
from typing import List
from fastapi.responses import FileResponse
import os

def export_weather_data(records: List[WeatherRecord], format: str = "json"):
    data = [
        {
            "id": r.id,
            "location": r.location,
            "temperature": r.temperature,
            "description": r.description,
            "date_requested": r.date_requested,
            "start_date": r.start_date,
            "end_date": r.end_date,
        }
        for r in records
    ]

    df = pd.DataFrame(data)
    filename = f"weather_export.{format}"

    if format == "csv":
        df.to_csv(filename, index=False)
    elif format == "json":
        df.to_json(filename, orient="records", indent=2)
    elif format == "md":
        df.to_markdown(buf=filename, index=False)
    else:
        raise ValueError("Unsupported format")

    return filename

import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube_videos(query: str, max_results=3):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("YouTube API error: " + response.text)

    items = response.json().get("items", [])
    results = []

    for item in items:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        thumbnail = item["snippet"]["thumbnails"]["high"]["url"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        results.append({
            "title": title,
            "url": video_url,
            "thumbnail": thumbnail
        })

    return results
