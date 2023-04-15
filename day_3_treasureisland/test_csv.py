import csv

with open('/home/ingxfm/PycharmProjects/day3_treasureisland/leap_years.csv') as csv_file:
    csv = csv.reader(csv_file, delimiter=',')
    leap_years: list = []
    for row in csv:
        leap_years.append(int(row[0]))