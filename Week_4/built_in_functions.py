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

