# I assume the file "numbers.txt" exists, is readable and is in the
# current folder

myfile=open("numbers.txt")

# The simplest way to iterate through a file line by  
# line is to use a for loop (a file is an "iterable" object
# that's why we can use it in a for loop)

for line in myfile:
    print(line)
    
myfile.close()