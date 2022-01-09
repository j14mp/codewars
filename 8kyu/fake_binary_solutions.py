"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""

def fake_bin(num_string):
    bi_string = ""
    for num in num_string:
        if int(num) < 5:
            bi_string += '0'
        else:
            bi_string += '1'
    return bi_string
  
  """
  Problems I had:
  I was turning num_string into an int which made it impossible to iterate through.
  I can only iterate through the string.
  I was supposed to turn num into an int and then compare
  Then I set bi_string += to a string character
  """
