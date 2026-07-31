import csv

with open("./csv_data_pandas/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for item in data:
        #print(item)
        if item[1] != "temp":
            temperatures.append(int(item[1]))
    print(temperatures)