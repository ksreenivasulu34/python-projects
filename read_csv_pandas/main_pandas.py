import pandas

data = pandas.read_csv("./csv_data_pandas/weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
#print(data_dict)

temp_data = data["temp"].to_list()
print(temp_data)



avg = sum(temp_data) / len(temp_data)
#print(avg)

print(data["temp"].max())
    