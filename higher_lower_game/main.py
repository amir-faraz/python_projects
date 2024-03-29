from game_data import data
from art import logo
import random

print(logo)
score = 0

random_data_A = random.choice(data)
random_data_B = random.choice(data)

winner_exist = False
playing = True
while playing:

    if not winner_exist:
        random_data_A = random.choice(data)
        random_data_B = random.choice(data)
    else:
        random_data_B = random.choice(data)

    print(f"Compare A: {random_data_A['name']} , {random_data_A['description']} from {random_data_A['country']}")
    print(f"Compare B: {random_data_B['name']} , {random_data_B['description']} from {random_data_B['country']}")

    answer_question = input("Who has more followers? Type A or B \n").lower()

    if (answer_question == "a") and (random_data_A['follower_count'] > random_data_B['follower_count']):
        print("The answer is correct and A is a winner")
        winner_exist = True
        random_data_A = random_data_B
        score += 1
        print (f"Your score is {score}")

    elif (answer_question == "b") and (random_data_B['follower_count'] > random_data_A['follower_count']):
        print("The answer is correct and B is a winner")
        winner_exist = True
        random_data_A = random_data_B
        score += 1
        print(f"Your score is {score}")

    elif random_data_B['follower_count'] == random_data_A['follower_count']:
        print("It's a  tie")

    else:
        print("The answer is wrong")
        print(f"Your score is {score}")
        playing = False
