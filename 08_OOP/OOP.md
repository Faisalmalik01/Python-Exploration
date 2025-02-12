# Complete Guide to Object-Oriented Programming (OOP) in Python

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [The __init__ Method](#the-init-method)
3. [Access Control with Underscores](#access-control-with-underscores)
4. [Classes and Objects](#classes-and-objects)
5. [Constructors](#constructors)
6. [Class Variables vs Instance Variables](#class-variables-vs-instance-variables)
7. [Methods](#methods)
8. [Inheritance](#inheritance)
9. [Polymorphism](#polymorphism)
10. [Encapsulation](#encapsulation)
11. [Abstraction](#abstraction)
12. [Static Methods](#static-methods)
13. [Property Decorators](#property-decorators)
14. [Multiple Inheritance](#multiple-inheritance)
15. [Method Overriding](#method-overriding)
16. [Method Overloading](#method-overloading)
17. [Operator Overloading](#operator-overloading)
18. [Abstract Classes and Interfaces](#abstract-classes-and-interfaces)
19. [Mixins](#mixins)
20. [Decorators](#decorators)

---

## Introduction to OOP

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into objects that contain both data and behavior. Python is a versatile language that fully supports OOP principles.

**Key OOP Principles:**
- **Encapsulation:** Bundling data and methods that operate on that data within a single unit
- **Inheritance:** Creating new classes that are built upon existing classes
- **Polymorphism:** Using a single interface with multiple implementations
- **Abstraction:** Hiding complex implementation details and showing only necessary features

**Benefits of OOP:**
- Improved code organization and modularity
- Better code reusability
- Enhanced maintainability
- More natural mapping of real-world problems to code
- Easier debugging and testing

---

## The __init__ Method

The `__init__` method is a special method in Python classes that serves as the constructor. It's automatically called when creating a new instance of a class.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand    # Public attribute
        self._model = model   # Protected attribute
        self.__year = year    # Private attribute
        
    def get_info(self):
        return f"{self.brand} {self._model} ({self.__year})"

# Creating an instance calls __init__ automatically
my_car = Car("Toyota", "Corolla", 2023)
print(my_car.get_info())  # Output: Toyota Corolla (2023)
```

**Key Points about __init__:**
- It's called automatically when creating new instances
- The first parameter must be `self`
- It can take any number of additional parameters
- It's used to initialize instance attributes
- It doesn't return anything (returns None implicitly)

---

## Access Control with Underscores

Python uses naming conventions with underscores to indicate access levels.

### Single Underscore (_)

The single underscore indicates protected access (convention only):

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public
        self._salary = salary     # Protected
    
    def _calculate_bonus(self):   # Protected method
        return self._salary * 0.1

emp = Employee("John", 50000)
print(emp.name)         # Accessing public attribute
print(emp._salary)      # Can still access, but shouldn't
```

### Double Underscore (__)

The double underscore implements name mangling for private access:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # Public
        self._type = "Savings"    # Protected
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(account.owner)           # Works fine
print(account._type)          # Works, but shouldn't be accessed
# print(account.__balance)    # AttributeError
print(account.get_balance())  # Correct way to access private attribute
```

### Special Methods (Dunder Methods)

Methods surrounded by double underscores are special methods:

```python
class Point:
    def __init__(self, x, y):        # Constructor
        self.x = x
        self.y = y
    
    def __str__(self):               # String representation
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):        # Addition operator
        return Point(self.x + other.x, self.y + other.y)
    
    def __len__(self):               # Length
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

p1 = Point(3, 4)
p2 = Point(1, 2)
print(str(p1))          # Calls __str__
print(p1 + p2)          # Calls __add__
print(len(p1))          # Calls __len__
```

---

## Classes and Objects

A class is a blueprint for creating objects. Objects are instances of a class.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.display_info())  # Output: Toyota Corolla
print(car2.display_info())  # Output: Honda Civic
```

---

## Class Variables vs Instance Variables

Understanding the difference between class and instance variables is crucial.

```python
class Employee:
    # Class variable shared by all instances
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables unique to each instance
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

# Using class and instance variables
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(Employee.company)        # Accessing class variable
print(emp1.name)              # Accessing instance variable
print(Employee.employee_count) # Output: 2
```

---

## Methods

Methods define object behaviors. Python supports several types of methods.

### Instance Methods
```python
class Car:
    def start_engine(self):      # Instance method
        return "Engine started!"

    def stop_engine(self):       # Instance method
        return "Engine stopped!"
```

### Class Methods
```python
class Car:
    @classmethod
    def get_vehicle_type(cls):   # Class method
        return "This is a car"
```

### Static Methods
```python
class Car:
    @staticmethod
    def get_info():             # Static method
        return "Cars are vehicles with wheels"
```

---

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return "Starting vehicle"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def start(self):
        return f"Starting {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.start())  # Output: Starting Toyota Corolla
```

---

## Polymorphism

Polymorphism allows methods to behave differently based on the object that calls them.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

---

## Property Decorators

Property decorators provide a way to customize attribute access.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)     # Using getter
temp.celsius = 30       # Using setter
print(temp.fahrenheit)  # Using computed property
```

---

## Multiple Inheritance

Python supports inheriting from multiple classes.

```python
class Engine:
    def start(self):
        return "Engine starting"

class Electric:
    def charge(self):
        return "Charging"

class HybridCar(Engine, Electric):
    def __init__(self, brand):
        self.brand = brand
    
    def start_car(self):
        return f"{self.start()} and {self.charge()}"

hybrid = HybridCar("Toyota")
print(hybrid.start_car())
```

---

## Abstract Classes and Interfaces

Abstract classes define methods that must be implemented by subclasses.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

# car = Car()
# print(car.start_engine())  # Output: Car engine started
```

---

## Mixins

Mixins provide reusable functionality to classes.

```python
class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class Car(LoggerMixin):
    def start_engine(self):
        self.log("Engine started")
        return "Engine is running"

car = Car()
car.start_engine()  # Output: Log: Engine started
```

---

## Decorators

Decorators modify or enhance class or method behavior.

```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result
    return wrapper

class DataProcessor:
    @timer
    def process_data(self):
        # Simulating some processing
        import time
        time.sleep(1)
        return "Data processed"

processor = DataProcessor()
processor.process_data()
```