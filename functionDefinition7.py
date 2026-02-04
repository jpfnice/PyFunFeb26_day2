"""
Function definition
"""

def add(arg1, arg2):
    """
    This function add tkaes 2 arguments
    arg1 and arg2
    It returns the addition of arg1 and arg2
    """
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1+arg2
    else:
        print("Wrong type of argument received")
        return None
        # Here you could raised an exception instead

print(add("abc", "def"))
print(add(12, 23))
print(add(12, "abc"))

somme=add # somme is now an alias of add

print(somme(129, 23))