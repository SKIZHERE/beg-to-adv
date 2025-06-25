""""""
# 1
"""
d = {"Namaste": "Hello", "Dhanyavaad": "Thank you", "Pyaar": "Love", "Sukh": "Happiness", "Dost": "Friend"}

x = str(input("enter the word: "))
print(d.get(x))
"""

# 2
"""
s = set()
for i in range(8):
    ui = int(input("enter the number: "))
    s.add(ui)
print(s)
# for i in range(len(s)):
#     print(s.pop(), end=" ")
"""

# 3
"""
s = {18, "18"}
print(s)

#Yes
"""

# 4
"""
s= set()
s.add(20)
s.add(20.0) #treated same as int of 20 
s.add("20")
print(len(s))
print(s)
"""

# 5
"""
s = {}
print(type(s)) #Dictionary
"""

# 6,7,8
"""
d = {}
for i in range(4):
    n = str(input("Name: "))
    l = str(input("Language: "))
    d.update({n:l})
print(d)
"""

# 9 can you change the values inside a list that is contained in a set s?
"""
s = {8,7,12,"Haryy", [1,2]}
"""
# no, because sets do not have indexing and are unordered




