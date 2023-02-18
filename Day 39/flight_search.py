import requests
import datetime as dt
now=dt.datetime.now()


TEQUILA_API_KEY='enn20upyvj-3_cQgp8_XS3jb5ixJtTS1'


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url='https://api.tequila.kiwi.com/'
        self.headers={"apikey":TEQUILA_API_KEY}

    def iata_code(self,city):
        paramters={'term':city,'location_types':'city'}
        response=requests.get(url=f"{self.url}locations/query?",params=paramters,headers=self.headers)
        response=response.json()
        return response['locations'][0]['code']

    def get_trip(self,origin_city_code,destination_city_code):
        start_date=now.date()
        end_date=now.date() + dt.timedelta(days=180)
        pamraters={
            'fly_from':origin_city_code,
            'fly_to':destination_city_code,
            'date_from':start_date.strftime("%d/%m/%Y"),
            'date_to':end_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        respnose=requests.get(f"{self.url}v2/search",params=pamraters,headers=self.headers)
        return respnose.json()