"""
# A function presenting a if and return
 
def identify():
    identify = input("What do you see?\n")

    if identify == "a large boulder":
        print("It is time to runnnn!!!!")
    else:
        print("We will be fine.")

    return print(f"You hear a sound of a {identify}")

identify()
 """
""" 
# Nested functions
def display_box(name):
    message = f"* Hello, {name} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))

def greet_user():
    name = input("Please enter your name\n")
    display_box(name)

greet_user()
 """
"""
# Excersise of a multiple function usage - ladder display

def display_ladder(steps):
    for step in range(1, steps + 1):
        print("|__|")
    print("|  |\n")

def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)

create_ladder()
 """
""" 
# A task creating a function that will sum weights

def sum_weights(character_weight, inventory_weight):
    total_weight = round(character_weight + inventory_weight, 2)
    return total_weight

def calc_avg_weight(character_weight, inventory_weight):
    avg_weight = round(sum_weights(character_weight, inventory_weight) / 2, 2)
    return avg_weight
def run():
    character_weight = float(input("What is your character's weight?\n"))
    inventory_weight = float(input("What is your inventory's weight?\n"))
    action = input("What value do you want to know (sum or average)?\n")
    if action == "sum":
        print(sum_weights(character_weight, inventory_weight))
    elif action == "average":
        print(calc_avg_weight(character_weight, inventory_weight))
run()
 """
""" 
# Creating a calculator function with a loop and a menu


    

def operation(selection):
       

    num1 = float(input("Enter first number:\n"))
    num2 = float(input("Enter second number:\n"))
    if selection == "1":
        addition_sum = float(num1 + num2)
        return addition_sum
    elif selection == "2":
        subtraction_sum = float(num1 - num2)
        return subtraction_sum
    elif selection == "3":
        multiplication_sum = float(num1 * num2)
        return multiplication_sum
    elif selection == "4":
        division_sum = float(num1 / num2)
        return division_sum
    elif selection == "5":
        print("\nProgram exit, thank you!\n")
        return 0


def menu():

    print("1. Add\n")
    print("2. Subtract\n")
    print("3. Multiply\n")
    print("4. Divide\n")
    print("5. Exit\n")
    selection = input("\nSelect an operation:\n")
    
    return selection

def display_box(message):
    message = f"|*| The result is {message} |*|"
    print("*" * len(message))
    print(message)
    print("*" * len(message))

while True:
    choice = menu()
    if choice == "5":
        print("\nExiting the program. Goodbye!\n")
        break
    elif choice in ["1", "2", "3", "4"]:
        result = operation(choice)
        print(display_box(result))
 """

def in_box(word):
    message = f"* {word} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))
def lower(word):
    print(word.lower())
def upper(word):
    print(word.upper())
def mirror(word):
    for letter in word[::-1]:
        print(letter, end="")
def repeat(word):
    times = int(input("How many times do you want the message to be repeated?\n: "))
    while times > 0:
        upper(word)
        times -= 1
        lower(word)
        times -= 1
