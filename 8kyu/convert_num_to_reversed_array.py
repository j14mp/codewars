"""
Description:
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
0 => [0]
"""

def digitize(n):
    n =str(n)
    n = list(n)
    n.reverse()
    return [int(i) for i in n]
  
"""
Most popular solution
"""

def digitize(n):
    return map(int, str(n)[::-1])
  
def digitize(n):
    return [int(x) for x in reversed(str(n))]
