"""
    Problem Description:
    Take an integer A as input, you have to tell whether it is a prime number or not.
    A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
"""


def is_it_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return "No"
        i += 1

    return "Yes"


print(is_it_prime(3))
print(is_it_prime(5))
print(is_it_prime(10))
print(is_it_prime(15))
