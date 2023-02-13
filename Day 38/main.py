import requests
import datetime as dt
APP_ID = '510c188f'
API_kEY = '7073afd711eb032f6d15ffb4c0095556'
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
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(url, json=parameters, headers=headers)
data = response.json()
# print(data)
sheety_url = 'https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/myWorkouts/workouts'
now = dt.datetime.now()
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
    response = requests.post(sheety_url, json=body)
    print(response.text)
    # print(data)
