
"""
str:
    an "immutable" sequence of characters
"""

# str methods, operators and functions
#import math

name="firST"

name=name.capitalize() # this a method call : objectname.methodname(..)

print(name) # this a built-in function call : functioname(..)

# math.cos(34) # this a function call : modulename.functioname(..)

# nb=(3*4)/(6+2)

# data=(45,67,67) # to create a tuple

name=name.upper() # lower()
print(name)

name="....Gordon...."
name=name.strip() # lstrip(), rstrip(), strip(".")
print(name, "the end")

data="23;45;56;67;68"
result=data.split(";")
print(result) # ['23', '45', '56', '67', '68']

data=['23', '45', '56', '67', '68']
result=":".join(data)
print(result) # "23:45:56:67:68"

path="image.gif"
print(path.endswith("gif"))

path="image.jpeg"
print(path.endswith("gif"))



