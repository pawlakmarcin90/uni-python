

#%%
file = open("C:\\Users\\pawla\\Uni\\Python\\Week_6\\disneyland_reviews.csv" , "r")
data = file.read()
print(data[:500])
# %%
from csv import reader
file = open("C:\\Users\\pawla\\Uni\\Python\\Week_6\\disneyland_reviews.csv" , "r")
csv_reader = reader(file)
for row in csv_reader:
    print(row)
    for column in row:
        print(column)

# %%
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())
# %%
import csv

with open("C:\\Users\\pawla\\Uni\\Python\\Week_6\\disneyland_reviews.csv") as file:
    csv_reader = csv.reader(file)
    for values in csv_reader:
        print(values)
# %%
import csv

with open("C:\\Users\\pawla\\Uni\\Python\\Week_6\\disneyland_reviews.csv") as file:
    print(file.read())

# %%
file = open("test_multiple.txt", "w")
file.write("File Handling in Python\n")
file.writelines(["Java\n", "Python\n", ".NET\n"])
file.close()
# %%
with open("test_multiple.txt", "w") as file:
    file.write("Changed Header\n\n")
    file.writelines(["New\n", "Another\n", "Yet another\n\n\n"])

# %%
with open("test_multiple.txt", "a") as file:
    file.write("\n\n\nAppend Header\n\n")
# %%
import csv
records = [
    ["ID", "Name", "Marks"],
    [1, "Amal", 90],
    [2, "Bimal", 80],
    [3, "Chitra", 70],
    [4, "Somero", 55],
    [5, "Anna", 62],
    [6, "Ariel", 76]

]
with open("students.csv", "w", newline = "") as file:
    data = csv.writer(file)
    data.writerows(records)

print("Student csv file created!")
# %%
import csv
with open("students.csv", "r") as file:
    data = csv.reader(file)

    next(data)  # Skip the header row
    for row in data:
        print(row[0], row[1], row[2])
# %%
