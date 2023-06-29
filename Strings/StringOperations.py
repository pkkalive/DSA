"""
    Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
        Concatenate the string with itself.
        Delete all the uppercase letters.
        Replace each vowel with '#'.
    You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
    NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
"""


def string_operations(word):
    ans = ""
    for letter in word:
        if 'A' <= letter <= 'Z':
            continue
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            ans += '#'
        else:
            ans += letter

    return ans * 2


print(string_operations("aeiOUz"))
