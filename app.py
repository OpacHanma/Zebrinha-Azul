import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
import os
from validation import validate_location  # Importe a função de validação

# Obtenha as chaves de API das variáveis de ambiente
weather_api_key = os.getenv('WEATHER_API_KEY')
traffic_api_key = os.getenv('TRAFFIC_API_KEY')

# Conecte-se ao banco de dados
engine = create_engine('sqlite:///zebrinha_azul.db')

# Leia os dados de clima e trânsito
weather_df = pd.read_sql('weather_data', engine)
traffic_df = pd.read_sql('traffic_data', engine)

# Adicionar mais localizações fictícias para demonstrar
additional_locations = pd.DataFrame([
    {'location': 'Paris', 'temperature': 293.15, 'humidity': 60, 'datetime': '2024-06-11 12:42:55'},
    {'location': 'Tokyo', 'temperature': 298.15, 'humidity': 70, 'datetime': '2024-06-11 12:42:55'}
])
weather_df = pd.concat([weather_df, additional_locations], ignore_index=True)

# Converta a coluna 'datetime' para o tipo datetime
weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
traffic_df['datetime'] = pd.to_datetime(traffic_df['datetime'])

# Converta a temperatura de Kelvin para Celsius
weather_df['temperature'] = weather_df['temperature'] - 273.15

# Inicialize o app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do app
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Painel de Dados de Clima e Tráfego", className="text-center"), className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='weather-graph'),
                dcc.Graph(id='traffic-graph')
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='location-dropdown',
                    options=[{'label': loc, 'value': loc} for loc in weather_df['location'].unique()],
                    value='London',
                    clearable=False,
                    style={"width": "50%"}
                )
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=weather_df['datetime'].min(),
                    end_date=weather_df['datetime'].max(),
                    display_format='YYYY-MM-DD'
                )
            ])
        ])
    ])
])

# Callbacks para atualizar os gráficos com base nos controles interativos
@app.callback(
    Output('weather-graph', 'figure'),
    Output('traffic-graph', 'figure'),
    Input('location-dropdown', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_graphs(selected_location, start_date, end_date):
    # Valide a localização selecionada
    try:
        validate_location(selected_location)
    except ValueError as e:
        return {
            'data': [],
            'layout': {'title': str(e)}
        }, {
            'data': [],
            'layout': {'title': str(e)}
        }

    filtered_weather_df = weather_df[
        (weather_df['location'] == selected_location) &
        (weather_df['datetime'] >= start_date) &
        (weather_df['datetime'] <= end_date)
    ]
    filtered_traffic_df = traffic_df[
        (traffic_df['datetime'] >= start_date) &
        (traffic_df['datetime'] <= end_date)
    ]

    weather_fig = {
        'data': [
            {
                'x': filtered_weather_df['datetime'],
                'y': filtered_weather_df['temperature'],
                'type': 'line',
                'name': 'Temperature (°C)',
                'line': {'color': 'blue'}
            },
            {
                'x': filtered_weather_df['datetime'],
                'y': filtered_weather_df['humidity'],
                'type': 'line',
                'name': 'Humidity (%)',
                'line': {'color': 'green'}
            }
        ],
        'layout': {
            'title': f'Dados de Clima para {selected_location}',
            'xaxis': {'title': 'Data'},
            'yaxis': {'title': 'Valores'},
            'legend': {'x': 0, 'y': 1, 'bgcolor': 'rgba(255, 255, 255, 0.5)'}
        }
    }

    traffic_fig = {
        'data': [
            {
                'x': filtered_traffic_df['datetime'],
                'y': filtered_traffic_df['duration_seconds'],
                'type': 'line',
                'name': 'Duration (seconds)',
                'line': {'color': 'red'}
            },
            {
                'x': filtered_traffic_df['datetime'],
                'y': filtered_traffic_df['distance_meters'],
                'type': 'line',
                'name': 'Distance (meters)',
                'line': {'color': 'purple'}
            }
        ],
        'layout': {
            'title': 'Dados de Trânsito',
            'xaxis': {'title': 'Data'},
            'yaxis': {'title': 'Valores'},
            'legend': {'x': 0, 'y': 1, 'bgcolor': 'rgba(255, 255, 255, 0.5)'}
        }
    }

    return weather_fig, traffic_fig

# Execute o app
if __name__ == '__main__':
    app.run_server(debug=True)
