import pandas as pd
import datetime as dt
from os import listdir
from os.path import isfile, join
from random import choice
import smtplib


PLACEHOLDER = "[NAME]"
STARTING_FIRST_LINE = "Dear [NAME],\n"
MY_EMAIL = "santiclo.gohan@gmail.com"
MY_PASSWORD = "testingground789"
EMAIL_SERVER_ADDRESS = "smtp.gmail.com"


# 1. Update the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
day_number = now.day
month_number = now.month

party_person_object = birthday_data.loc[(birthday_data.month == month_number) & (birthday_data.day == day_number)]
name_to_letter = party_person_object["name"].values[0]

# 2. Check if today matches a birthday in the birthdays.csv
if name_to_letter:
    # 3. If step 2 is true, pick a random letter from letter templates and replace
    # the [NAME] with the person's actual name from birthdays.csv
    # this line lists the files in a directory
    only_files = [item for item in listdir("letter_templates/") if isfile(join("letter_templates/", item))]
    template_birthday_letter = choice(only_files)
    print(template_birthday_letter)
    print(type(template_birthday_letter))

    with open(f"letter_templates/{template_birthday_letter}") as birthday_letter_file:
        file_data = birthday_letter_file.readlines()

    print(file_data)

    new_first_line = file_data[0].replace(PLACEHOLDER, name_to_letter)
    file_data[0] = new_first_line

    message = f"Subject: Happy birthday {name_to_letter}\n\n"
    for line in file_data:
        message += line

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(EMAIL_SERVER_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="santiclo.gohan@yahoo.com", msg=message)
