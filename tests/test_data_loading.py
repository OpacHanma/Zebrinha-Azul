import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_model import WeatherData, TrafficData, create_db_and_tables
from data_loading import load_data
from data_transformation import clean_weather_data, clean_traffic_data

@pytest.fixture(scope='module')
def db_session():
    engine = create_engine('sqlite:///:memory:')
    create_db_and_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_load_weather_data(db_session):
    sample_data = {
        "main": {
            "temp": 280.32,
            "humidity": 81
        },
        "dt": 1605182400
    }
    weather_df = clean_weather_data(sample_data)
    print("Weather DataFrame:")
    print(weather_df)
    load_data(db_session, WeatherData, weather_df)
    
    result = db_session.query(WeatherData).all()
    assert len(result) == 1, "Nenhum dado de clima foi carregado no banco de dados"
    assert result[0].temperature == 280.32, "A temperatura dos dados carregados está incorreta"

def test_load_traffic_data(db_session):
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
    traffic_df = clean_traffic_data(sample_data)
    print("Traffic DataFrame:")
    print(traffic_df)
    load_data(db_session, TrafficData, traffic_df)
    
    result = db_session.query(TrafficData).all()
    assert len(result) == 1, "Nenhum dado de tráfego foi carregado no banco de dados"
    assert result[0].duration_seconds == 3600, "A duração dos dados carregados está incorreta"
