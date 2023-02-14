import requests
import datetime as dt
import os
APP_ID = os.environ.get("APP_ID")
API_kEY = os.environ.get("API_KEY")
parameters = {
    "query": input("Tell me which excercise you did:"),
    "gender": "male",
    "weight_kg": 64,
    "height_cm": 164.64,
    "age": 20
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_kEY
}
url = os.environ.get('NUTRITION_URL')
response = requests.post(url, json=parameters, headers=headers)
data = response.json()
# print(data)
sheety_url = os.environ.get('SHEETLY_URL')
now = dt.datetime.now()
headers={
    "Authorization":os.environ.get("SHEETLY_KEY")
}
for excercise in data['exercises']:
    body = {
        'workout': {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": f"{excercise['name'].title()}",
            "duration": f"{excercise['duration_min']}min",
            "calories": f"{excercise['nf_calories']}",
        }
    }

    # requests.delete(sheety_url+'/3')
    response = requests.post(sheety_url, json=body,headers=headers)
    print(response.text)
    # print(data)
