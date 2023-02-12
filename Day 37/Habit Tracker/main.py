import datetime as dt
import requests


USERNAME = "pratik16"
TOKEN = "fadk;fadlfkasdfa"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "fadk;fadlfkasdfa",
    "username": "pratik16",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_cofing = {
    "id": "graph1",
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_cofing,headers=headers)
# print(response.text)
# now = dt.datetime(year=2023,month=2,day=1)
now = dt.datetime(year=2023,month=2,day=1)
# month =  "0"+ str(now.month) if now.month < 9 else now.month
# day =  "0"+ str(now.day) if now.day < 9 else now.day
endpoint_post_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
post_pixel_json = {
    "date":now.strftime("%Y%m%d"),
    "quantity": input("How many Kilo meters did you cycle today?")
}
response = requests.post(
    endpoint_post_pixel, json=post_pixel_json, headers=headers)
# response=requests.delete(endpoint_post_pixel,json=post_pixel_json,headers=headers)
print(response.text)
