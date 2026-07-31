import random

names = ["Android", "ios", "Flutter", "React", "AI", "Python"]

names_dict = { name: random.randint(1, 100) for name in names}

passed_items = {key : value for key,value in names_dict.items() if value > 60 }
print(names_dict)
print(passed_items)