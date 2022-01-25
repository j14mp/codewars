"""
Description:
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
"""

def move_ten(st):
    forward = ''
    for x in st:
        if ord(x) <= 112:
            forward += chr(ord(x) + 10)
        else:
            forward += chr(ord(x) + 10 - 123 + 97)
    return forward
