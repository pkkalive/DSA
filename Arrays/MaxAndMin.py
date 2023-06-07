"""
    Take input an array A of size N and write a program to print maximum and minimum elements of the
     input. The only line of the input would contain a single integer N that represents the length
     of the array followed by the N elements of the input array A.
"""
import sys


def max_min(nums):
    cur_max, cur_min = -sys.maxsize, sys.maxsize
    if len(nums) == 0:
        return []
    for num in nums:
        if num > cur_max:
            cur_max = num
        if num < cur_min:
            cur_min = num

    return [cur_max, cur_min]


print(max_min([1, 2, 3, 4, 5]))
print(max_min([10, 50, 40, 80]))
print(max_min([9, 9, 9, 9, 9, 9, 9]))
print(max_min([]))
