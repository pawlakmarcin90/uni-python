"""
# Display a simple message
print("Program started!")

# Read users input
character = input("Enter a standard character: ")

# Check if the input is a single character
if len(character) != 1:
    print("Error: Please enter a single character.")
else:
    # Display the ASCII value of the character
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is: {ascii_value}")
print("Program ended!")
 """

""" # Creating a funtion using define function
def ascii_code_placeholder(char):
    if len(char) != 1:
        print("Error, please enter a single character.\n")
    else:
        ascii_order = ord(char)
        print(f"The ASCII value of '{char}' is: {ascii_order}\n")

# Asking user for inout and calling the function
char = input("Enter a single standard character: ")
ascii_code_placeholder(char)
 """
# A simple program to get the ASCII value of a number input by the user
""" 
ascii_value = abs(int(input("Enter a number to get its ASCII value: ")))
if ascii_value < 0 or ascii_value > 127:
    print("Error: Please enter a number between 0 and 127.")
else:
    print(f"The ASCII code representation for {ascii_value} is '{chr(ascii_value)}'.")
 """

