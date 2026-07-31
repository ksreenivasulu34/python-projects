import csv

with open("./list_comprehension/nato_phonetic_alphabet.csv") as file:
    data = csv.reader(file)
    
    items_dict = { key:value for key,value in data if key != "letter"}
    print(items_dict)
    
user_input = input("Enter your word:").upper()
print(user_input)

output = [items_dict[letter] for letter in user_input]
print(output)
    