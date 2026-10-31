"""
apples = int(input("How many apples should i Remove?\n"))
removed_apples = 0

while removed_apples < apples:
    removed_apples += 1
    print("Removed apple.")

"""
"""
obstacle_num = int(input("How many obstacles must I avoid?\n"))
obstacle_count = 0

while obstacle_count < obstacle_num:
    print("Avoiding...", end ="")
    obstacle_count += 1
    print(f"...Done {obstacle_count} obstacles avoided.")

"""
"""
battery_percent = int(input("How many bars should be charged?\n"))
battery_status = 0
battery_icon = "█"
while battery_status < battery_percent:
    battery_status += 1
    print(f"Charging... {(battery_icon + ' ') * battery_status}")
print("Battery is fully charged!")

"""
"""
phrase = input("Please enter a phrase:\n")
count = 0

while count < len(phrase):
    count += 1
    print("Hi", end =' ')
"""

