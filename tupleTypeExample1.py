"""
tuple:
    a tuple is an "immutable" sequence
    len(), for, in, not in, +, [], [:]
"""

data=(23,45,67,12)
print(data, type(data))

data=23,45,56
print(data, type(data))

data=tuple([4,5,6,7])
print(data, type(data))

for x1 in data:
    print(x1)

print("size of data is ",len(data))

print(data[1])


