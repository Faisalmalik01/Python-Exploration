# Loops in Python

## Introduction
Loops are used in Python to execute a block of code multiple times. Python supports two main types of loops:
- **for loop**: Iterates over a sequence (like lists, tuples, strings, dictionaries, etc.).
- **while loop**: Repeats as long as a condition remains true.

---

## 1. `for` Loop

### Syntax:
```python
for variable in iterable:
    # Code block to execute
```

### Example:
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```
**Output:**
```
1
2
3
4
5
```

### Using `range()` in a `for` loop:
```python
for i in range(5):  # Iterates from 0 to 4
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## 2. `while` Loop

### Syntax:
```python
while condition:
    # Code block to execute
```

### Example:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

**Output:**
```
0
1
2
3
4
```

---

## 3. Loop Control Statements

### `break` Statement
Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
**Output:**
```
0
1
2
3
4
```

### `continue` Statement
Skips the current iteration and continues with the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**
```
0
1
3
4
```

### `else` Clause in Loops
The `else` clause executes if the loop completes normally (without `break`).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed successfully!")
```

**Output:**
```
0
1
2
Loop completed successfully!
```

---

## 4. Looping Techniques

### Looping over Dictionaries
```python
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(key, "->", value)
```

### Looping with `enumerate()`
```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)
```

---

## 5. List Comprehension (Alternative to Loops)
```python
squares = [x**2 for x in range(5)]
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16]
```
