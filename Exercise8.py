"""
Define a function addList which purpose element by element 2 lists of numbers:
    
    d1=[5,6,7]
    d2=[20,10,11]
    result=addList(d1,d2) # [25, 16, 18]
    
    d1=[5,6,7,10,5]
    d2=[20,10,11]
    result=addList(d1,d2) # [25, 16, 18, 10, 5]
"""

def addList(arg1, arg2):
    return [] # TO BE COMPLETED

d1=[5,6,7]
d2=[20,10,11]
result=addList(d1,d2) 
print(result) # [25, 16, 18]

d1=[5,6,7,10,5]
d2=[20,10,11]
result=addList(d1,d2) 
print(result)  # [25, 16, 18, 10, 5]

d1=[5,6,7]
d2=[20,10,11,32,34]
result=addList(d1,d2) 
print(result)  # [25, 16, 18, 32, 34]

d1=[]
d2=[]
result=addList(d1,d2) 
print(result)  # []
    
    