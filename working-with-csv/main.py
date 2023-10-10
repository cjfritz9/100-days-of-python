# import csv
import pandas

# with open("weather_data.csv") as file_data:
#   data = csv.reader(file_data)

#   temperatures = []
#   for row in data:
#     if row[1] != 'temp':
#       temperatures.append(int(row[1]))
#   print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# mean_temp = data["temp"].max()

# print(mean_temp)

# max = data['temp'].max()

# print(data[data["temp"] == max])

# monday_temp = data[data['day'] == 'Monday']['temp']
# monday_temp_f = monday_temp * 1.8 + 32

# print(monday_temp_f)

data = pandas.read_csv("cp_squirrel_data.csv")

squirrel_counts = []

cinnamon_squirrels = data[data["Primary Fur Color"] == 'Cinnamon']["Primary Fur Color"].to_list()
gray_squirrels = data[data["Primary Fur Color"] == 'Gray']["Primary Fur Color"].to_list()
black_squirrels = data[data["Primary Fur Color"] == 'Black']["Primary Fur Color"].to_list()

cinn_squirrels_count = len(cinnamon_squirrels)
gray_squirrels_count = len(gray_squirrels)
black_squirrels_count = len(black_squirrels)

data_dict = pandas.DataFrame({
  "Fur Color": ["Cinnamon", "Gray", "Black"],
  "Count": [cinn_squirrels_count, gray_squirrels_count, black_squirrels_count]
})

data_dict.to_csv("squirrel_counts.csv")

squirrel_data = pandas.read_csv("squirrel_counts.csv")

print(squirrel_data)
