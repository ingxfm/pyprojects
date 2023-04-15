#  built-ins
import smtplib
import datetime as dt
from time import sleep

# 3rd parties
import requests


# location and mail
LATITUDE = -38.606836
LONGITUDE = -157.195061
MY_EMAIL = "dummy@gmail.com"
MY_PASSWORD = ""

def is_iss_near_me():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()
    print(data_iss)

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)

    lat_compare = iss_latitude - LATITUDE
    lng_compare = iss_longitude - LONGITUDE

    iss_position = (iss_latitude, iss_longitude)
    print(iss_position)
    print(lat_compare)
    print(lng_compare)

    if lat_compare < 5 and lat_compare > -5 and lng_compare < 5 and lng_compare > -5:
        return True


def is_it_dark():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = dt.datetime.now().hour

    print(time_now)

    if time_now < sunrise or time_now > sunset:
        return True


while 1:
    if is_iss_near_me() and is_it_dark():
        print("GO OUT! The ISS is visible in the night sky.")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= "Subject: GET OUT\n\nThe ISS is visible in the sky."
        )
    else:
        print("stay quiet")

    sleep(60)
