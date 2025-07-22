# 1 Walrus Operator :=  helps to assign value to a variable inside an expression
"""
if (n := len([1,2,3,4])) > 3:
    print(f"list is too long, {n} elements, <3 expected")
"""

# 2 Types Definition in Python - used to define the type of variable whether int or string or dict etc.
# we use the module typing, and function such as List, Tuple, Dict, and Union
"""
age : int = 25
def greeting (name: str) -> str:
    return f"Hello, {name}"
print(greeting("Raj"))
"""
"""
from typing import List, Tuple, Dict, Union

num: List[int] = [1, 2, 3, 4]
PAge: Tuple[str, int] = ("Ally", 22)
score: Dict[str, int] = {"raj": 20, "mahi": 7}
ID: Union[int, str] = "AB123"
print(num)
"""


# 3 Match Case - if case matches then the output is given accordingly
"""
def http_status(statusCode):
    match statusCode:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status code"


print(http_status(505))
"""
# 4 Dictionary Merge - used to merge 2 dictionary together, or update values
"""
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = d1 | d2
print(merged)
"""

# 5 opening multiple files using one with statement
"""
with(
    open("file1.txt", "w") as f1,
    open("file2.txt", "w") as f2
):
    pass
"""

# 6 Exception handling,
# try except,
# raising an error,
# try with else clause,
# try with finally clause.
"""
try:
    age = int(input("enter you age: "))
    print(age)
except ValueError as e: #except Exception as e
    print(e)
#"""

"""
a = int(input("Number 1: "))
b = int(input("Number 2: "))
if b == 0:
    raise ZeroDivisionError("we cannot divide by zero")
else:
    print(a/b)
"""
# try with else
"""
def main():
    try:
        a = int(input("Enter the number: "))
        print(a)


    except Exception as e:
        print(e)


    else: # runs, only when try block runs, overriden by return statment, i.e. doesnt run when return statement is
        # run in the try block
        print("hey this is else block")

main()
"""
# try with finally
"""
def main():
    try:
        b = 5
        a = int(input("Enter the number: "))
        if a == 0:
            raise Exception("we do not take zeros, lol")
        print(b/a)
        return

    except Exception as e:
        print(e)
        return

    finally: # always runs, overrides return
        print("hey this is finally block")
        return

main()
"""
# try with statement
"""
def main():
    try:
        a = int(input("Enter the number: "))
        print(a)
        return 

    except Exception as e:
        print(e)
        return 

    print("hey this is statment block in func") # does not run when return in any statement, otherwise runs always

main()
"""
from modlue import myFunc




