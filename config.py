import os

WEATHER_API_KEY = os.getenv('16d2462a5f7f467b846a2f1bcc26231a')
TRAFFIC_API_KEY = os.getenv('AIzaSyDsaPooCEEFr__oGW5wAJXYIZH5WYStZJs')
DATABASE_URL = 'sqlite:///zebrinha_azul.db'

if not WEATHER_API_KEY or not TRAFFIC_API_KEY:
    raise ValueError("Chaves de API não configuradas nas variáveis de ambiente")
