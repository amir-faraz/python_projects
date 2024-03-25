#welcoming
print("Welcome to the bill calculator")

#bill input
bill_input = float(input(f"What was a total bill?\n$"))

#tip input
tip_input = float(input("How much do you wanna tip? 10, 12, 15 \n"))

#people split bill
people_split = float(input("How many people split the bill?\n"))

#tip percentage
tip_percentage = bill_input / 100
percentage = tip_percentage * tip_input

#total and round it up to 2 number
total = percentage / people_split
new_total = total.__round__(2)

#bill and the tip
bill_tip = new_total + bill_input

print(f"Each person owes {new_total} tip")
print(f"Your total plus tip is {bill_tip}")
