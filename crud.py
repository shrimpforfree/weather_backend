from sqlalchemy.orm import Session
from models import WeatherRecord
from schemas import WeatherCreate, WeatherUpdate
from weather import fetch_weather_by_city


def create_weather_record(db: Session, weather_in: WeatherCreate):
    # fetch weather from API
    weather_data = fetch_weather_by_city(weather_in.location)

    db_record = WeatherRecord(
        location=weather_data["location"],
        temperature=weather_data["temperature"],
        description=weather_data["description"],
        map_url=weather_data["map_url"],
        start_date=weather_in.start_date,
        end_date=weather_in.end_date
    )


    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_all_weather_records(db: Session):
    return db.query(WeatherRecord).all()

def update_weather_record(db: Session, record_id: int, update_data: WeatherUpdate):
    record = db.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()

    if not record:
        return None  # You can raise HTTPException if you prefer

    new_weather = fetch_weather_by_city(update_data.location)

    record.location = new_weather["location"]
    record.temperature = new_weather["temperature"]
    record.description = new_weather["description"]
    record.start_date = update_data.start_date
    record.end_date = update_data.end_date

    db.commit()
    db.refresh(record)
    return record

def delete_weather_record(db: Session, record_id: int):
    record = db.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()
    if not record:
        return None

    db.delete(record)
    db.commit()
    return record


