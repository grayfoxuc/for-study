from ast import Not
from operator import is_not
from random import *

max_range = randint(5,100)
guess=None

print("****************************************")
print(f"Guess the number from 0 and {max_range}")
print("****************************************")
num_to_guess = randint(0, max_range)


while guess != num_to_guess:
    guess = int(input("What is your guess? \n"))
    last_guess = guess
    if guess == num_to_guess:
        print(f"Lucky guess! the number is {num_to_guess}")
    else:
        print("****************************************")
        print(f"Guess the number from 0 and {max_range}")
        print("****************************************")
        if guess < num_to_guess:
            print(f"Clue: **HIGHER! --your last guess is {last_guess}")
        else:
            print(f"Clue: **LOWER! --your last guess is {last_guess}")
        print("Guess again :(")