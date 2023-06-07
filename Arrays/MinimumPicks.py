"""
    You are given an array of integers A of size N. Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
"""
import sys


def minimum_picks(arr):
    even_max, odd_min = -sys.maxsize, sys.maxsize
    for num in arr:
        if num & 1 == 0 and num > even_max:
            even_max = num
        if num & 1 == 1 and num < odd_min:
            odd_min = num

    return even_max - odd_min


print(minimum_picks([0, 2, 9]))
print(minimum_picks([5, 17, 100, 1]))