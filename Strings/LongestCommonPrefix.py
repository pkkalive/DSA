"""
    Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
    The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
    Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""


def longest_common_prefix(arr):
    n, i = len(arr) - 1, 1
    ans = arr[0]

    while i <= n and ans != "":
        cur = ""
        loop_len = min(len(ans), len(arr[i]))
        for j in range(loop_len):
            if arr[i][j] == ans[j]:
                cur += ans[j]
            else:
                break
        ans = cur
        i += 1
    return ans


print(longest_common_prefix(["abcdefgh", "aefghiertrhrh", "abcefgh"]))
print(longest_common_prefix(["aaaaa", "aaaa", "aaa", "aa"]))
print(longest_common_prefix(["abcd", "abde", "abcf"]))
print(longest_common_prefix(
    ["aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]))
