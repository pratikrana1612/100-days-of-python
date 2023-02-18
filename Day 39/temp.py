# print(f"{'https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/flightDeals/prices'}/{5}")
# print('https://api.sheety.co/26bd36fdb21d428925f0599460cdbdac/flightDeals/prices' + f"/{5}")


import datetime as dt
now=dt.datetime.now()
two_hours = now.date() + dt.timedelta(days=180)
new_date=now.date() + dt.timedelta(days=180)
print(now.date().strftime("%d/%m/%Y"))
print(new_date.strftime("%d/%m/%Y"))
print(two_hours)