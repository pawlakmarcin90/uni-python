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
# Excersise of a multiple function usage - ladder display

def display_ladder(steps):
    for step in range(1, steps + 1):
        print("|__|")
    print("|  |\n")

def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)

create_ladder()