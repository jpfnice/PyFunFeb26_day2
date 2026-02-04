
"""
str:
    an "immutable" sequence of characters
"""

# Special character: '\n' '\t' '\a' '\b'

name="first second third"
print(name)

name="""first
second
third
"""
print(name)

name="first\nsecond\nthird\n"
print(name)

name="""first
    second
third
"""
print(name)

name="first\n\tsecond\nthird\n"
print(name)

path="c:\temp\newfile.py"
print(path)

path="c:\\temp\\newfile.py"
print(path)

path=r"c:\temp\newfile.py" # r means raw
print(path)





