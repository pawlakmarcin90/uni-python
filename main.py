import Week_4.module_task as module_t
import Week_4.built_in_functions as built_in_f

def run_week_4():
    response = input("Which program in Week 4 would you like to run?\n[number_game] or [ascii_converter]: ")

    if response == "number_game":
        module_t.play_guess_the_number()
    elif response == "ascii_converter":
        built_in_f.ascii_value()
def run():

    while(True):
        print("\nWhat do you want to do?\n")
        print("[a] Run Week 4 programs.\n")
        print("[b] Exit.\n")
        response = input(": ")

        if response == "a":
            run_week_4()
        elif response == "b":
            print("\nExiting the program. Goodbye!\n")
            break
        else:
            print("\nInvalid selection, try again.\n: ")

run()