""""""
# 1  Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
"""
try:
    with (
        open("1.txt") as f1,
        open("2.txt") as f2,
        open("3.txt") as f3
    ):
        pass
except Exception as e:
    print(e)
"""
# 2 Write a program to print third, fifth and seventh element from a list using enumerate
# function.
"""
lst = ["a","b","c","d","e","f","g","h"]
for index , obj in enumerate(lst):
    if index + 1 in [3,5,7]:
        print(obj)
"""

# 3 Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.
"""
inp = int(input("Enter the number: "))
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [i*inp for i in l1 ]
print(l2)
"""

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.
"""
a = int(input("No 1: "))
b = int(input("No 2: "))

if b == 0:
    raise ZeroDivisionError("Infinite")

print(a/b)
"""
# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt
"""
inp = int(input("Enter the number: "))
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [i*inp for i in l1 ]
l3 = [f"{inp} x {index + 1} = {i}\n"for index, i in enumerate(l2)]
print(l2)
with open("Tables.txt","w") as f:
    f.writelines(l3)
"""