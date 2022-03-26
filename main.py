# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
# for i in range(len(data)):
#     data[i] = data[i].strip()
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # for row in data:
#     #     print(row)
#     temperatures = []
#     first_line = True
#     for row in data:
#         if not first_line:
#             temperatures.append(int(row[1]))
#         first_line = False
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# # Get Data Columns
# temp_series = data.temp
# temp_list = temp_series.to_list()
# print(temp_list)

# # Let's calculate the average temperature
# # average_temp = sum(temp_list) / len(temp_list)
# # A better way
# average_temp = temp_series.mean()
# print(average_temp)


# # The maximum value
# max_temp = temp_series.max()
# print(max_temp)

# # Get  Data Rows
# print(data[data.day == "Monday"])
# # Get the row of data with the maximum temperature
# print(data[data.temp == max_temp])
# # Convert Monday's temperature in Fahrenheit
# monday_dataframe = data[data.day == "Monday"]
# monday_temp = monday_dataframe.temp
# print(monday_temp)
# monday_temp_fahrenheint = monday_temp * (9/5) + 32
# print(monday_temp_fahrenheint)

# # Create a DataFrame from scracth
# data_dict_scratch = {
#   "students": ["Amy", "James", "Angela"],
#   "scores" : [76, 56, 65]
# }

# data_scratch = pandas.DataFrame(data_dict_scratch)
# print(data_scratch)
# #data_scratch.to_csv("data_from_scratch.csv")

# Working with the Central Park Squirrel Census Data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"]
colors_series = (colors.value_counts())
print(colors_series)
# colors_series.to_csv("number_of_squirrels_per_color.csv")
# # We modify the first line of the csv file after that
# with open("number_of_squirrels_per_color.csv") as file:
#   lines = file.readlines()
# lines[0] = "Primary Fur Color, Count\n"
# with open("number_of_squirrels_per_color.csv", "w") as file:
#   file.writelines(lines)

# Another way
colors_series.to_csv("number_of_squirrels_per_color.csv", header=False)
# Now We add our header
with open("number_of_squirrels_per_color.csv") as file:
  lines = file.readlines()
with open("number_of_squirrels_per_color.csv", "w") as file:
  file.write("Primary Fur Color,Count\n")
  file.writelines(lines)
  

new_data = pandas.read_csv("number_of_squirrels_per_color.csv")
print(new_data)