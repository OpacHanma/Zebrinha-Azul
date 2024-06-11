import dash
from dash import dcc, html
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_model import WeatherData, TrafficData
import pandas as pd

# Configurar conexão com o banco de dados
engine = create_engine('sqlite:///zebrinha_azul.db')
Session = sessionmaker(bind=engine)
session = Session()

# Consultar dados de clima e tráfego
weather_data = session.query(WeatherData).all()
traffic_data = session.query(TrafficData).all()

# Transformar dados em DataFrames
weather_df = pd.DataFrame([{
    'location': data.location,
    'temperature': data.temperature,
    'humidity': data.humidity,
    'datetime': data.datetime
} for data in weather_data])

traffic_df = pd.DataFrame([{
    'origin': data.origin,
    'destination': data.destination,
    'duration_seconds': data.duration_seconds,
    'distance_meters': data.distance_meters,
    'datetime': data.datetime
} for data in traffic_data])

# Criar visualizações com Plotly
weather_fig = px.line(weather_df, x='datetime', y='temperature', title='Temperature Over Time')
traffic_fig = px.scatter(traffic_df, x='distance_meters', y='duration_seconds', title='Traffic Duration vs Distance')

# Inicializar o Dash
app = dash.Dash(__name__)

# Layout do Dash
app.layout = html.Div(children=[
    html.H1(children='Zebrinha Azul Data Visualization'),

    html.Div(children='''
        Weather Data:
    '''),
    dcc.Graph(
        id='weather-graph',
        figure=weather_fig
    ),

    html.Div(children='''
        Traffic Data:
    '''),
    dcc.Graph(
        id='traffic-graph',
        figure=traffic_fig
    )
])

# Executar o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True)
