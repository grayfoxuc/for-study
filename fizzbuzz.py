"""
Print 1 - 100
Print fizz if number is divisible by 3
Print buzz if number is divisble by 5
Print fizzbuzz if number is divisible by both 3 and 5
"""
num = 1

while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num += 1
