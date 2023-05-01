def is_prime(num):
    if num > 2 and num%2 == 0:
        return False
    else:
        for item in range(2, int(num**0.5)+1):
            if num % item == 0:
                return False
        return True
    
x = is_prime(12)
print(x)