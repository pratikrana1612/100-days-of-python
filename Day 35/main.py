import requests
api_key = '8b452bef21b1077a662cbf462269699b'
url = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {
    "lat": 20.593683,
    "long": 78.962883,
    # "city":"ahmedabad,india",
    "appid": '8b452bef21b1077a662cbf462269699b',
    # "exlude":"current,minutely,daily"
}


response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
