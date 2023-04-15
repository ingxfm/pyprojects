import smtplib
import os

MY_EMAIL = os.environ['FROM']
MY_PASSWORD = os.environ['FROM_PASS']
EMAIL_SERVER_ADDRESS = 'smtp.gmail.com'
TO_EMAIL = os.environ['TO']


class EmailMessage:

    def __init__(self, current_price, preset_price):
        self.message: str = f'The current price {current_price}, is equal or lower than the' \
                  f'preset price {preset_price}. Opportunity!'

    def send_message(self, lower_than_preset):
        if lower_than_preset:
            with smtplib.SMTP(EMAIL_SERVER_ADDRESS) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,
                                 password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=TO_EMAIL,
                    msg=self.message,
                )
