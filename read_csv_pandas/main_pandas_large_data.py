import pandas

data = pandas.read_csv("./csv_data_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "count" : [grey_color_count, cinnamon_color_count, black_color_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./csv_data_pandas/new_data.csv")

#using list and for loop
# colors_list = data["Primary Fur Color"].to_list()
# grey_color_list = []
# cinnamon_color_list = []
# black_color_lsit = []
# for color in colors_list:
#     if color == "Gray":
#         grey_color_list.append(color)
#     elif color == "Cinnamon": 
#         cinnamon_color_list.append(color)
#     elif color == "Black":
#         black_color_lsit.append(color)
        
# data_dict = {
#     "Fur Color" : [grey_color_list[0], cinnamon_color_list[0], black_color_lsit[0]],
#     "count" : [int(len(grey_color_list)), int(len(cinnamon_color_list)), int(len(black_color_lsit))]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")



        