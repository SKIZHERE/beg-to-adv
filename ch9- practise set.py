""""""
# File I/O
# 1 Checking twinkle in the file
"""
with open("file.txt", "r") as f:
    word = "twinkle"
    l = f.read()
    if word in l:
        print(f"{word} is present")
    else:
        print(f"{word} is absent")
"""
# 2 edit hi score every time
"""
def game(g):
#    g = int(input())
    f = open("hi-score.txt", "r")
    score = int(f.read())
    if score >= g:
        pass
        f.close()
        return (score)
    else:
        with open("hi-score.txt", "w") as f1:
            f1.write(str(g))
        return(g)
print(game(9))
"""

# 3 write table in different file of different folder
"""
import os

os.makedirs('Table', exist_ok=True)
for i in range(2,21):
    with open(f"G:\\python\\beg to adv\\Table\\Table {i}","w") as f:
        for j in range(1,11):
            pdt = i*j
            f.write(f"{i} x {j} = {pdt}\n")
"""

# 4 replacing word
"""
word = "donkey"
with open("badfile.txt", "r") as f :
    content= f.read()

NewContent = content.replace(word,"#####")

with open("badfile.txt", "w") as f:
    f.write(NewContent)
"""

# 5
"""
word = ["donkey", "the"]
with open("badfile.txt", "r") as f :
    content= f.read()

for i in word:
    content = content.replace(i,"#####")

with open("badfile.txt", "w") as f:
    f.write(content)
"""

# 6, 7
"""
with open("log.txt", "r") as f:
    l = f.readlines()
n=1
nl = []
word = "python"
for i in l:
    if word in i:
        nl.append(n)
    else:
        n+=1
print(f"the word {word} is in line :", nl)

#AI version faster and better readability
# with open("log.txt", "r") as f:
#     lines = f.readlines()
# 
# word = "python"
# matching_lines = [i for i, line in enumerate(lines, start=1) if word in line]
# 
print(f"The word '{word}' is found in lines:", matching_lines)
"""

# 8 copy of a file
"""
with open("log.txt", "r") as f:
    txt = f.read()
with open("Copy_log.txt","w") as f1:
    f1.write(txt)
print("copy succesfully made")
"""

# 9 checking copy of a file
"""
f,f1 = open("log.txt", "r"),open("badfile.txt", "r")
r,r1 = f.read(),f1.read()

if r==r1 :print("they both are same")
else: print("both are different")

f.close(),f1.close()
"""

# 10 wipe out the file
"""
with open("file.txt", "w") as f:
    pass
"""

# 11 rename a file
"""
with open("badfile.txt", "r") as old_file:
        content = old_file.read()

with open("renamed_by_python.txt", "w") as new_file:
        new_file.write(content)
"""
