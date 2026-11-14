""" 
lists = [23, 54, 5, 32]
list2 = []

list2 += lists[:-1]
def cmp(list1, list2):
    if list1 == list2:
        return 0
    elif list1 < list2:
        return -1
    else:
        return 1

lists.reverse()

print(lists)
print(lists.count(5))
lists.append(100)
print(lists)

compare = cmp(lists, list2)
print(compare)

 """

def directions():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")

    return steps
def run_task1():
    print(directions())

if __name__ == "__main__":
    run_task1()

fruits = ["apple", "banana", "cherry", "date"]

for index in range(len(fruits)):
    fruit = fruits[index]
    print(f"{fruit} is at index {index}")