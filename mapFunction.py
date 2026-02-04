"""  
The built-in map function

"""

data=[5,6,7,10,11,12,13,6,5]

# result=[]
# for e in data:
#     result.append(e**2)
# print(result)

def fct(arg):
    return arg**2

result=list(map(fct, data))
print(result)

text="45;67;78"
result=text.split(";")
print(result)

result2=list(map(int, result))
print(result2)
