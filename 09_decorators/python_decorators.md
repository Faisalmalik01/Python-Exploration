# Python Decorators Explained

## Introduction

Decorators in Python are a powerful feature that allows us to modify the behavior of functions or methods without changing their code. They provide a clean and reusable way to extend functionalities such as logging, caching, authorization, and performance tracking.

In simple terms, a decorator is a function that takes another function as an argument and returns a modified version of it.

---

## Understanding Decorators

### 1. Functions are First-Class Citizens in Python

Python allows functions to be:

- ✅ Assigned to variables
- ✅ Passed as arguments to other functions
- ✅ Returned from functions

This enables the creation of decorators.

**Example:**

```python
def greet():
    return "Hello, World!"

say_hello = greet  # Assign function to a variable
print(say_hello())  # Output: Hello, World!
```

---

### 2. Functions Inside Functions (Nested Functions)

A function can be defined inside another function, which is key to understanding decorators.

```python
def outer():
    def inner():
        print("Inside inner function!")
    
    inner()  # Calling inner function

outer()  # Output: Inside inner function!
```

---

### 3. Functions as Arguments

A function can accept another function as a parameter, allowing us to modify its behavior.

```python
def shout(text):
    return text.upper()

def greet(func):
    print(func("hello!"))  # Passing a function as an argument

greet(shout)  # Output: HELLO!
```

---

## What is a Decorator?

A decorator is a function that takes another function, adds functionality to it, and returns it.

---

### Basic Decorator Example

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()  # Calling the original function
        print("Something after the function runs")
    return wrapper  # Return the modified function

@my_decorator  # Applying the decorator
def say_hello():
    print("Hello, World!")

say_hello()
```

**Output:**

```
Something before the function runs
Hello, World!
Something after the function runs
```

---

## Types of Python Decorators

### 1. Timer Decorator (Measuring Execution Time)

```python
import time  

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)  # Simulating delay
    print("Function execution complete!")

slow_function()
```

---

### 2. Debug Decorator (Logging Function Calls)

```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_str = ', '.join(str(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with arguments ({args_str}, {kwargs_str})")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")
```

**Output:**

```
Calling greet with arguments (Alice, greeting=Hi)
Hi, Alice!
```

---

### 3. Caching Decorator (Memoization)

Useful for optimizing expensive function calls.

```python
def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print(f"Cache hit: {args} -> {cache_dict[args]}")
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        print(f"Cache miss: {args} -> {result}")
        return result

    return wrapper

@cache
def slow_add(a, b):
    time.sleep(3)  # Simulating a slow operation
    return a + b

print(slow_add(2, 3))  # Cache miss
print(slow_add(2, 3))  # Cache hit
```

---

### 4. Authentication Decorator (Access Control)

```python
def require_login(func):
    def wrapper(user):
        if not user.get("authenticated", False):
            print("Access Denied! Please log in.")
            return
        return func(user)
    return wrapper

@require_login
def view_dashboard(user):
    print(f"Welcome, {user['name']}!")

user1 = {"name": "Faisal", "authenticated": True}
user2 = {"name": "Guest", "authenticated": False}

view_dashboard(user1)  # Access granted
view_dashboard(user2)  # Access denied
```

---

## Chaining Multiple Decorators

Python allows multiple decorators to be applied to a single function.

```python
@timer
@debug
def add(a, b):
    return a + b

print(add(3, 5))
```

The execution order is from bottom to top:

1️⃣ `debug` decorates `add`.  
2️⃣ `timer` decorates the result of `debug(add)`.

---

## Best Practices for Using Decorators

- ✅ Use `functools.wraps(func)` to preserve function metadata.
- ✅ Keep decorators small and focused.
- ✅ Use built-in decorators like `@staticmethod`, `@classmethod`, and `@property`.
- ✅ Test decorators carefully, especially those modifying function behavior.

**Example with `functools.wraps`:**

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function name and docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Real-World Applications of Decorators

- 🔹 **Logging** – Track function calls.
- 🔹 **Performance Monitoring** – Measure execution time.
- 🔹 **Caching** – Speed up repeated function calls.
- 🔹 **Access Control** – Restrict user actions based on roles.
- 🔹 **API Rate Limiting** – Prevent excessive requests.
- 🔹 **Data Validation** – Ensure input correctness.

---

## Conclusion

Decorators enhance the functionality of functions in an elegant and reusable way. Mastering decorators will help you write cleaner, more efficient, and modular Python code. 🚀
