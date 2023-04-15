import os
import requests
from twilio.rest import Client
import datetime as dt

# get the date of yesterday and the day before yesterday
# from Monday to Friday
today = dt.datetime.today()
yesterday = str((today - dt.timedelta(days=1)).date())
# In the datetime library, Monday to Sunday is 0 to 6.
if today.weekday() == 1:
    day_before_yesterday = str((today - dt.timedelta(days=4)).date())
else:
    day_before_yesterday = str((today - dt.timedelta(days=2)).date())

STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"
LOWER_COMPANY_NAME: str = "tesla"

AV_ENDPOINT: str = "https://www.alphavantage.co/query"
AV_KEY = os.environ["AV_API_KEY"]
AV_PARAMS: dict = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": AV_KEY,
}

NA_END_POINT: str = "https://newsapi.org/v2/everything"
NA_KEY = os.environ["NA_API_KEY"]
NA_PARAMS: dict = {
    "q": LOWER_COMPANY_NAME,
    "from": f"{day_before_yesterday}",
    "sortBy": "publishedAt",
    "apiKey": NA_KEY,
}

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# # STEP 1: Use https://www.alphavantage.co, Alpha Advantage abbreviated as AV
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(AV_ENDPOINT, params=AV_PARAMS)

yesterday_closing_price = float(response.json()["Time Series (Daily)"]["2022-03-14"]["4. close"])
day_before_yesterday_closing_price = float(response.json()["Time Series (Daily)"]["2022-03-11"]["4. close"])

difference = ((yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price) * 100

print(yesterday_closing_price)
print(day_before_yesterday_closing_price)
print(f"{difference:.2f}")


def get_news(na_endpoint, na_parameters):
    # # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    response_na = requests.get(na_endpoint, na_parameters)
    data = response_na.json()["articles"][:3]
    return data


def send_SMS_Twilio(twilio_sid, twilio_parameters, data, difference):
    # # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    data_title = data[0]["title"]
    data_description = data[0]["description"]
    body_sent: str = f"{STOCK} {difference:.2f}%\n" \
                f"Headline: {data_title}" \
                f"Brief: {data_description}"

    client = Client(twilio_sid, twilio_parameters)
    message = client.messages.create(
        body=body_sent,
        from_=os.environ["FROM_NUMBER"],
        to=os.environ["TO_NUMBER"],
    )


if difference > 2:
    news_to_send = get_news(NA_END_POINT, NA_PARAMS)
    send_SMS_Twilio(TWILIO_SID, TWILIO_TOKEN, news_to_send, difference)

elif difference < -2:
    news_to_send = get_news(NA_END_POINT, NA_PARAMS)
    send_SMS_Twilio(TWILIO_SID, TWILIO_TOKEN, news_to_send, difference)
