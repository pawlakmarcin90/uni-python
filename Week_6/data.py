

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
