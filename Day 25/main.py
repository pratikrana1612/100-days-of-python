# with open("Day 25/weather_data.csv") as file:
#     data=file.readlines()
# print(data)

# import csv

# with open("Day 25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures=[]
#     for row in data:
#             if(row[1] != 'temp'):
#                 temperatures.append(int(row[1]))
#         # print(row)
#     print(temperatures)


import pandas

# data = pandas.read_csv("Day 25/weather_data.csv")
# print(type(data))
# print(data)
# print(data['temp'])
# print(type(data['temp']))
# dict=data.to_dict()
# temp_list=data['temp'].to_list()
# sum_list=sum(temp_list)
# print(sum_list/len(temp_list))
# print(dict)
# print(data['temp'].mean())
# print(data['temp'].max())

# getting columns
# print(data['condition'])
# print(data.condition)

# getting rows
# print(data[data.day=='Monday'])
# print(data[data['day']=='Monday'])
# max=data['temp'].max()
# print(data[data.temp==data.temp.max()])
# monday=data[data.day=='Monday']
# print((int(monday.temp)*(9/5))+32)
# data_dict={
#     "students":["Pratik","kartik","Rohan"],
#     "scores":[2,4,5]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = 0
cinnamon_squirrel = 0
black_sqirrel = 0

# print(data['Primary Fur Color'])
gray_rows = data[data["Primary Fur Color"] == "Gray"]
gray_squirrel = len(gray_rows["Primary Fur Color"].to_list())
cinnamon_row = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrel = len(cinnamon_row["Primary Fur Color"].to_list())
black_row = data[data["Primary Fur Color"] == "Black"]
black_sqirrel = len(black_row["Primary Fur Color"].to_list())
# print(cinnamon_squirrel)
# print(black_sqirrel)

# print(data[data['Primary Fur Color']=="Gray"]['Primary Fur Color'])
squirrel_colors = {
    "Fur color":["gray","red","black"],
    "Count":[gray_squirrel,cinnamon_squirrel,black_sqirrel]
}
print(squirrel_colors)
squirrel_colors_data = pandas.DataFrame(squirrel_colors)
squirrel_colors_data.to_csv("squirrel_count")
