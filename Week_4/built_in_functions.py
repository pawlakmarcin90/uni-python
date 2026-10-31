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