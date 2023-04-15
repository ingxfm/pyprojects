# # TODO: my way
# # with open("./weather_data.csv") as data_file:
# #     lines_list = data_file.readlines()
# #
# # print(lines_list)
# #
# # for line in lines_list:
# #     stripped_line = line.strip("\n")
# #     separated_word = stripped_line.split(",")
# #     print(separated_word)
#
# # TODO using import csv
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data_frame = pandas.read_csv("weather_data.csv", index_col=False)
# # print(type(data_frame))
# # print(data_frame["temp"])
# #
# # data_dict = data_frame.to_dict()
# # print(data_dict)
# #
# # temp_list = data_frame["temp"].to_list()
# # print(temp_list)
# #
# # average_temp = sum(temp_list) / len(temp_list)
# # print(f"{average_temp:.2f}")
# #
# # average_temp_pandas = data_frame["temp"].mean()
# # print(f"{average_temp_pandas:.2f}")
# #
# max_value_pandas = data_frame["temp"].max()
# # print(f"{max_value_pandas}")
# #
# # # Get data from columns
# # print(data_frame["condition"])
# #
# # # Get data without using brackets
# # print(data_frame.condition)
# # # Pandas converts the headings into attributes
#
# # Get rows
# # print(data_frame[data_frame.day == "Monday"])
#
# # Get day of highest temperature
# print(f"The day of the maximum temperature is {data_frame[data_frame.temp == max_value_pandas].day}.\n"
#       f"And the temperature is {data_frame[data_frame.temp == max_value_pandas].temp}.")
# # when a particular condition is equal to a particular value, the row is selected instead.
#
# # get Monday's temperature in Fahrenheit
# monday_temp_celsius = data_frame[data_frame.day == "Monday"].temp
# print(f"In celsius is {monday_temp_celsius}.")
# monday_temp_fahrenheit = monday_temp_celsius * 1.8 + 32
# print(f"In Fahrenheit is {monday_temp_fahrenheit}.")
#
#
# # Create  a data frame from scratch
# data_dict_1 = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# print(data_dict_1)
# datas = pandas.DataFrame(data_dict_1)
# datas.to_csv("new_data.csv")

# import pandas as pd
#
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# new_data_file = data["Primary Fur Color"].value_counts()
#
# new_data_file.to_csv("fur_color_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("mentor_fur_color.csv")
