"""
    You are given a string A of size N consisting of lowercase alphabets.
    You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
    Find the minimum number of distinct characters in the resulting string.
"""


def change_characters(word, k):
    my_dist = {}
    for ch in word:
        my_dist.update({ch: my_dist.get(ch, 0) + 1 or 1})
    count = []
    for i in my_dist:
        count.append(my_dist.get(i))
    count.sort()
    ans = len(count)
    for i in count:
        if i <= k:
            k -= i
            ans -= 1
    return ans


print(change_characters("abcabbccd", 3))
print(change_characters("abcabbccd", 0))
