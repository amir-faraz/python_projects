import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty: Easy / Hard? \n").lower()

random_number = random.randint(1, 101)



attempts = {
    "easy": 10,
    "hard": 5
}

choose_number = attempts[difficulty]

playing = True
while playing:

        print(f"You have {choose_number} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print("You Win")
            playing = False
        else:

            if guess > random_number:
                print("Too high")
                choose_number -= 1

            elif guess < random_number:
                print("Too low")
                choose_number -= 1

            if choose_number == 0:
                playing = False
                print(f"The number was: {random_number}")
                print("Unfortunately you lose")
    #
    # if difficulty == "easy":
    #     print(f"You have {attempts_easy} attempts remaining to guess the number")
    #     guess = int(input("Make a guess: "))
    #
    #     if guess == random_number:
    #         print("You Win")
    #         playing = False
    #     else:
    #
    #         if guess > random_number:
    #             print("Too high")
    #             attempts_easy -= 1
    #
    #         elif guess < random_number:
    #             print("Too low")
    #             attempts_easy -= 1
    #
    #         if attempts_easy == 0:
    #             playing = False
    #             print("Unfortunately you lose")