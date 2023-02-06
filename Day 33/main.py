import requests
import datetime as dt
import smtplib
import time

my_email = "std122021@gmail.com"
password = "rqyvxrgfnqtuyoyx"
MY_LAT = 23.0315293
MY_LNG = 72.6032779


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    iss_position = (float(data['iss_position']['latitude']),
                    float(data['iss_position']['longitude']))
    if (iss_position[0]-MY_LAT <= 5 and iss_position[1]-MY_LNG <= 5):
        return True
    # print(iss_position)
    # # if response.status_code!=200:
    # #     print("Error")


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(
        'https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    my_hour = dt.datetime.now().hour
    if (my_hour < sunrise or my_hour > sunset):
        return True
    # print(sunrise)
    # print(sunset)
# print(now.time().hour)


def email_checker():
    if(is_iss_overhead() and is_night()):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='ranapratik1612@gmail.com',
                                msg="Subject:It's time to see iss space station\n\nUpar juvo station tamari aaju baju j che")

while True:
    time.sleep(60)
    email_checker()
