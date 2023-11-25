import requests
from datetime import datetime

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "APP_ID"
APP_KEY = "APP_KEY"

SHEET_ENDPOINT = "your sheet enpoint"

exercise_text = input("Tell which exercise you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameter = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 81.5,
    "height_cm": 191.84,
    "age": 55
}

response = requests.post(END_POINT, json=parameter, headers=headers)
result = response.json()
print(result)

#create account on https://dashboard.sheety.com and get post add enabled
today_date = datetime.now().strftime("%x")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input ={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT,json=sheet_input, auth=(
        "username",
        "password"
       )
    )
    print(sheet_response.text)
