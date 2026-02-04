
"""
str:
    an "immutable" sequence of characters
"""

# Creation:

name="Gordon says 'Hello'"
print(name, type(name))

name='Gordon says "Hello"'
print(name, type(name))

name="""This is 
a long 
string"""

print(name, type(name))

name='''This is a long string'''
print(name, type(name))

value=str(345.67)
print(value, type(value))

nb=3

text=f"nb is {nb}"
print(text)

text=f"nb is {nb} nb**2 {(nb+2)**3}"
print(text)

import math
text=f"nb is {nb} nb**2 {(nb+2)**3} cos(nb) is {math.cos(nb)}"
print(text)

text=f"nb is {nb:10} nb**2 {(nb+2)**3:<10} cos(nb) is {math.cos(nb):.2f}"
print(text)

# More info: https://docs.python.org/3/library/string.html#format-string-syntax
