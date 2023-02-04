import smtplib
my_email = "std122021@gmail.com"
password = "rqyvxrgfnqtuyoyx"
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='ranapratik1612@gmail.com',
#                         msg="Subject:Hello\n\nThis is second time i send my email")

from random import choice
import datetime as dt

# now=dt.datetime.now()
# date_of_birth=dt.datetime(year=2003,month=12,day=16,hour=12)
# print(date_of_birth)
# print(type(now.year))
# # print(type(now))
# print(now.weekday())
quotes=[]
with open('quotes.txt') as file:
    quotes=file.read().split('\n')
now=dt.datetime.now()
if(now.weekday()==0):
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs='ranapratik1612@gmail.com',msg=f"Subject:Motivational quotes\n\n {choice(quotes)}")
    
