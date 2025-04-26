class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example
s1 = Student("Alice", 85)
s1.display()
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example
c1 = Counter()
c2 = Counter()
Counter.display_count()
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

# Example
car1 = Car("Toyota")
print(car1.brand)
car1.start()
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
print(b1.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example
print(MathUtils.add(5, 7))
class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

# Example
logger = Logger()
del logger
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

# Example
e = Employee("John", 50000, "123-45-6789")
print(e.name)
print(e._salary)
# print(e.__ssn)  # This will cause an error
print(e._Employee__ssn)  # Correct way to access private variable
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example
t = Teacher("Mr. Smith", "Math")
print(t.name, t.subject)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example
rect = Rectangle(5, 3)
print(rect.area())
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Example
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example
Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example
print(TemperatureConverter.celsius_to_fahrenheit(0))
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

# Example
eng = Engine()
my_car = Car(eng)
my_car.start_car()
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.employee = emp

# Example
e = Employee("Alice")
d = Department(e)
print(d.employee.name)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Example
obj = D()
obj.show()
print(D.mro())
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Example
say_hello()
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Example
p = Person()
print(p.greet())
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example
p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

# Example
mul = Multiplier(3)
print(mul(10))
print(callable(mul))
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Example
try:
    check_age(16)
except InvalidAgeError as e:
    print(e)
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Example
for num in Countdown(5):
    print(num)
