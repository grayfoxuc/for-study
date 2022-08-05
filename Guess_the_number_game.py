from random import *
from colorama import Fore, init

init(autoreset=True)

max_range = randint(5, 100)
guess = None
lives = 6

print("****************************************")
print(f"Guess the number from 0 and {max_range}")
print("****************************************")
num_to_guess = randint(0, max_range)


while guess != num_to_guess:
    try:
        print(f"Guess credit ({lives})")
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
            lives -= 1
            if lives == 0:
                print(f"\nRan out of guess credit ({lives})")
                print("GAME OVER")
                break
    except:
        print("Please enter a valid number")
        continue
