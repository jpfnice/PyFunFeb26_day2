# The built-in range() function:
    
data=[5,16,True, 45,66, 188, "last"]

# To print each element of data in turn:
for e in data:
    print(e)
    
print()

# To print each element of data in turn except the first one:
for e in data[1:]:
    print(e)

print()

# To print the number (int) between 2 and 5:
for index in range(2,6):
    print(index)

print()

# To print each element of data in turn with it's position:
for index in range(len(data)):
    print(index, data[index])
    
print()

# To print the element of data at position 1 and 2: 
for index in range(1,3):
    print(index, data[index])
    
print()

# To print the element of data at position 0,1,2,3,4:  
for index in range(5): # 0,1,2,3,4
    print(index, data[index])

print()

# To create a list composed of the numbers (int) between 10 and 19:
numbers=list(range(10,20))
print(numbers)
