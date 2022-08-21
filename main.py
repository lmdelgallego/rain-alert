import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "049a2388eb5f8f385aa98307d07e3c5b"

parameters = {
    # "lat": 4.723514,
    # "lon": -74.040685,
    "lat": 11.982860,
    "lon": 124.754723,
    "appid": api_key,
    "exclude": "minutely,daily"
}

response_weather = requests.get(url=OWM_ENDPOINT, params=parameters)
response_weather.raise_for_status()
weather_data = response_weather.json()
weather_slice = weather_data.get('hourly')[:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data.get("weather")[0].get("id")
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

# print(current_weather.get('hourly')[0].get('weather')[0])

