from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WeatherCreate(BaseModel):
    location: str
    start_date: str
    end_date: str

class WeatherOut(BaseModel):
    id: int
    location: str
    temperature: float
    description: str
    date_requested: datetime
    start_date: str
    end_date: str
    map_url: str

    model_config = {
        "from_attributes": True
    }

class WeatherUpdate(BaseModel):
    location: str
    start_date: str
    end_date: str

