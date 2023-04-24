from random import *
import time
import os

clear = lambda: os.system("cls")

max_range = randint(5, 100)
num_to_guess = randint(1, max_range)
lives = 6
last_guess = 0


def prompt(max_range):
    return f"Guess the number from 0 and {max_range}"


def is_correct(last_guess, num_to_guess):
    return last_guess == num_to_guess


def clue(last_guess, num_to_guess):
    if last_guess < num_to_guess:
        higher = f"Hint: **HIGHER! your last guess is {last_guess}\n"
        return higher
    else:
        lower = f"Hint: **LOWER! your last guess is {last_guess}\n"
        return lower

# def main(guess, num_to_guess):

#     while not is_correct(guess, num_to_guess):
#         clear()
#         prompt(max_range, lives, last_guess, num_to_guess)
#         last_guess = guess
#         lives -= 1
#         if lives == 0:
#             clear()
#             print(f"Guess credit ({lives})\n")
#             print(f"GAME OVER: the correct number is {num_to_guess}\n")
#             break
#         elif num_to_guess == guess:
#             clear()
#             print(f"\nLucky guess! the number is {num_to_guess}\n")
#             break


# entry will be check if equal to the num_to_guess
