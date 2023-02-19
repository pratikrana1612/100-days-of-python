import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,data):
        self.email='std122021@gmail.com'
        self.password='rqyvxrgfnqtuyoyx'
        self.message=f'Low Price alert! Only £{data.price} to fly from {data.fromCity}-{data.cityCodeFrom} \nto {data.toCity}-{data.cityCodeTo} from {data.out_date} to {data.return_date}.'
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=self.email,password=self.password)
            connection.sendmail(from_addr=self.email,to_addrs='ranapratik1612@gmail.com',msg=f"Subject:'Time to Trip'\n\n{self.message}".encode('utf-8'))