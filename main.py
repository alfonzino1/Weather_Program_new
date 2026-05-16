import os
from fastapi import FastAPI
from dotenv import load_dotenv
import requests
# Грузим переменные окружения
load_dotenv()

app = FastAPI()

@app.get("/")

def home():
    api_key = os.getenv("WEATHER_API_KEY")
    city = os.getenv("CITY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    respone =requests.get(url)
    data = respone.json()
    if respone.status_code == 200:
        temp = data["main"]["temp"]
        return {
            "city": city,
            "temperatyra": f"{temp} C"
        }
    else:
        return {"error:":data.get("message", "unknown error")}
