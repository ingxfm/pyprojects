#  On every year that is evenly divisible by 4.
#  except those that are divisible by 100
#  unless the year is also evenly divisible by 400
import csv

with open('leap_years.csv') as csv_file:
    csv = csv.reader(csv_file, delimiter=',')
    leap_years: list = []
    for row in csv:
        leap_years.append(int(row[0]))

check_if_leap_year = True
while check_if_leap_year:
    # year: int = int(input('What year do you want to check is a leap year? '))
    leap_year: bool = False
    leap_year_answer: list = []
    for year in leap_years:
        if year % 4 == 0:
            leap_year = True
            if year % 400 != 0:
                if year % 100 == 0:
                    leap_year = False
            else:
                leap_year = True

        if leap_year:
            leap_year_answer.append('Leap year.')
        else:
            leap_year_answer.append('Not a leap year')

    print(leap_year_answer)

    choice = input('Do you want to continue checking if the year is a leap year? Type "y" for Yes: ').lower()
    if choice != 'y':
        break
