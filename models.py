from sqlalchemy import Column, Integer, String, Float, DateTime
from db import Base
from datetime import datetime

class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)
    date_requested = Column(DateTime, default=datetime.utcnow)
    start_date = Column(String)
    end_date = Column(String)
    map_url = Column(String)

