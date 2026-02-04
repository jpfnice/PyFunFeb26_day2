"""  
List comprehension
"""

data=[5,6,7,-7,10,-2,11,-12,13,6,5]


# result=[]
# for e in data:
#     result.append(e**2)
# print(result)

result=[e**2 for e in data] # a "list comprehension"
print(result)

# result=[]
# for e in data:
#     if e > 0:
#         result.append(e**2)
# print(result)

result=[e**2 for e in data if e > 0] # a "list comprehension"
print(result)

result={e**2 for e in data if e > 0} # a "set comprehension"
print(result)
