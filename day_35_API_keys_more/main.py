import requests
import os
from twilio.rest import Client

# TODO 1: get latitude and longitude (Prague)
LATITUDE: float = 35.002460
LONGITUDE: float = -5.903560

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

OWM_KEY: str = os.environ["OWM_API_KEY"]
OWM_ENDPOINT: str = "https://api.openweathermap.org/data/2.5/onecall"

parameters: dict = {
    "lat": LATITUDE,
    "lon": {LONGITUDE},
    "exclude": "current,minutely,daily,alerts",
    "appid": OWM_KEY,
}

# TODO 2: make a request to the One Call API using the requests module
response = requests.get(OWM_ENDPOINT, params=parameters)

# TODO 3: print out the HTTP status code that you get back
print(f"{response.status_code}\n")

# TODO 4: print the response to the console
# TODO 5: take the next 12 hours data
data = response.json()["hourly"][:12]
print(data)
print(len(data))

rainy_hours = [data[id_item]["weather"][0]["id"] for id_item in range(len(data))
               if int(data[id_item]["weather"][0]["id"]) < 700]

if rainy_hours:
    # print(rainy_hours)
    print("Bring an umbrella.")
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
                     body="Good morning. Take an umbrella.",
                     from_=os.environ["FROM_NUMBER"],
                     to=os.environ["TO_NUMBER"],
    )

print(message.sid)

# # TODO: her way
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
#
# will_rain = False
#
#
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring an umbrella.")












