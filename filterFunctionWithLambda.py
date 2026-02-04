"""  
The built-in filter function

"""

data=[5,6,7,10,11,12,13,6,5]


# def iseven(arg):
#     return arg%2 == 0

result=list(filter(lambda a:a%2==0, data))
print(result)


