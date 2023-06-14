"""
    Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
    The digits are stored such that the most significant digit is at the head of the list.
    NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :
    Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
    A: For the purpose of this question, YES
    Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
    A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""


def plus_one(arr):
    result_num, power = 0, 1
    n = len(arr) - 1
    for i in range(n, -1, -1):
        num = arr[i] * power
        result_num += num
        power *= 10
    return result_num + 1


print(plus_one([1, 2, 3]))
print(plus_one([15, 16, 17]))
print(plus_one([0]))
