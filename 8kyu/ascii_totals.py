"""
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all ASCII characters.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291
"""

def uni_total(str):
    sum = 0
    for val in str: sum += ord(val)
    return sum
  
"""
Most popular solution:
def uni_total(string):
    return sum(map(ord, string))
    
    map(function, iterator)
    map returns a list
"""
