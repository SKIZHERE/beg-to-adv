""""""
# 1
"""
import datetime
name = str(input("Your Name:"))

current_time = datetime.datetime.now()
current_hour = current_time.hour

x = str()
if 5 <= current_hour < 12:
    x = "Morning!"
elif 12 <= current_hour < 18:
    x = "Afternoon!"
elif 18 <= current_hour < 22:
    x = "Evening!"
else:
    x = "Night!"

greet = f"Hi {name} Good {x}"
print(greet)
"""

# 2
"""
Name = str(input("Name :"))
Date = str(input("Date :"))
letter = f'''
Dear {Name},
You are selected!
{Date}'''
print(letter)
"""

# 3
"""
a = "Hi this is  a sentence  with double  spaces"
r = len(a)
n = 0
print(r)
for i in range(r):
    if a[i] ==" " and a[i+1] == " ":
        n+=1
print(f"the total number of double spaces are {n}")
"""

# 4
"""
a = "Hi this is  a sentence  with double  spaces"
r = len(a)
n = 0
print(r)
for i in range(r):
    if a[i] == " " and a[i + 1] == " ":
        n += 1
print(f"the total number of double spaces are {n}")
"""

# 5
"""
letter = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter)
"""
