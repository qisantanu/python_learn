from fastapi import HTTPException, APIRouter
from typing import Union
from pydantic import BaseModel
import httpx
from models.weather_model import WeatherResponse, WeatherErrorResponse
import json
from dotenv import dotenv_values

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

    config = dotenv_values(".env")

    api_key = config['WEATHER_API_KEY']
    weather_service_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}' 
    print(weather_service_url)
    response = httpx.get(weather_service_url)
    parsed_reponse = json.loads(response.text)

    if response.status_code != 200:
      return parsed_reponse
    else:
      return { 
         'city': parsed_reponse['name'], 
         'temparature': parsed_reponse['main']['temp'], 
         'description': parsed_reponse['weather'][0]['description']
      }

    # return dummy_data