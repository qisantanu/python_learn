# from typing import List, Optional
from pydantic import BaseModel


class WeatherRequest(BaseModel):
    lat: float
    lon: float    

### CREATE SCHEMAs ###

class WeatherResponse(BaseModel):
    city: str
    temparature: float
    description: str

class WeatherErrorResponse(BaseModel):
    cod: int
    message: str
