# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
flight_search = FlightSearch()
data = DataManager()
sheet_data = data.make_get_requests()
# pprint(sheet_data)
if (sheet_data['prices'][0]['iataCode'] == ''):
    for row in sheet_data['prices']:
        row['iataCode'] = flight_search.iata_code(row['city'])
    data.make_put_requests(sheet_data['prices'])

for row in sheet_data['prices']:
    response = flight_search.get_trip('LON',row['iataCode'])
    pprint(response)
# pprint(sheet_data)
# data_sheet=data.make_requests()
# print(data_sheet)
