import clear
from art import logo

print(logo)

bid_dict = {}

still_bidding = True
while still_bidding:

    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? "))

    bid_dict[name] = bid_price

    other_users = input("Are there other users who want to bid? Type 'yes' or 'no'. ")

    if other_users == "yes":
        clear()

    elif other_users == "no":
        print(f"The winner is {max(bid_dict, key=bid_dict.get), max(bid_dict.values())}")
        still_bidding = False