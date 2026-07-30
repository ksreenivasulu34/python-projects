import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
print(random_number)

attempts_remaining = 0
continue_checking = True
level_type = input("Choose a difficulty. Type 'easy' or 'hard':")
if level_type == "easy":
    attempts_remaining = 10
    print(f"You have {attempts_remaining} attempts remaining to guess the number")
else:
    attempts_remaining = 5
    print(f"You have {attempts_remaining} attempts remaining to guess the number")

# guess = int(input("Make a guess: "))

while continue_checking:
    if not attempts_remaining == 0:
        guess = int(input("Make a guess: "))
        if random_number < guess:
            print("Too high!")
            print("Guess again.")
            attempts_remaining -= 1
            print(f"You have {attempts_remaining} attempts remaining to guess the number")
        elif random_number > guess:
            print("Too Low!")
            print("Guess again.")
            attempts_remaining -= 1
            print(f"You have {attempts_remaining} attempts remaining to guess the number")
        else:
            print("You got it right!")
            continue_checking = False
    else:
        continue_checking = False
        print(f"You have lost. You have excedded attempts remaining to guess the number")
    

