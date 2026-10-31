
"""
# This is a simple for loop that will display a specified number of mountains.

mountains = int(input("How many mountains should I display?\n"))

for i in range(mountains):
    print("    ^")
    print("   /\\")
    print("  /  \\")
    print(" / ^  \\")
    print("/   ^ \\")
    
"""
# Example of using a range() funcion
"""
steps = int(input("How far are we from the target?\n"))

for i in range(steps, 0, -1):
    print(f"{i} steps remaining")
print("Target achieved!")

"""

# Adjusting the brightness level using a range() function
"""
brightness = int(input("What level of brightness is required?\n"))

for i in range(2, brightness +2, 2):
    print(f"Brightness level: {'*' * i}")
"""

# Representing using indexes and iterating through a string as a list of characters
"""
word = input("What word do you see?\n")

for i in range(len(word)):
    print(f"index {i}: {word[i]}")

"""

""" for count in range(0, 3, 1):
        for number in range(0, 10, 1):
            print(f"{number} |", end="")
            print() 
"""
"""
# Reversing a string using slicing and a for loop
phrase = input("What phrase do you want to see in reverse?\n")
 for letter in phrase[::-1]:
    print(letter, end="") """
""" 
# Reversing a string using a for loop and indexes

for i in range(len(phrase)):
    print(phrase[len(phrase) - 1 - i], end="") """
