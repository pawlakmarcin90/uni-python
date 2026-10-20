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