def is_prime(num: int) -> bool:
    """
    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. In other words, a prime number is a number that can only be evenly divided by 1 and itself.
    For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41 are prime numbers.
    On the other hand, numbers like 4, 6, 8, 9, 10, 12, 14, and 15 are not prime numbers, because they have divisors other than 1 and themselves. For example, 4 can be evenly divided by 2, so it is not a prime number.
    Prime numbers have many interesting properties and applications in mathematics and computer science. They are used in cryptography, number theory, and other areas of research.
    """
    if num > 2 and num % 2 == 0:
        return False


test = is_prime(15)
print(test)
