""""""
# 1 find greatest of 3 numbers
"""
def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
x = 1
y = 23
z = 3
print(great(x,y,z))
"""

# 2 celsius to farenheit
"""
def TempConvn(c):
    f = ((c*9)/5) + 32
    return f
print(TempConvn(100))
"""

# 3 how to prevent print() to prevent printing a new line at the end

# by using print("x",end="")

# 4 recursive function to find sum of n natural numbers
"""
def Sum(n):
    if n == 1:
        return 1
    else:
        return n+Sum(n-1)
print(Sum(999)) #recurison has a limit of 997 it can print upto 999 here
"""

# 5
"""
def patt(n):
    if n == 1:
        print("*")
    else:
        print("*"*n)
        return patt(n-1)
patt(10)
"""
# AI Version
"""
def patt(n):
    if n == 0:
     return
    print("*"*n)
    patt(n-1)
patt(3)
"""

# 6 inch to cm conversion
"""
def inTocm(n):
    return n*2.54
print(inTocm())
"""

# 7 func to remove a given word from the list and also strip it at the same time
"""
def remstr(l,word):
    n = []
    for i in l:
        if i != word:
            n.append(i.strip(word))
    return n
l = ["Harry","Rohan","Shubham","an"]
print(remstr(l,"an"))
#"""

# 8 print multiplication table
"""
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
table(5)
"""
