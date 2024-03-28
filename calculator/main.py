from art import logo
# calculater functions( addition, subtraction, multiplication, division )
def subtraction(a, b):
    return a - b


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


# operation dictionary
operations = {
    "-": subtraction,
    "+": addition,
    "*": multiplication,
    "/": division
}

print(logo)

#Calculation Function


def calculator():
    # User first number
    first_number = float(input("what is the first number? \n"))

    continue_calculating = True
    while continue_calculating:
        # For loop to go through the operations one by one
        for i in operations:
            print(i)
        # Operation_input
        operation = input("Please pick an operation \n")

        # Second number
        second_number = float(input("What is your second number? \n"))
        calculate_function = operations[operation]
        answer = calculate_function(first_number, second_number)
        answer_round = round(answer, 3)

        print(f"The answer is : {answer_round}")

        # User operation_input on an operation and a final answer that rounded up

        yes_no = input(f"Type 'y' to continue calculating with {answer_round}, or type 'n' to start a new calculation: ")
        if yes_no == "y":
            first_number = answer_round
            continue_calculating = True

        else:
            continue_calculating = False
            calculator()


calculator()
