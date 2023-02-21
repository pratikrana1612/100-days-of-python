import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = 'https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/flightDeals/prices'
        self.headers={'Authorization': 'Basic dHJhdmVsOnRyYXZlbDEyMw=='}

    def make_get_requests(self):
        response = requests.get(self.url,headers=self.headers)
        return response.json()

    def make_put_requests(self,sheet_data):
        for city in sheet_data:
            print(city)
            body=  {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response=requests.put(f"{self.url}/{city['id']}",json=body,headers=self.headers)
            print(response.text)

    def put_users(self,FirstName,LastName,Email):
        body={
        "user":{
            "firstName":FirstName,
            "lastName":LastName,
            "email":Email
        }
        }
        response=requests.get('https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/flightDeals/users',headers=self.headers)
        # response=requests.post('https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/flightDeals/users',json=body,headers=self.headers)
        print(response.json())
