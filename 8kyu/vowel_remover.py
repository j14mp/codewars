"""
Create a function called shortcut to remove all the lowercase vowels in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

Don't worry about uppercase vowels.
"""

def shortcut(word):
    new_word = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word

"""
Top rated solution:
def shortcut(s):
    return s.translate(None, 'aeiou')
"""
