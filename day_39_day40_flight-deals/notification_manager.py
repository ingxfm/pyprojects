from twilio.rest import Client
import os

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, departure_airport, departure_city, destination_airport, destination_city, flight_price, flight_dates):
        self.body_sent: str = f"Departure Airport: {departure_airport} in the City: {departure_city}" \
                         f"Destination Airport: {destination_airport} in the City: {destination_city}" \
                         f"Price: {flight_price:.2f}EUR" \
                         f"On dates{flight_dates}"  # include the times

    def send_SMS_Twilio(self):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=self.body_sent,
            from_=os.environ["FROM_NUMBER"],
            to=os.environ["TO_NUMBER"],
        )
# add functionality to send all required messages