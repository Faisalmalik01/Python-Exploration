# Python Dictionaries 

## Introduction to Dictionaries
A dictionary in Python is an unordered, mutable collection that stores data in key-value pairs. It is defined using curly braces `{}` with keys and their corresponding values separated by a colon `:`.

### Key Features of Dictionaries:
- Stores data in **key-value pairs**.
- Keys must be **unique** and **immutable** (strings, numbers, or tuples).
- Values can be of **any data type**.
- Dictionaries are **unordered** (Python 3.6+ maintains insertion order).
- Dictionaries are **mutable**, meaning they can be changed after creation.

---
## Creating Dictionaries
```python
# Defining a dictionary
chai_types = {"Masala": "spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)
```
Output:
```
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
```

---
## Accessing Dictionary Values
You can access values using **keys**:
```python
print(chai_types["Masala"])  # Direct access
print(chai_types.get("Ginger"))  # Using get() method
print(chai_types.get("Gingery"))  # Returns None if key doesn't exist
```

---
## Modifying Dictionary
```python
chai_types["Green"] = "Fresh"  # Modifying a value
print(chai_types)
```
Output:
```
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
```

---
## Iterating Over a Dictionary
### Iterating Over Keys:
```python
for chai in chai_types:
    print(chai)
```
Output:
```
Masala
Ginger
Green
```

### Iterating Over Key-Value Pairs:
```python
for key, value in chai_types.items():
    print(key, value)
```
Output:
```
Masala spicy
Ginger Zesty
Green Fresh
```

---
## Checking Key Existence
```python
if "Masala" in chai_types:
    print("I have Masala chai")
```
Output:
```
I have Masala chai
```

---
## Dictionary Length
```python
print(len(chai_types))  # Number of key-value pairs
```
Output:
```
3
```

---
## Adding and Removing Elements
### Adding a New Key-Value Pair:
```python
chai_types["Earl Grey"] = "Citrus"
print(chai_types)
```

### Removing an Element:
```python
chai_types.pop("Ginger")
print(chai_types)
```

### Removing the Last Inserted Item:
```python
chai_types.popitem()
print(chai_types)
```

### Deleting a Specific Key:
```python
del chai_types["Green"]
print(chai_types)
```

---
## Copying a Dictionary
```python
chai_types_copy = chai_types.copy()
```

---
## Nested Dictionaries
Dictionaries can contain other dictionaries:
```python
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}
print(tea_shop)
```
Accessing Nested Dictionary Values:
```python
print(tea_shop["chai"]["Ginger"])  # Output: zesty
```

---
## Dictionary Comprehension
```python
squared_num = {x: x**2 for x in range(6)}
print(squared_num)
```
Output:
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---
## Clearing a Dictionary
```python
squared_num.clear()
print(squared_num)  # Output: {}
```

---
## Creating Dictionary from Keys
```python
keys = ["Masala", "Ginger", "Lemon"]
new_dict = dict.fromkeys(keys, "Delicious")
print(new_dict)
```
Output:
```
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
```

---
## Summary
Dictionaries are a powerful data structure in Python that allows efficient key-value storage and retrieval. Understanding their methods and properties can help in solving various programming problems efficiently.

