import requests
import datetime as dt
import smtplib
# from email.mime.text import MIMEText
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = '6JHQ82EWFZIXL9ZJ'
NEWS_API_KEY = 'cfaa3ed3cc2443a2b5a6913126e1ebd4'
MY_EMAIL = 'std122021@gmail.com'
PASSWORD = "rqyvxrgfnqtuyoyx"
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_url = 'https://www.alphavantage.co/query'
stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
# https://www.alphavantage.co/query?'function'='TIME_SERIES_DAILY_ADJUSTED'&'symbol'='TSLA'&'apikey'='6JHQ82EWFZIXL9ZJ'
response = requests.get(stock_url, params=stock_parameters)
response.raise_for_status()
data = response.json()
# print(data)
last_stock_price = []
last_stock_price=[value["4. close"] for (key,value) in data["Time Series (Daily)"].items()]
# print(last_stock_price)
# for date in data["Time Series (Daily)"]:
#     last_stock_price.append(date["4. close"])
yesterday_price = float(last_stock_price[0])
day_before_yesterday = float(last_stock_price[1])
# print(yesterday_price,day_before_yesterday)
percentage = round(
    ((yesterday_price-day_before_yesterday)/day_before_yesterday)*100, 2)
print(percentage)
# percentage=8.0
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
is_increase_descrease = False
if (percentage >= 5.0):
    message = str(percentage) + ' %🔺'
    is_increase_descrease = True
elif (percentage <= -5.0):
    message = str(percentage) +' %🔻'
    is_increase_descrease = True
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
if is_increase_descrease:
    now = dt.datetime.now()
    news_parameters = {
        'q': COMPANY_NAME,
        'from': 'yesterday',
        'sortBy': 'popularity',
        'api_key': NEWS_API_KEY
    }
    news_url = 'https://newsapi.org/v2/everything?q=Tesla%20Inc&from=yesterday&sortBy=popularity&apiKey=cfaa3ed3cc2443a2b5a6913126e1ebd4'
    response = requests.get(news_url, params=news_parameters)
    response.raise_for_status()
    data = response.json()['articles'][:3]
    messages = []
    for news in data:
        messages.append({
            'Headline': news['title'],
            'Brief': news['description']
        })
    # print(messages)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
      
            # print(news['title'])
            # print(news['description'])
        # connection.send_message(from_addr=MY_EMAIL, to_addrs='ranapratik1612@gmail.com',
        #                         msg=f"}")
        # connection.sendmail(from_addr=MY_EMAIL,to_addrs='ranapratik1612@gmail.com',msg=f"Subject:TSLA:{message}\n\n'Headline':{messages[0]['Headline']}\n'Brief':{messages[0]['Brief']}\n'Headline':{messages[1]['Headline']}\n'Brief':{messages[1]['Brief']}\n'Headline':{messages[2]['Headline']}\n'Brief':{messages[2]['Brief']}")
        # message=MIMEText(message)
        # msg=MIMEText(f"Subject:{message}\n\nHeadline:{messages[0]['Headline']}\n\nBrief:{messages[0]['Brief']}\n\nHeadline:{messages[1]['Headline']}\n\nBrief:{messages[1]['Brief']}\n\nHeadline:{messages[2]['Headline']}\n\nBrief:{messages[2]['Brief']}")
        msg=f"Headline:{messages[0]['Headline']}\n\nBrief:{messages[0]['Brief']}\n\nHeadline:{messages[1]['Headline']}\n\nBrief:{messages[1]['Brief']}\n\nHeadline:{messages[2]['Headline']}\n\nBrief:{messages[2]['Brief']}"
        connection.sendmail(from_addr=MY_EMAIL,to_addrs='ranapratik1612@gmail.com',msg=f"Subject:TESLA STOCK PERCETAGE {message}\n\n{msg}".encode('utf-8'))