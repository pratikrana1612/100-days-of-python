class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,airlines,availability,fromCity,toCity,cityCodeFrom,cityCodeTo,price,out_date,return_date):
        self.airlines=airlines
        self.fromCity=fromCity
        self.toCity=toCity
        self.availability=availability
        self.cityCodeFrom=cityCodeFrom
        self.cityCodeTo=cityCodeTo
        self.price=price
        self.out_date=out_date
        self.return_date=return_date
        