""""""
# 1  Create a class (2-D vector) and use it to create another class representing a 3-D vector.

"""
class vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def val2D(self):
        return f"{self.i}i + {self.j}j"


class vector3D(vector2D):  # it won't work without inheritance of vector2D because super() is used.
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def val3D(self):
        return f"{self.i}i + {self.j}j + {self.k}k "


inp = vector2D(5, 4)
print(inp.val2D())

inp2 = vector3D(3, 7, 8)
print(inp2.val3D())
"""


# 2 Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
# Add a method ‘bark’ to class ‘Dog’.

"""
class Animals:
    def __init__(self, n):
        self.n = n

    def isAnimal(self):
        print(f"Yes, {self.n} is an animal")


class Pets(Animals):
    def __init__(self, n):
        super().__init__(n)

    def isPet(self):
        print(f"Yes, {self.n} is a pet")


class Dog(Pets):
    def __init__(self, n):
        super().__init__(n)

    def bark(self):
        print(f"Your pet dog, {self.n} barks at the neighbour")


pet = Dog("Rosy")
pet.isPet()
pet.isAnimal()
pet.bark()
"""

# 3 Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

"""
class Employee:
    def __init__(self, name, PF = 1000):
        self.name = name
        self.PF = PF
#        self.salaryEmp = salaryEmp

    @property
    def salaryAfterIncrement(self):
        return (f"Your salary will be {int(self.salaryEmp + self.salaryEmp*0.1)} after increment of"
                f" {int(self.salaryEmp*0.1)}")

    def __str__(self):
        return (f"name : {self.name}, salary : {self.salaryEmp + self.PF}, PF : {self.PF}, increment :"
                f" {int(self.salaryEmp*0.1)}")

    def increment(self):
        # self.salaryEmp = salaryEmp - self.PF
        print(f"Your increment wil be 10% of {self.salaryEmp}")

    @salaryAfterIncrement.setter
    def setSalary(self, salaryEmp):
        self.salaryEmp = salaryEmp - self.PF
        print(f"{self.name}, Your Current salary is {self.salaryEmp + self.PF} including PF amount {self.PF}")

emp = Employee("rajiv", 5000)
emp.setSalary = 20000
emp.increment()
print(emp.salaryAfterIncrement)

print(emp)
"""

# 4 Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

"""
class Complex:
    def __init__(self, im=0, re=0):
        self.im = im
        self.re = re
    def __str__(self):
        return f"{self.im}i + {self.re}"
    def __add__(self, other):
        return f"addition: {self.im + other.im}i + {self.re + other.re}"
    def __mul__(self, other):
        return f"multiplication: {-self.im * other.im + self.re * other.re}"

c1 = Complex(3, 5)
print(c1)

c2 = Complex(2,6)
print(c2)

print(n1+n2)
print(n1*n2)
"""

# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.
# &
# 6. Write __str__() method to print the vector as follows:
#  7i + 8j +10k
# Assume vector of dimension 3 for this problem.
# &
# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

"""
class vector:
    def __init__(self, i=0, j=0, k=0):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return f"{self.i + other.i}i + {self.j + other.j}j + {self.k+other.k}k"

    def __mul__(self, other):
        return f"{self.i * other.i + self.j * other.j +self.k * other.k}"

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __len__(self):
        # l = [self.i, self.j, self.k]
        # return len(l)
        return 3
v1 = vector(3,5,1)
print(v1)

v2 = vector(11,2,5)
print(v2)

print(v1+v2)
print(v1*v2)
print(len(v1))
"""
