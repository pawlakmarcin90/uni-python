
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

