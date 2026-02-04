"""
Function definition
"""

def myfunction(arg1=0, arg2=0):
    temp=arg1+arg2  # temp is a local variable
    return temp # return None by default

result=myfunction(4,7)

print(result)

result=myfunction(4)

print(result)

result=myfunction()

print(result)

result=myfunction(arg2=19)
print(result)