"""
    Write a program to find sum all Natural numbers from 1 to N where you have to take N as input
    from user
"""


def summation_game(num):
    return (num * (num + 1)) // 2


print(summation_game(50))
print(summation_game(100))
