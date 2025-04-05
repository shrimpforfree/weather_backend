from fastapi import FastAPI
from db import Base, engine
from weather import fetch_weather_by_city
from fastapi import Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import crud
from schemas import WeatherCreate, WeatherOut
from youtube import search_youtube_videos


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/current-weather")
def get_current_weather(city: str):
    try:
        result = fetch_weather_by_city(city)
        return result
    except Exception as e:
        return {"error": str(e)}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/weather/create", response_model=WeatherOut)
def create_weather(weather: WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather_record(db, weather)

from typing import List

@app.get("/weather/read", response_model=List[WeatherOut])
def read_all_weather(db: Session = Depends(get_db)):
    return crud.get_all_weather_records(db)

from schemas import WeatherUpdate
from fastapi import HTTPException

@app.put("/weather/update/{record_id}", response_model=WeatherOut)
def update_weather(record_id: int, weather_update: WeatherUpdate, db: Session = Depends(get_db)):
    result = crud.update_weather_record(db, record_id, weather_update)
    if result is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

@app.delete("/weather/delete/{record_id}", response_model=WeatherOut)
def delete_weather(record_id: int, db: Session = Depends(get_db)):
    result = crud.delete_weather_record(db, record_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return result

from utils import export_weather_data
from fastapi.responses import FileResponse

@app.get("/weather/export")
def export_data(format: str = "json", db: Session = Depends(get_db)):
    records = crud.get_all_weather_records(db)

    try:
        file_path = export_weather_data(records, format)
        return FileResponse(path=file_path, filename=file_path, media_type='application/octet-stream')
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported format. Use 'json', 'csv', or 'md'")

from youtube import search_youtube_videos  # ✅ make sure this import is at the top

@app.get("/youtube")
def get_youtube_videos(location: str):
    try:
        videos = search_youtube_videos(location + " travel")
        return {"location": location, "videos": videos}
    except Exception as e:
        return {"error": str(e)}





