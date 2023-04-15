import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "santiclo.gohan@gmail.com"
MY_PASSWORD = "testingground789"
EMAIL_SERVER_ADDRESS = "smtp.gmail.com"

now = dt.datetime.now()
today_is = now.weekday()
if today_is == 3:
    with open("quotes.txt") as quote_file:
        quotes_list = quote_file.readlines()
    one_random_quote = choice(quotes_list)
    message = f"Subject: Quote of the day\n\n{one_random_quote}"

    with smtplib.SMTP(EMAIL_SERVER_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="santiclo.gohan@yahoo.com", msg=message)
