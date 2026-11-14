temperatures = (19, 23, 21, 21, 20, 18, 22)

# Concatenate tuples (this creates a new tuple)
all_temperatures = temperatures + (20, 21)
print(all_temperatures)

# Repeat a tuple
print(temperatures * 2)

# Check membership of a tuple
print(20 in temperatures)

# Printing minimum and maximum values from the tuple
print(f"The lowest temperature is: {min(temperatures)}")
print(f"The highest temperature is: {max(temperatures)}")

# Defining a funcion to calculate smallest likelyhood of failing
def likelyhood():
    likelyhoods = (50, 38, 27, 99, 4)
    return min(likelyhoods)

def run_task1():
    result = likelyhood()
    print(f"The smallest likelyhood of failing is: {result}")

if __name__ == "__main__":
    run_task1()