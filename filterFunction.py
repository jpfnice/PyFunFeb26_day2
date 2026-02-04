"""  
The built-in filter function

"""

data=[5,6,7,10,11,12,13,6,5]

# result=[]
# for e in data:
#     if e % 2 ==0:
#         result.append(e)
# print(result)

def iseven(arg):
    return arg%2 == 0

result=list(filter(iseven, data))
print(result)


