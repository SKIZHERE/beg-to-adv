""""""
# 1
"""
l= []
for i in range(4):
    x = int(input("number : "))
    l.append(x)
n = l[0]
for i in range(1,len(l)):
    if l[i]>n:
        n = l[i]
    else:
        continue
print(n)
"""
# 2
"""
s1 = int(input("Subject 1: "))
s2 = int(input("Subject 2: "))
s3 = int(input("Subject 3: "))
t = (s1+s2+s3)/3

if s1<33 or s2<33 or s3<33 or t<40:
    print("Fail!")
else:
    print("Pass!")
"""

# 3
"""
spam = ["make a lot of money","buy now","subscribe this","click this"]
msg = str(input("Comment: "))
if msg in spam:
    print("Spam comment")
else:
    print("not a spam")
"""

# 4
"""
txt = str(input("enter username: "))
if len(txt)<10 :
    print("less than 10 character")
else:
    print("valid username")
"""

# 5
"""
lst = ["ram", "shyam", "kishor", "sukhvinder"]
n = str(input("name: "))
if n in lst :
    print("in list")
else:
    print("not in list")
"""

# 6
"""
mark = int(input("marks: "))
if mark<=100 and mark>=90:
    print("Ex")
elif mark < 90 and mark >= 80:
    print("A")
elif mark<80 and mark>=70:
    print("B")
elif mark<70 and mark>=60:
    print("C")
elif mark<60 and mark>=50:
    print("D")
else:
    print("F")
"""

# 7
"""
post = str(input("Enter the post: "))
if "harry" in post.lower():
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")
"""
