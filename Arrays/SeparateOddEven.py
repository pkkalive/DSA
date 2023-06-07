"""
    You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A.
    You have to print the odd and even elements of array A in 2 separate lines.
    NOTE: Array elements should have the same relative order as in A.
"""


def separate_even_odd(arr):
    even, odd = [], []
    for num in arr:
        if num & 1 == 0:
            even.append(num)
        else:
            odd.append(num)

    for num in odd:
        print(num, end=" ")
    print()
    for num in even:
        print(num, end=" ")
    print()


separate_even_odd([1, 2, 3, 4, 5])
separate_even_odd([4, 3, 2])
