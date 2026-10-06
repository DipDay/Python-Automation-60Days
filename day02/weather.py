import requests
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 23.7104,
	"longitude": 90.4074,
	"daily": "weather_code",
	"hourly": "temperature_2m",
	"timezone": "auto",
}
r = requests.get(url, params = params)
# print(r.url)
weather_data = r.json()
# print(weather_data)
print(f"Coordinates: {weather_data["latitude"]}°N {weather_data["longitude"]}°E")
print(f"Elevation: {weather_data["elevation"]} m asl")
print(f"Timezone: {weather_data["timezone"]} {weather_data["timezone_abbreviation"]}")

current_time_str = datetime.now().strftime("%Y-%m-%dT%H:00")
# print(current_time_str)
current_index = weather_data["hourly"]["time"].index(current_time_str)
print(f"Current Temperature: {weather_data["hourly"]["temperature_2m"][current_index]} °C")
