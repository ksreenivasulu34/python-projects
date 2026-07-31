numbers = [1, 2, 3]
new_numbers = [item + 2  for item in numbers]
print(new_numbers)

names = ["Android", "ios", "Flutter", "React", "AI", "Python"]

filtered_names = [name.upper() for name in names if len(name) > 5 ]
print(filtered_names)