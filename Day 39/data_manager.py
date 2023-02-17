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
        for i in range(2,11):
            print(sheet_data['prices'][i-2])
            # body= {
            #     'price':{
            #         'city':sheet_data['prices'][i-2]['city'],
            #         'iatacode':sheet_data['prices'][i-2]['iataCode'],
            #         'lowestPrice':sheet_data['prices'][i-2]['lowestPrice']
            #     }
            # }
            requests.put(self.url+f'/{i}',json=body,headers=self.headers)