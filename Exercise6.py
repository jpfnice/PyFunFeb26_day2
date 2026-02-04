"""
Define a function to test if a number received as argument is a prime number or not

A prime number is:
    an int
    greater than 0
    that can only be divided by 1 and by itself
    
"""

def isPrime(aNumber):
    """
    isPrime returns True or False depending on the fact that aNumber
    is a prime number or not
    
    Parameters
    ----------
    aNumber : the int to be tested

    Returns
    -------
    True if aNumber is a prime number.
    False if aNumber is not a prime number.
    None if an error is encountered.

    """
    if not isinstance(aNumber, int):
        # For the moment, we haven't seen how to raise an exception, therefore
        # to indicate there is a problem with the argument received I used this
        # strategy: I print an error message then I return a None value
        # Most of the time, it this more interesting to "raise" an exception:
        # we will see that later on
        print("Wrong argument given: should be an int!")
        return None
    if aNumber <= 1:
        print("Wrong argument given: should be an int > 1!")
        return None
    for divisor in range(2,aNumber):
        if aNumber % divisor == 0:
            return False
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
        