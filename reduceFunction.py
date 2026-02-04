"""  
The reduce function of the module functools

"""

import functools

data=[5,6,7,10,11,12,13,6,5]

# result=1
# for e in data:
#     result=result*e
# print(result)

def fct(a,b):
    return a*b

result=functools.reduce(fct, data)
print(result)


