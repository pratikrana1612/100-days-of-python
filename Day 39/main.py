# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# import all classes
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# creating objects from classes
flight_search = FlightSearch()
data = DataManager()
sheet_data = data.make_get_requests()
pprint(sheet_data)

# if iata code is empty then full fill it
if (sheet_data['prices'][0]['iataCode'] == ''):
    for row in sheet_data['prices']:
        row['iataCode'] = flight_search.iata_code(row['city'])
    data.make_put_requests(sheet_data['prices'])

# list for all flights and checking for flights are available for our trip and storing those data into flight_data and making objects of it
flights = []
for row in sheet_data['prices']:
    response = flight_search.get_trip('LON', row['iataCode'])
    # pprint(response)
    response = response['data']
    try:
        response = response[0]
        flights.append(FlightData(response['airlines'],
                                  response['availability']['seats'],
                                  response['route'][0]['cityFrom'],
                                  response['route'][0]['cityTo'],
                                  response['route'][0]['cityCodeFrom'],
                                  response['route'][0]['cityCodeTo'],
                                  response['price'],
                                  response['route'][0]['local_departure'].split("T")[
            0],
            response['route'][1]['local_departure'].split("T")[0]))
    except IndexError:
        print("no data found")
    # print("****************************************************")


# if price is less then sending email
for index in range(len(flights)):
    if (flights[index].price <= sheet_data['prices'][index]["lowestPrice"]):
        make_email = NotificationManager(flights[index])
    print(
        f"{flights[index].toCity}:${flights[index].price}:${sheet_data['prices'][index]['lowestPrice']}")
    # print(f"out_date:{city.out_date},return_date:{city.return_date}")
# pprint(sheet_data)
# data_sheet=data.make_requests()
# print(data_sheet)
