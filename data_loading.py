from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data_model import WeatherData, TrafficData, create_db_and_tables
from data_extraction import fetch_weather_data, fetch_traffic_data
from data_transformation import clean_weather_data, clean_traffic_data

def load_data(session, model, df):
    for index, row in df.iterrows():
        print(f"Loading row: {row.to_dict()}")
        record = model(**row.to_dict())
        session.add(record)
    session.commit()

# Configurar o Banco de Dados
engine = create_db_and_tables('sqlite:///zebrinha_azul.db')
Session = sessionmaker(bind=engine)
session = Session()

# Chaves das APIs
weather_api_key = '16d2462a5f7f467b846a2f1bcc26231a'
traffic_api_key = 'AIzaSyDsaPooCEEFr__oGW5wAJXYIZH5WYStZJs'

# Locais e Rota de Exemplo
location = "London"
origin = "New York"
destination = "Los Angeles"

# Extração de Dados
weather_data = fetch_weather_data(weather_api_key, location)
traffic_data = fetch_traffic_data(traffic_api_key, origin, destination)

# Limpeza e Transformação dos Dados
cleaned_weather_data = clean_weather_data(weather_data)
cleaned_traffic_data = clean_traffic_data(traffic_data)

# Carregar Dados no Banco de Dados
print("Cleaned Weather Data:")
print(cleaned_weather_data)

print("Cleaned Traffic Data:")
print(cleaned_traffic_data)

load_data(session, WeatherData, cleaned_weather_data)
load_data(session, TrafficData, cleaned_traffic_data)
