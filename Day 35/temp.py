import requests

api_key = "8b452bef21b1077a662cbf462269699b"
city = "London,UK"

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(weather_url)
data = response.json()
print(data)
# current_temperature = data["main"]["temp"]
# current_humidity = data["main"]["humidity"]
# current_description = data["weather"][0]["description"]

# print(f"Temperature: {current_temperature}°C")
# print(f"Humidity: {current_humidity}%")
# print(f"Description: {current_description}")


