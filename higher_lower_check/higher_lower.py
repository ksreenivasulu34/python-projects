import art
import data
import random

print(art.logo)
data_length = len(data.data)

continue_game = True
game_points = 0

while continue_game:
    #compare A data
    compare_a = random.randint(0, data_length-1)
    name = data.data[compare_a]["name"]
    proffession = data.data[compare_a]["description"]
    country = data.data[compare_a]["country"]
    compare_a_follwers = data.data[compare_a]["follower_count"]
    print(f"Compare A: { name }, { proffession }, { country }.")

    #Logo Print of Vs
    print(art.vs)

    #Against B data 
    against_a = random.randint(0, data_length-1)
    against_name = data.data[against_a]["name"]
    against_proffession = data.data[against_a]["description"]
    against_country = data.data[against_a]["country"]
    against_follwers = data.data[against_a]["follower_count"]
    print(f"Against B: { against_name }, { against_proffession },{ against_country }.")

    answer_is = ""
    if compare_a_follwers > against_follwers:
        print("A has more followers!")
        answer_is = "A"
    else:
        print("B has more followers!") 
        answer_is = "B"


    who_has_more = input("Who has more followers? 'A' or 'B': ")
    if who_has_more == answer_is:
        game_points += 1 
        print(f"You are right! Current score is: {game_points}\n")
    else:
        continue_game = False
        print("\n" * 20)
        print(f"Sorry, Thats wrong! Final score is: {game_points}")
