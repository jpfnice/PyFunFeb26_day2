"""
Function definition
"""
# A function that accept a variable number of positionnal arguments:
def mysum(*args):
    #print(args, type(args))
    total=0
    for e in args:
        total = total + e
    return total
    

result=mysum(4,7,8,10)
print(result)

result=mysum(4,7,8,10,67,89)
print(result)

# data=[5,6,7]
# result=mysum(data) # mysum receives as argument a list but it expect to receive numbers
# print(result)

data=[5,6,7]
result=mysum(*data) # <=> result=mysum(5,6,7)
print(result)