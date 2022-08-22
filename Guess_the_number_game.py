from random import *
from rich.console import Console as c
import os

clear = lambda: os.system('cls')

c = c()

clear()

max_range = randint(5, 100)
guess = None
lives = 6

c.print("\n[yellow]****************************************[/]")
c.print("Guess the number from 0 and "+ str(max_range), style="bold")
c.print("[yellow]****************************************[/]")
num_to_guess = randint(0, max_range)


while guess != num_to_guess:
    try:
        c.print(f"Guess credit ({lives})")
        guess = int(input("\nWhat is your guess? \n"))
        last_guess = guess

        if guess == num_to_guess:
            print(f"Lucky guess! the number is {num_to_guess}")
        else:
            c.print("\n[yellow]****************************************[/]")
            c.print(f"Guess the number from 0 and {max_range}", style="bold")
            c.print("[yellow]****************************************[/]")
            if guess < num_to_guess:
                c.print(f"Clue: **HIGHER! your last guess is {str(last_guess)}")
            else:
                c.print(f"Clue: **LOWER! your last guess is {str(last_guess)}")
            lives -= 1
            if lives == 0:
                c.print(f"\nRan out of guess credit ({lives})")
                c.print(f"GAME OVER: the correct number is {num_to_guess}")
                break
    except:
        print("Please enter a valid number")
        continue
