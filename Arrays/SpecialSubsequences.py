"""
    You have given a string A having Uppercase English letters.
    You have to find how many times subsequence "AG" is there in the given string.
    NOTE: Return the answer modulo 109 + 7 as the answer can be very large
"""


def special_subsequences(string):
    a_count, total_count, MOD = 0, 0, 10**9 + 7
    for s in string:
        if s == 'A':
            a_count += 1
        if s == 'G':
            total_count += a_count

    return total_count % MOD


print(special_subsequences("ABCGAG"))
print(special_subsequences("GAB"))
