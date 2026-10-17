#Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}.")

eye = input("Enter a single character for the eye of the robot.\n")
print("##########")
print(f"# {eye}    {eye} #")
print("#   __   #")
print("##########")
print("    ##")
print("##########     #")
print("#   ##   #    #")
print("#   ##   # ###")
print(" #  ##    ")
print("##########")
print("   #  #  ")
print("  ##  ##  ")
print("   #  #  ")
print(" ###  ### ")

# BMI Calculator
print("What is your name?")
name_bmi = input()
print("How old are you (in years)?")
age_bmi = float(input())
print("How tall are you(in meters)?")
height = float(input())
print("What is your weight (in kilograms)")
weight = float(input())

bmi = weight / height ** 2
bmi_round = round(bmi, 2)

print(f"{name_bmi}, your BMI is {bmi_round}")

# Simple game simulation
print("Enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())
print("\nHealth has been set.")

for heart in range(lives):
    print("♥", end = ' ')
print()
for shield in range(energy):
    print("♦", end=' ')
print()
for armor in range(shield):
    print("♦", end=' ')
print()