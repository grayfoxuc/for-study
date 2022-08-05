from random import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

max_range = randint(5, 100)
guess = None

print("****************************************")
print(f"Guess the number from 0 and {max_range}")
print("****************************************")
num_to_guess = randint(0, max_range)


while guess != num_to_guess:
    try:
        guess = int(input("What is your guess? \n"))
        last_guess = guess

        if guess == num_to_guess:
            print(Fore.YELLOW + f"Lucky guess! the number is {num_to_guess}")
        else:
            print("****************************************")
            print(f"Guess the number from 0 and {max_range}")
            print("****************************************")
            if guess < num_to_guess:
                print(
                    f"Clue: "
                    + Fore.RED
                    + "**HIGHER!"
                    + Fore.WHITE
                    + " --your last guess is "
                    + Fore.CYAN
                    + str(last_guess)
                )
            else:
                print(
                    "Clue: "
                    + Fore.RED
                    + "**LOWER!"
                    + Fore.WHITE
                    + " --your last guess is "
                    + Fore.CYAN
                    + str(last_guess)
                )
            print("Guess again :(")
    except:
        print("Please enter a valid number")
        continue
