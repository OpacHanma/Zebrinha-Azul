import pytest
from data_extraction import fetch_weather_data, fetch_traffic_data

def test_fetch_weather_data():
    data = fetch_weather_data("London")
    assert 'main' in data, "Key 'main' not in weather data"
    assert 'temp' in data['main'], "Key 'temp' not in weather data"

def test_fetch_traffic_data():
    data = fetch_traffic_data("New York", "Los Angeles")
    assert 'routes' in data, "Key 'routes' not in traffic data"
