import smtplib
my_email = "ranapratik1612@gmail.com"
password = "123456"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs='ranapratik47904@gmail.com',msg="Subject:Hello\n\nThis is the body of the email")
    

