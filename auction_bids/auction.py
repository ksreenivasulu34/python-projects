import art

print(art.logo)

print("Welcome to Auction!")

bidding_dictionary = {}

anyone_else = True



def anybody_else():
    name = input("Please enter name: ")

    value = input("Enter Amount: ")

    bidding_dictionary[name] = value

    anyone_else = input("Any one else to bid, Enter 'Yes' or 'No'?").lower()

    if anyone_else == "yes":
        print("\n" * 20)
        anybody_else()
    else:
        find_highest_bid()


def find_highest_bid():
    highest = 0
    for bid in bidding_dictionary:
        highest = bidding_dictionary[bid]
        if highest < bidding_dictionary[bid]:
            highest = bidding_dictionary[bid]
    
    print(f"Highest bid is { bid } with a value of {highest}")
    
    max_value = max(bidding_dictionary)
    print(max_value)
    
anybody_else()


