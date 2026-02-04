# I assume the file "numbers.txt" exists, is readable and is in the
# current folder

myfile=open("c:/Users/jpf/pyfunfeb26/numbers.txt")

# The simplest way to iterate through a file line by  
# line is to use a for loop (a file is an "iterable" object
# that's why we can use it in a for loop)

for line in myfile:
    result=line.split(":")
    total=0
    for e in result:
        total = total + int(e)
    print(total)
   

    
myfile.close()