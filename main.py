import requests
from datetime import datetime as dt

GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 184.5
AGE = 22

APP_ID = {}
API_KEY = {}
TOKEN_BEARER = {"Authorization": "Bearer {}"}

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "{}s"

exercise_text = input("Input your excerice:\n")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=excercise_endpoint, json=parameters, headers=headers)
result = response.json()

exercise_name = result['exercises'][0]['name']
exercise_cal = result['exercises'][0]['nf_calories']
exercise_dur = result['exercises'][0]['duration_min']

today = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

data = {
    "workout": {
        "date": today,
        "time": now_time,
        "exercise": exercise_name.title(),
        "duration": f"{exercise_dur}",
        "calories": f"{exercise_cal}",
    }
}

print(exercise_dur)
response = requests.post(url=sheety_endpoint, json=data, headers=TOKEN_BEARER)
response = response.json()
print(response)
