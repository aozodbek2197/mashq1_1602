# 1-mashq
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.brand} {self.model} {self.year}")

c1 = Car("GM", "Cobalt", 2022)
c1.info()

# 2-mashq
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"{self.name} o‘qiyapti")

s1 = Student("Ali", 18, 11)
s1.study()

# 3-mashq
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"{self.title} kitobi o‘qilmoqda")

b1 = Book("Python", "John")
b1.read()

# 4-mashq
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area())

# 5-mashq
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

e = Employee("Bek", 500)
print(e.annual_salary())
