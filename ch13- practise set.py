""""""
# 1. Create two virtual environments, install few packages in the first one. How do you
# create a similar environment in the second one?

# created myenv & myenv_copy

# 2. Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”
"""
name = str(input("Name: "))
marks = int(input("Marks: "))
phone = str(input("Ph no: "))
statement = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone )
print(statement)
"""

# 3. A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers.
"""
l = [str(7*i) for i in range(1,11)]
s = "\n".join(l)
print(s)
"""

# 4. Write a program to filter a list of numbers which are divisible by 5.
"""
div5 = lambda x:x%5==0
l = [i for i in range(1,32)]
x = filter(div5,l) # (or) print(list(filter(div5,l)))
print(list(x))
"""

# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
"""
# Generates a random list(AI generated)
import random
random_list = random.sample(range(1, 101), 10)
print(random_list)

# main program
from functools import reduce
func = lambda a,b:max(a,b)
maxValue = reduce(func,random_list)
print(maxValue)
"""

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar
# virtualenv.

# created sys_copy & requirements_sys.txt, requirements_sys_copy.txt

# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

