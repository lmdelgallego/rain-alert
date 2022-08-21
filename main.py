import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

parameters = {
    "lat": 4.723514,
    "lon": -74.040685,
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
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ.get('https_proxy')}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️️",
        from_='+12513069861',
        to='+573004523529'
    )

    print(message.status)
    print(message.body)
