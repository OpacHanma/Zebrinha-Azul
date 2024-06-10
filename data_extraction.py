import requests

def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def fetch_traffic_data(api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    weather_api_key = 'Y16d2462a5f7f467b846a2f1bcc26231a'
    traffic_api_key = 'AIzaSyCO8x0KhEGJhNtNtZhNU3weuu3ljIAARTk'
    location = "London"
    origin = "New York"
    destination = "Los Angeles"
    
    weather_data = fetch_weather_data(weather_api_key, location)
    print("Weather Data:", weather_data)
    
    traffic_data = fetch_traffic_data(traffic_api_key, origin, destination)
    print("Traffic Data:", traffic_data)
