"""API Endpoints for weather"""

from fastapi import APIRouter
import json
import requests
import os
import datetime
from fastapi import APIRouter
from dotenv import dotenv_values, load_dotenv

router = APIRouter()
load_dotenv()


API_KEY = os.getenv('PROJECT_API_KEY')

@router.get('/get_weather')
async def get_weather(lat,lon):
    """Returns weather data from OpenWeather"""
    '''
    
    # parameters of JSON output. All parameters are in imperial units.
    # FYI - this API can only do a max. of 60 Calls / minute.
    
    coord
        coord.lon City geo location, longitude
        coord.lat City geo location, latitude
    weather (more info Weather condition codes)
        weather.id Weather condition id
        weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
        weather.description Weather condition within the group. You can get the output in your language. Learn more
        weather.icon Weather icon id
    base Internal parameter
    main
        main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
        main.humidity Humidity, %
        main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.sea_level Atmospheric pressure on the sea level, hPa
        main.grnd_level Atmospheric pressure on the ground level, hPa
    wind
        wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
        wind.deg Wind direction, degrees (meteorological)
        wind.gust Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
    clouds
        clouds.all Cloudiness, %
    rain
        rain.1h Rain volume for the last 1 hour, mm
        rain.3h Rain volume for the last 3 hours, mm
    snow
        snow.1h Snow volume for the last 1 hour, mm
        snow.3h Snow volume for the last 3 hours, mm
    dt Time of data calculation, unix, UTC
    sys
        sys.type Internal parameter
        sys.id Internal parameter
        sys.message Internal parameter
        sys.country Country code (GB, JP etc.)
        sys.sunrise Sunrise time, unix, UTC
        sys.sunset Sunset time, unix, UTC
    timezone Shift in seconds from UTC
    id City ID
    name City name
    cod Internal parameter

'''
    
    
    
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, API_KEY)
    response = requests.get(url)
    data = json.loads(response.text)
    return data
    pass