# Note:3.0 wants subscription and phone number api also

import requests
api_key = '8b452bef21b1077a662cbf462269699b'
url = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    "lat": 20.593683,
    "lon": 78.962883,
    "appid": api_key,
    # "city":"ahmedabad,india",
    # "exlude":"current,minutely,daily"
}

# will_rain=False
# for hour in hourly:
#     for idx in json[hour]['weather']:
#         if(json[hour]['weather'][idx]['id']<700):
#             will_rain=True

# if will_rain:
#     print("Bring umbrella")
response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
