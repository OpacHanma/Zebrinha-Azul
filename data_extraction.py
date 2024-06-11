import requests
from config import WEATHER_API_KEY, TRAFFIC_API_KEY
from utils.logger import logger

def fetch_weather_data(location):
    logger.info(f"Fetching weather data for {location}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_traffic_data(origin, destination):
    logger.info(f"Fetching traffic data from {origin} to {destination}")
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={TRAFFIC_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
