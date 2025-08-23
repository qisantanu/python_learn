from fastapi import HTTPException, APIRouter
from typing import Union
from pydantic import BaseModel
import httpx
from models.weather_model import WeatherResponse, WeatherErrorResponse
import json

router = APIRouter()

@router.get("/get_current_weather_data", tags=['weather'], response_model=Union[WeatherResponse, WeatherErrorResponse])
async def get_weather_data(lat: float = 22.6138, lon: float = 88.4306):
    # Implement logic to fetch weather data from a weather API
    # For simplicity, let's assume we return dummy data
    dummy_data = {
        "city": 'Kolkata',
        "temparature": 30.2,
        "description": "Sunny"
    }

    api_key = 'f3d3a1b9f8b4e4b0c0b0c0b0c0b0c0b0'
    weather_service_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}' 

    response = httpx.get(weather_service_url)
    
    if response.status_code != 200:
      return json.loads(response.text)
    else:
      return response.text

    # return dummy_data