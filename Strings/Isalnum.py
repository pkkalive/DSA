"""
    You are given a function isalpha() consisting of a character array A.
    Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.
"""


def isalnum(arr):
    for letter in arr:
        if 'a' <= letter <= 'z':
            continue
        if 'A' <= letter <= 'Z':
            continue
        if '0' <= letter <= '9':
            continue
        return 0
    return 1


print(isalnum(['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']))
print(isalnum(['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']))
