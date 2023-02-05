##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
from random import choice
import smtplib

email='std122021@gmail.com'
password="rqyvxrgfnqtuyoyx"

now = dt.datetime.now()
letters = []
with open('letter_templates/letter_1.txt') as file:
    letter = file.read()
    letters.append(letter)
with open('letter_templates/letter_2.txt') as file:
    letter = file.read()
    letters.append(letter)
with open('letter_templates/letter_2.txt') as file:
    letter = file.read()
    letters.append(letter)
# for letter in letters:
#     print(letter)
# print(letters)
data = pandas.read_csv('birthdays.csv')
for (index, row) in data.iterrows():
    if (now.month == row['month'] and now.day == row['day']):
        # print("it's your birthday")
        letter = choice(letters)
        letter=letter.replace('[NAME]',row['name']).replace('Angela',"Pratik")
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email,to_addrs='ranapratik1612@gmail.com',msg=f'Subject:Birthday Wish\n\n{letter}')
        # letter.replace('Angela','afad')
