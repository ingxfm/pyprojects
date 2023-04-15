import requests
from datetime import datetime as dt
import os

APP_ID = os.environ["NUTRI_ID"]
API_KEY = os.environ["NUTRI_KEY"]
API_ENDPOINT: str = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercises_input = input("Tell me the exercises you did: ").lower()
exercise_config: dict = {
    "query": exercises_input,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 175.2,
    "age": 39,
}

headers: dict = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=API_ENDPOINT, json=exercise_config, headers=headers)
response.raise_for_status()
exercise_data = response.json()["exercises"]

today = dt.today().strftime("%d/%m/%Y")
time_now = dt.now().strftime("%H:%M:%S")
# print(time_now)

PROJECT_NAME = "workouts"
SHEETY_USER = os.environ["NAME"]
SHEETY_EMAIL = os.environ["EMAIL_TO"]
SHEETY_ENDPOINT: str = os.environ["SH_URL"]

headers_post: dict = {
    "Authorization": os.environ["SH_KEY"],
}

for exercise in range(len(exercise_data)):
    post_config = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise_data[exercise]["name"].title(),
            "duration": exercise_data[exercise]["duration_min"],
            "calories": exercise_data[exercise]["nf_calories"],
        }
    }
    response_post = requests.post(url=SHEETY_ENDPOINT, json=post_config, headers=headers_post)
    response_post.raise_for_status()
