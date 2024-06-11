import pandas as pd
from datetime import datetime

def clean_weather_data(data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    
    df = pd.DataFrame([data])
    
    print("Initial Weather DataFrame:")
    print(df)
    
    for column in df.columns:
        if isinstance(df[column].iloc[0], (dict, list)):
            print(f"Removing column {column} with dict or list values")
            df = df.drop(columns=[column])
    
    print("Weather DataFrame after removing dict/list columns:")
    print(df)
    
    df.drop_duplicates(inplace=True)
    df['dt'] = pd.to_datetime(df['dt'], unit='s')
    df['location'] = 'London'
    df['temperature'] = temperature
    df['humidity'] = humidity
    df.rename(columns={
        'dt': 'datetime'
    }, inplace=True)
    
    print("Final Weather DataFrame:")
    print(df)
    
    return df[['location', 'temperature', 'humidity', 'datetime']]

def clean_traffic_data(data):
    routes = data.get('routes', [])
    if not routes:
        print("No routes found in the traffic data.")
        return pd.DataFrame(columns=['origin', 'destination', 'duration_seconds', 'distance_meters', 'datetime'])
    
    legs = [route['legs'][0] for route in routes]
    df = pd.json_normalize(legs)
    
    print("Initial Traffic DataFrame:")
    print(df)
    
    for column in df.columns:
        if isinstance(df[column].iloc[0], list):
            print(f"Removing column {column} with list values")
            df = df.drop(columns=[column])
    
    df.drop_duplicates(inplace=True)
    df['origin'] = 'New York'
    df['destination'] = 'Los Angeles'
    df['datetime'] = pd.to_datetime('now')
    df.rename(columns={
        'duration.value': 'duration_seconds',
        'distance.value': 'distance_meters',
        'datetime': 'datetime'
    }, inplace=True)
    
    print("Final Traffic DataFrame:")
    print(df)
    
    return df[['origin', 'destination', 'duration_seconds', 'distance_meters', 'datetime']]
