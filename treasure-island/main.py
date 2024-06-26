#Treasure Island ASCII Art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Welcome Message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Choose your path(Left / Right)
path = input("Which path you choose? left or right \n")

#Conditions for the path
if path == "left":
    swim_wait = input("Swim or Wait? \n").lower()
    if swim_wait == "wait":
        door_input = input("Which door do you prefer? Red, Blue or Yellow ".lower())
        if door_input == "red":
            print("Burned by fire, GAME OVER")
        elif door_input == "blue":
            print("Eaten by beasts, GAME OVER")
        elif door_input == "yellow":
            print("You Win")
        else:
            print("Game Over")

    elif swim_wait == "swim":
        print("Attacked by trout, Game Over")

elif path == "right":
    print("Fall into a hole, Game over")

