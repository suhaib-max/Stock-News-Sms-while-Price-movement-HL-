import requests

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "APP_ID"
APP_KEY = "APP_KEY"


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
