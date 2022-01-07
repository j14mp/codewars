"""
Write a function that will check if two given characters are the same case.

'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1

If any of characters is not a letter, return -1.

If both characters are the same case, return 1.

If both characters are letters and not the same case, return 0.
"""

def same_case(a, b):
    if a.isalpha() and b.isalpha():
        return a.isupper() and b.isupper() or a.islower() and b.islower()
    return -1
