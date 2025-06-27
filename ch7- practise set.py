""""""
# 1 multipliation table of a given number
"""
n = int(input("Number: "))
for i in range(1,11):
    print(n," x ",i, " = ", n*i)
"""
# 2 greet person with name starting with "s"
"""
l = ["Harry","Soham","Sachin","Rahul"]
for i in l:
    if i.lower()[0] == "s":
        print("Good Morning",i )
    else:
        pass
"""
# 3
"""
n = int(input("Number: "))
x= 1
while x<11:
    print(n,"x",x, "=", n*x)
    x+=1
"""
# 4
"""
n = int(input("number: "))
x = n-1
while x>=2:
    if n%(x) == 0:
        print("it is not a prime number")
        break
    else:
        if x-1 == 1:
            print("it is a prime number")
            break
        else:
            x-=1
"""

# 5 sum of first n natural number
"""
n = int(input("Number: "))
x = 0
while n>0:
    x += n
    n -= 1
print(x)
"""

# 6 factorial using for loop
"""
n = int(input("Number: "))
x = 1
for i in range(1,n+1):
    x = x*i
print(x)
"""

# 7 star pattern
"""
n = 4
for i in range(n):
    x = (2*i)+1
    t = n-x
    print(" "*t, "*"*x)
"""

# 8 star pattern 2
"""
n = 3
for i in range(1,n+1):
    print("*"*i)
"""
# 9 star square patter
"""
n = 7
for i in range (1,n+1):
    if i ==1 or i == n:
        print("* "*n)
    else:
        x = n-2
        print("* "," "*x," *")
"""

# 10 print multiplication table of n in reverse order
"""
n = int(input("Number: "))
for i in range(10,0,-1):
    print(n," x ",i, " = ", n*i)
"""
