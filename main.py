#   Approach 1
# with open("./weather_data.csv", mode="r") as weather_data:
#     data_list = weather_data.readlines()
#     print(data_list)

#   Approach 2
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             a = int(row[1])
#             temperatures.append(a)
#     print(temperatures)

#   Approach 3

                    # SERIES == ROW
                    # SERIES == ROW
                    # SERIES == ROW

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))

# DATA TO DICTIONARY
# data_dict = data.to_dict()
# print(data_dict)

# DATA TO LIST
data_list = data["temp"].to_list()
# print(data_list)

# Approach 1
# sum = 0
# for data in data_list:
#     sum += data
# avg = sum / 7
# print(f"Sum {sum} Avg {avg}")

# Approach 2
# avg = sum(data_list) / len(data_list)
# print(avg)

# print(data[data.day == "Monday"])

# print(data["temp"].max())

# Another way to call series
# print(data.condition)

# Pull a row with max temperature
# maximum = data["temp"].max()
# print(data[data.temp == maximum])

# 1
# monday = data[data.day == "Monday"]
# print(monday.condition)

# Get Monday temp and convert it into Fahrenheit
# mon = data[data.day == "Monday"]
# monday_temp = mon.temp * 9/5 + 32
# print(monday_temp)

# Creating a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# Data to CSV File
data_frame.to_csv("new_csv.csv")



