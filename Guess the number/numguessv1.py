from random import *
import os

clear = lambda: os.system("cls")


def prompt(max_range, lives, last_guess, num_to_guess):
    print("****************************************")
    print(f"Guess the number from 0 and {max_range}")
    print("****************************************")
    print(f"Guess credit ({lives})\n")
    clue(last_guess, num_to_guess)


def is_correct(guess, num_to_guess):
    return guess == num_to_guess


def clue(last_guess, num_to_guess):
    if last_guess < num_to_guess:
        print(f"Clue: **HIGHER! your last guess is {last_guess}\n")
    else:
        print(f"Clue: **LOWER! your last guess is {last_guess}\n")


def main():
    max_range = randint(5, 100)
    num_to_guess = randint(1, max_range)
    lives = 6
    guess = 0
    last_guess = 0
    while not is_correct(guess, num_to_guess):
        clear()
        prompt(max_range, lives, last_guess, num_to_guess)
        try:
            guess = int(input("What is your guess? \n"))
        except ValueError:
            print("Enter a valid number.")
        last_guess = guess
        lives -= 1
        if lives == 0:
            print(f"Guess credit ({lives})\n")
            print(f"GAME OVER: the correct number is {num_to_guess}\n")
            break
        elif num_to_guess == guess:
            print(f"\nLucky guess! the number is {num_to_guess}\n")
            break


main()
