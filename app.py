### 1. Using self

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example usage
student = Student("Alice", 90)
student.display()


### 2. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
c1 = Counter()
c2 = Counter()
Counter.display_count()


### 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

# Example usage
car = Car("Toyota")
print(car.brand)
car.start()


### 4. Class Variables and Class Methods

class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example usage
print(Bank.bank_name)
Bank.change_bank_name("New Bank")
print(Bank.bank_name)


### 5. Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
result = MathUtils.add(5, 3)
print(result)


### 6. Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger created.")

    def __del__(self):
        print("Logger destroyed.")

# Example usage
logger = Logger()
del logger


### 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public
        self._salary = salary  # protected
        self.__ssn = ssn  # private

# Example usage
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)  # Accessible
print(emp._salary)  # Accessible but should be treated as protected
# print(emp.__ssn)  # Raises AttributeError


### 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage
teacher = Teacher("Mr. Smith", "Math")
print(teacher.name, teacher.subject)


### 9. Abstract Classes and Methods

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

# Example usage
rect = Rectangle(5, 3)
print(rect.area())


### 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Example usage
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

### 11. Class Methods

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
Book.increment_book_count()
print(Book.total_books)


### 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
print(fahrenheit)


### 13. Composition

class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

# Example usage
engine = Engine()
car = Car(engine)
car.start()


### 14. Aggregation

class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name


