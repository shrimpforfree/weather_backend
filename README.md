# AI Weather Backend – Technical Assessment (AI Engineer Intern)

This project is the **backend portion** of a weather app for the AI Engineer Intern assessment. It allows users to:
- Get real-time weather for any location
- Store and retrieve past weather queries
- Export data in multiple formats
- View related YouTube videos and Google Maps
- Perform full CRUD operations with validation and error handling

---

## Features

- Real-time weather from WeatherAPI.com
- Full CRUD (Create, Read, Update, Delete)
- Google Maps integration (clickable location links)
- YouTube API integration (travel-related videos)
- Export to **JSON**, **CSV**, **Markdown**
- Graceful error handling
- SQL (SQLite) database with SQLAlchemy


---

## How to Run
## 1. Clone & Set Up Environment


git clone https://github.com/yourusername/weather_backend.git
cd weather_backend
python -m venv venv
venv\Scripts\activate   # (Windows) or source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt

## 2. Create .env file in the root:
    WEATHERAPI_KEY=your_weatherapi_key
    YOUTUBE_API_KEY=your_youtube_api_key
    
## 3. Run The APP
uvicorn main:app --reload




