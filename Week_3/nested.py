""" 
for count in range(0, 2, 1):
    for number in range(0, 10, 1):
        print(f"{number} |", end = "")
    print()
     """
# A simple nested loop example showing columns and rows of smiley faces
"""
rows = int(input("How many rows would you like to display?\n"))
columns = int(input("How many columns would you like to display?\n"))

for r in range(rows):
    for c in range(columns):
        print(":-) ", end="")
    print()
 """
# Additional example using operators in a single loop
""" 
for _ in range(rows):
    print(":-) " * columns)
 """
# Additional example showing a decreasing number of smiley faces in each row
""" 
for r in range(rows, 0, -1):
    print(":-)" * r)
 """

# A code showing nested loop and character counting with marker comparison
""" 
sequence = input("Enter a sequence of characters separated with dashes and two markers (X----X):")
marker = input("Enter your marker exactly as shown above (X):")
count = 0
for i in range(len(sequence)):
    if sequence[i] == marker:
        for j in range(i + 1, len(sequence)):
            if sequence[j] == "-":
                count += 1
            elif sequence[j] == marker:
                break
    break

print(f"{count}")
 """