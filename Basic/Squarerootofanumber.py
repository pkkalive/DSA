"""
    Given a number A. Return square root of the number if it is perfect square otherwise return -1.
    Note: A number is a perfect square if its square root is an integer.
"""


def square_root(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return i

        i += 1
    return -1


print(square_root(4))
print(square_root(1001))