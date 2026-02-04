"""  
The reduce function of the module functools

"""

import functools

data=[5,6,7,10,11,12,13,6,5]

# def fct(a,b):
#     return a*b

result=functools.reduce(lambda a,b: a*b, data)
print(result)


