# Using if statement
book_type = input("What type of book is this?\n")
if book_type == "adventure":
    print("\nI like adventure books!")
print("\nFinished reading book!")

# Expanding if statement to include an else
activity = input("Please enter the activity to be performed.\n")
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")
print("\nActivity completed!")

direction = input("Towards which direction should I go (up, down, left or right)?\n")
if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in an downward direction!")
elif direction == "left":
    print("I am moving in a leftward direction!")
elif direction == "right":
    print("I am moving in a rightward direction!")
else:
    print("Direction unknown!")

# Demonstrating the use of modulo operator
number = int(input("Please enter a whole number.\n"))
if number % 2 == 0:
    print(f"The number {number} is even number")
else:
    print(f"The number {number} is an odd number")

# Comparison operator finding the smallest number

num_1 = input("Please enter the first number.\n")
print(num_1)
num_2 = input("Please enter the second number.\n")
print(num_2)

if num_1 == num_2:
    print("Both are equal!")
elif num_1 < num_2:
    print("The first number is the smallest.")
else:
    print("The second number is the smallest.")
