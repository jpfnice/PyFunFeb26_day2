
"""
A set is a muttable collection (not a sequence !) which does accept duplicated
elements
"""

data={4,5,5,10,23,6,1,0,0}
print(data, type(data))

data=set([34,56,34,78])
print(data, type(data))

print(len(data))

for e in data:
    print(e)

s1={4,5,5,10,23,6,1,0}
s2={4,5,7,33,6,100}

s3=s1.union(s2)
print(s3)

s3=s1.intersection(s2)
print(s3)

s1.add(67)
print(s1)

s1.remove(5)
print(s1)

s1.pop()
print(s1)
