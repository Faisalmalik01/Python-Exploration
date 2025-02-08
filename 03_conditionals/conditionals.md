# Python Conditionals

## Introduction  
Conditionals in Python allow us to execute different blocks of code based on conditions. They enable decision-making in programs, making them more dynamic and interactive.

## Conditional Statements in Python  
Python provides the following conditional statements:  

1. **if Statement**  
2. **if-else Statement**  
3. **if-elif-else Statement**  
4. **Nested if Statements**  
5. **Ternary Operator (Conditional Expression)**  

---

## 1. The `if` Statement  
The `if` statement executes a block of code only if the given condition evaluates to `True`.  

### **Syntax:**  
```python
if condition:
    # Code to execute if the condition is True
```

### **Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

---

## 2. The `if-else` Statement  
The `if-else` statement provides an alternative block of code when the condition is `False`.  

### **Syntax:**
```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

### **Example:**
```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

## 3. The `if-elif-else` Statement  
The `if-elif-else` statement allows multiple conditions to be checked sequentially.  

### **Syntax:**
```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition2 is True
else:
    # Code if none of the conditions are True
```

### **Example:**
```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
```

---

## 4. Nested `if` Statements  
An `if` statement inside another `if` statement is called a **nested if statement**. It allows checking multiple conditions at different levels.  

### **Syntax:**
```python
if condition1:
    if condition2:
        # Code to execute if both conditions are True
```

### **Example:**
```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("You must be a citizen to vote.")
```

---

## 5. The Ternary Operator (Conditional Expression)  
Python provides a shorthand way to write an `if-else` statement using the **ternary operator**.  

### **Syntax:**
```python
value_if_true if condition else value_if_false
```

### **Example:**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```
> Output: `Adult`

---

## Best Practices for Writing Conditionals  

- **Use meaningful variable names:**  
  ```python
  is_raining = True  # Instead of 'a' or 'flag'
  ```

- **Avoid unnecessary conditions:**  
  ```python
  if is_raining:  # Instead of 'if is_raining == True'
      print("Take an umbrella.")
  ```

- **Keep conditions simple and readable:**  
  ```python
  if 18 <= age <= 65:  # Instead of 'if age >= 18 and age <= 65'
  ```

- **Use the ternary operator for short conditions:**  
  ```python
  status = "Eligible" if age >= 18 else "Not Eligible"
  ```

- **Use `elif` instead of multiple `if` statements:**  
  ```python
  if marks >= 90:
      print("A")
  elif marks >= 80:
      print("B")  # Instead of using multiple 'if' conditions
  ```

---

## Conclusion  
Conditional statements are fundamental in Python programming. They allow us to implement decision-making logic efficiently. Understanding `if`, `if-else`, `if-elif-else`, and nested conditionals will help you write more structured and efficient code.

---
