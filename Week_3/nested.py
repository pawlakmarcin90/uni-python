""" 
for count in range(0, 2, 1):
    for number in range(0, 10, 1):
        print(f"{number} |", end = "")
    print()
     """
# A simple nested loop example showing columns and rows of smiley faces

rows = int(input("How many rows would you like to display?\n"))
columns = int(input("How many columns would you like to display?\n"))
""" 
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
