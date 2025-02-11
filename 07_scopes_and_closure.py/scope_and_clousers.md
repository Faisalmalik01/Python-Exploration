 
# Scope and Closures in Python

## 📌 Introduction  
Understanding **scope** and **closures** is crucial in Python, as they define how and where variables are accessible throughout a program.  

---

## 🔹 Scope in Python  
In Python, **scope** refers to the region where a variable is accessible. Python follows the **LEGB Rule** (Local → Enclosing → Global → Built-in) to resolve variable names.


1️⃣ Local (L) → Variables inside a function.
2️⃣ Enclosing (E) → Variables from an outer function (for nested functions).
3️⃣ Global (G) → Variables at the top level of a script/module.
4️⃣ Built-in (B) → Predefined Python functions like print(), len(), etc.

### 1️⃣ Global Scope  
A variable declared outside a function is **global** and can be accessed anywhere in the file.  

```python
username = "admin"  # Global variable

def display():
    username = "Faisal"  # Local variable (Function Scope)
    print(username)

print(username)  # Output: admin
display()        # Output: Faisal
```

🔹 **Global variables** remain accessible throughout the script but should be used cautiously inside functions.  

---

### 2️⃣ Local Scope  
Variables defined inside a function are **local** to that function and cannot be accessed outside.  

```python
def greet():
    message = "Hello, World!"  # Local scope
    print(message)

greet()  # Output: Hello, World!

# print(message)  # ❌ Error: 'message' is not defined outside the function.
```

---

### 3️⃣ Enclosing Scope (Nonlocal)  
Nested functions can access variables from their enclosing function (but not modify them directly unless declared `nonlocal`).  

```python
def outer_function():
    outer_var = "Outer Scope"

    def inner_function():
        print(outer_var)  # Accessing outer function's variable

    inner_function()

outer_function()  # Output: Outer Scope
```

To modify an **enclosing scope variable**, use `nonlocal`:

```python
def counter():
    count = 0  # Enclosing scope

    def increment():
        nonlocal count  # Modifies the enclosing variable
        count += 1
        return count

    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2
```

---

### 4️⃣ Built-in Scope  
Python has built-in functions and constants that are always available, such as `print()`, `len()`, `range()`, etc.  

```python
print(len("Python"))  # Output: 6  (len() is a built-in function)
```

---

## ⚠️ Global Keyword (Modifying Global Variables)  
Although global variables can be accessed inside a function, they cannot be modified directly **unless** declared `global`.  

```python
x = 99  # Global variable

def modify_global():
    global x  # Declaring x as global
    x = 12

modify_global()
print(x)  # Output: 12
```

🔴 **Note:** Changing global variables inside functions is **not recommended** due to potential unintended side effects.

---

## 🔹 Closures in Python  
A **closure** is a function that remembers the values from its enclosing scope, even after the outer function has finished executing.

### 🔥 Example 1: Function Returning a Function  

```python
def power_function(exponent):
    def actual_power(base):
        return base ** exponent  # Accessing 'exponent' from outer scope

    return actual_power  # Returns function reference

square = power_function(2)
cube = power_function(3)

print(square(4))  # Output: 16 (4^2)
print(cube(2))    # Output: 8  (2^3)
```

✅ Here, `actual_power()` is a **closure** because it remembers the `exponent` variable from its enclosing function (`power_function`).

---

### 🔥 Example 2: Maintaining State  
Closures are useful for maintaining state across multiple function calls.

```python
def counter():
    count = 0  # Enclosing scope variable

    def increment():
        nonlocal count  # Retains previous value
        count += 1
        return count

    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = counter()  # Creates a new independent counter
print(counter2())  # Output: 1
```

---

## ✅ When to Use Closures?  
Closures are useful when:  
✔️ You want to retain state information without using global variables.  
✔️ You need to create **function factories** (like in decorators).  
✔️ You want to create flexible and reusable functions.

---

## 🔥 Key Takeaways  
✅ Python uses **LEGB rule** for variable scope resolution.  
✅ Use **local variables** whenever possible to avoid unwanted side effects.  
✅ Use `nonlocal` when modifying variables in an **enclosing function**.  
✅ Closures allow a function to remember variables from its **enclosing scope** even after execution.  
✅ Be cautious when modifying global variables using `global`.

---

## 🔗 Additional Resources  
📌 Python Official Docs: [Scope & Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)  
📌 Understanding Closures in Python: [Real Python Guide](https://realpython.com/inner-functions-what-are-they-good-for/)  

---
