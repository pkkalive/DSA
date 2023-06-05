"""
    Given the Number of Test Cases as T, For each test case, take an integer N as input, you have to tell
    whether it is a perfect number or not. A perfect number is a positive integer that is equal to the sum
    of its proper positive divisors (excluding the number itself). A positive proper divisor divides a
    number without leaving any remainder.
"""


def is_it_perfect(num):
    ans, i = 0, 1
    while i < num:
        if num % i == 0:
            ans += i
        i += 1

    if ans == num:
        print("YES")
    else:
        print("NO")


is_it_perfect(4)
is_it_perfect(6)
