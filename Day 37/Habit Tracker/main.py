import requests


USERNAME="pratik16"
TOKEN="fadk;fadlfkasdfa"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "fadk;fadlfkasdfa",
    "username": "pratik16",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_cofing={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
response=requests.post(url=graph_endpoint,json=graph_cofing,headers=headers)
print(response.text)