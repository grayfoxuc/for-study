"""
Enter a number and function will run the Collatz Sequence where
it will run and print the result until = 1
"""


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return (number * 3) + 1


while True:
    try:
        input_num = int(input("Enter number: "))
        break
    except:
        print("Please enter a valid number")
        continue

while input_num != 1:
    collatz(input_num)
    input_num = collatz(input_num)
    print(input_num)
