def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return (number * 3) + 1


input_num = int(input("Enter number: "))

while input_num != 1:
    collatz(input_num)
    input_num = collatz(input_num)
    print(input_num)
