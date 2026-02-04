"""
Define a function to test if a number received as argument is a prime number or not

A prime number is:
    an int
    greater than 0
    that can only be divided by 1 and by itself
    
"""

def isPrime(arg1):
    return True


while True:
    value=input("Enter a number to be tested or 'stop' to stop the script: ")    
    if value == 'stop':
        print("Bye!")
        break
    value=int(value)
    if isPrime(value):
        print(value, "is a prime number")
    else:
        print(value, "is a not prime number")
        