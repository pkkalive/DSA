"""
    You are given an integer N you need to print all the Armstrong Numbers between 1 to N.
    (N inclusive).If sum of cubes of each digit of the number is equal to the number itself,
    then the number is called an Armstrong number.
    For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).
    Note: All the test cases in this problem are limited to 3-digit numbers.
"""


def armstrong_number(nums):
    for num in range(1, nums + 1):
        ans, temp = 0, num
        while temp > 0:
            last = temp % 10
            ans = ans + (last * last * last)
            temp = temp // 10

        if num == ans:
            print(ans)


armstrong_number(50)
armstrong_number(200)
