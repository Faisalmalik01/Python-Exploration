# 📌 Functions in Python

## 🔹 What is a Function?
A **function** is a block of reusable code designed to perform a specific task. Functions help make code **modular, readable, and reusable**.

### **Types of Functions in Python**
1. **Built-in Functions** (e.g., `print()`, `len()`, `sum()`).
2. **User-defined Functions** (functions created by the user).
3. **Lambda (Anonymous) Functions** (one-liner functions).
4. **Recursive Functions** (functions that call themselves).

---

## **1️⃣ Defining and Calling a Function**
A function is defined using the `def` keyword, followed by a function name, parentheses `()`, and a colon `:`.

### **Example: Function to Calculate the Square of a Number**
```python
def square(num):
    return num * num

print(square(4))  # Output: 16
```

### **Example: Function that Asks User for a Number and Returns the Square**
```python
def square_input():
    num = int(input("Enter a number: "))
    return num * num

print(square_input())
```

---

## **2️⃣ Functions with Multiple Parameters**
A function can take multiple parameters as input.

### **Example: Function to Add Two Numbers**
```python
def add(num1, num2):
    return num1 + num2

print(add(4, 5))  # Output: 9
```

### **Example: Function to Find Greater of Two Numbers**
```python
def greater(num1, num2):
    return num1 if num1 > num2 else num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(greater(num1, num2))
```

---

## **3️⃣ Functions That Work with Different Data Types**
### **Example: Function to Multiply Integers and Strings**
```python
def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 5))       # Output: 20
print(multiply("Hello", 3)) # Output: HelloHelloHello
```

---

## **4️⃣ Functions Returning Multiple Values**
A function can return multiple values as a tuple.

### **Example: Area & Circumference of a Circle**
```python
import math

def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return round(area), round(circumference)

radius = int(input("Enter radius: "))
area, circumference = circle(radius)
print(f"Area: {area}, Circumference: {circumference}")
```

---

## **5️⃣ Default Parameters in Functions**
### **Example: Function with Default Parameter**
```python
def greet(name="User"):
    return f"Hello, {name}!"

print(greet("Faisal"))  # Output: Hello, Faisal!
print(greet())          # Output: Hello, User!
```

---

## **6️⃣ Lambda (Anonymous) Functions**
A **lambda function** is a small anonymous function that can have any number of arguments but only one expression.

### **Example: Lambda Function to Compute Cube**
```python
cube = lambda x: x ** 3
print(cube(3))  # Output: 27
```

---

## **7️⃣ Functions with Variable Number of Arguments (`*args`)**
A function can accept **any number of positional arguments** using `*args`.

### **Example: Sum of All Arguments**
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

---

## **8️⃣ Functions with Keyword Arguments (`**kwargs`)**
A function can accept **any number of named arguments** using `**kwargs`.

### **Example: Print Key-Value Pairs**
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Faisal", power="Coding", enemy="Procrastination")
```

---

## **9️⃣ Generator Functions (`yield`)**
A **generator function** uses `yield` instead of `return` to produce a sequence of values.

### **Example: Generate Even Numbers**
```python
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i 

for num in even_numbers(10):
    print(num)
```

---

## **🔟 Recursive Functions**
A **recursive function** is a function that calls itself until a base condition is met.

### **Example: Factorial Using Recursion**
```python
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))  # Output: 120
```

---

## **🚀 Conclusion**
- Functions help **break down complex problems** into smaller, manageable parts.
- Python supports **default arguments, lambda functions, recursion, and generators**.
- Using `*args` and `**kwargs` allows for **flexibility in function parameters**.
