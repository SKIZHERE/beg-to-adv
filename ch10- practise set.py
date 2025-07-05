""""""
# 1
"""
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, exp):
        self.salary = salary
        self.name = name
        self.exp = exp

ramu = Programmer("ramu", 120000, 4)
print(ramu.name,ramu.salary,ramu.exp,ramu.company)
"""

# 2 calculator
"""
class Calculator:
    def __init__(self,n):
        self.n = n
#        print(n)
    def square(self):
        print(f"The square is {self.n**2}")
    def cube(self):
        print(f"The cube is {self.n**3}")
    def sqrt(self):
        print(f"The square root is {self.n**(1/2)}")
a = Calculator(4)
print(a.n)
a.sqrt()
a.square()
a.cube()
"""

# 3
"""
class temp:
    a=6

obj = temp()
print(obj.a)
obj.a = 0 # Instance Attribute
print(obj.a)
print(temp().a)
# Class Attribute does not change, it remains but object property changes
"""
# 4
"""
class Calculator:
    def __init__(self,n):
        self.n = n
        print("")
    def square(self):
        print(f"The square is {self.n**2}")
    def cube(self):
        print(f"The cube is {self.n**3}")
    def sqrt(self):
        print(f"The square root is {self.n**(1/2)}")

    @staticmethod
    def greet():
        print("good morning")
a = Calculator(4)
print(a.n)
a.sqrt()
a.square()
a.cube()
a.greet()
"""

# 5, 6
"""
import random

class Train:
    def __init__(slf, TrainNo):
        print("Welcome to Indian Railways")
        slf.TrainNo = TrainNo

    def bookTicket(self, dep, dest):
        print(f"Your Train ticket is booked for train no : {self.TrainNo} from {dep} to {dest}")

    def getStatus(self):
        print(f"Train no {self.TrainNo} is running on time")

    def getFare(harry, dep, dest):
        print(f"Your Train ticket is booked for train no : {harry.TrainNo} from {dep} to {dest} \n Total fare {random.randint(200,2000)}")

ram = Train(123125)
ram.getFare("Delhi","Chennai")
ram.bookTicket("Delhi","Chennai")
ram.getStatus()
"""