""" 
def play_guess_the_number():
    import random as rn

    print("Please enter the minimum value.")
    min_number = int(input())
    print("Please enter the maximum value.")
    max_number = int(input())
    random_number = rn.randint(min_number, max_number)
    print(f"I am thinking of a number between {min_number} and {max_number}. Can you guess what it is?")

    guess = int(input("Enter your guess:  "))
    while guess != random_number:
        if guess < random_number:
            print("Your guess is too low.")
            guess = int(input("Try again: "))
        else:
            print("Your guess is too high.")
            guess = int(input("Try again: "))

    print(f"Congratulations! You guessed the number {random_number} correctly!")

play_guess_the_number()
 """
