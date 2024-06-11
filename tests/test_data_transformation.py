import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from data_transformation import clean_weather_data, clean_traffic_data

def test_clean_weather_data():
    sample_data = {
        "main": {
            "temp": 280.32,
            "humidity": 81
        },
        "dt": 1605182400
    }
    cleaned_data = clean_weather_data(sample_data)
    print("Cleaned Weather DataFrame:")
    print(cleaned_data)
    
    assert not cleaned_data.empty, "Os dados limpos de clima estão vazios"
    assert 'temperature' in cleaned_data.columns, "A coluna 'temperature' não foi encontrada nos dados limpos"
    assert 'datetime' in cleaned_data.columns, "A coluna 'datetime' não foi encontrada nos dados limpos"

def test_clean_traffic_data():
    sample_data = {
        "routes": [
            {
                "legs": [
                    {
                        "duration": {
                            "value": 3600
                        },
                        "distance": {
                            "value": 10000
                        }
                    }
                ]
            }
        ],
        "status": "OK"
    }
    if sample_data.get('error_message'):
        pytest.fail(f"Error fetching traffic data: {sample_data['error_message']}")
    
    cleaned_data = clean_traffic_data(sample_data)
    print("Cleaned Traffic DataFrame:")
    print(cleaned_data)
    
    assert not cleaned_data.empty, "Os dados limpos de tráfego estão vazios"
    assert 'duration_seconds' in cleaned_data.columns, "A coluna 'duration_seconds' não foi encontrada nos dados limpos"
    assert 'distance_meters' in cleaned_data.columns, "A coluna 'distance_meters' não foi encontrada nos dados limpos"
