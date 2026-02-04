"""
Function definition
"""

def myfunction(arg1=0, arg2=0):
    temp=arg1+arg2  # temp is a local variable
    return temp # return None by default
    print("The end") # This statement is "unreachable" this is not a
    # syntax error, but this satement is useless
    

result=myfunction(4,7)

print(result)

