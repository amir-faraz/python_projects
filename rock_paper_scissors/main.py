import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = ["rock", "paper", "scissors"]

#user_choice(rock/paper or scissors)
user_choice = int(input("What is your choice? 0 for rock, 1 for paper or  2 for scissors \n"))
print(game_list[user_choice])

#computer_choice(random)
computer_choice = random.randint(0,2)
print(game_list[computer_choice])

#conditions
if user_choice == computer_choice:
    print("It's a Draw!")
elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
    print(f"You Win! {game_list[user_choice]} beats {game_list[computer_choice]}.")
else:
    print(f"You Lose! {game_list[computer_choice]} beats {game_list[user_choice]}.")