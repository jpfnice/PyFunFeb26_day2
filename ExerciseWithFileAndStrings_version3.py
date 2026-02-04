"""  
Given a file with this format (you can use "data.txt" for instance or create your own test file):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.

To extract the 2 float out of each line you could:
    1) use slices
    2) use 2 split() methods
    3) use another strategy ??
    
Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

"""
import math

datafile=open("data.txt")

X1=[]
X2=[]

for line in datafile:
    # a line do have the following format:
    #  "    x1:0.34;x2:0.56\n"
    
    firstIndex=line.index(":") # position of the first ":"
    secondIndex=line.index(";")# position of the first ";"
    thirdIndex=line.index(":",secondIndex) # position of the second ":" see help(str.index)
    
    firstValue=float(line[firstIndex+1:secondIndex]) # a slice to get the first float
    secondValue=float(line[thirdIndex+1:]) # a slice to get the second float
    X1.append(firstValue)
    X2.append(secondValue)   

datafile.close()

print(X1)
print(X2)

Y1=[]
Y2=[]

for index in range(len(X1)):
    Y1.append(math.cos(X1[index]))
    Y2.append(math.cos(X2[index]))

print(Y1)
print(Y2)
    
