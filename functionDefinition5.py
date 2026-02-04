"""
Function definition
"""
# A function that accept a variable number of named arguments:
def myfct(**args):
    print(args, type(args))

result=myfct(a=7, value=6, name="Maria", tel=87665)
print(result)

