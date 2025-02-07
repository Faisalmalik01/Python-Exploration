# Python Lists

## Introduction to Lists
Lists in Python are ordered, mutable collections that can store items of different data types. They are one of the most commonly used data structures in Python.

## Creating Lists
Lists are created using square brackets `[]`:
```python
tea_varieties = ["Black", "Green", "Oolong", "White"]
```

## Accessing Elements
Elements in a list can be accessed using indexing:
- **Positive Indexing**: Starts from 0.
- **Negative Indexing**: Starts from -1 (last element).
- **Slicing**: Extracts a portion of the list.

Examples:
```python
print(tea_varieties[0])  # First element
print(tea_varieties[-1]) # Last element
print(tea_varieties[1:3])  # Elements from index 1 to 2
print(tea_varieties[2:])  # Elements from index 2 onward
```

## Modifying Lists
Lists are mutable, meaning elements can be changed:
```python
tea_varieties[3] = "Herbal"
print(tea_varieties)
```

## Slicing and Replacing Elements
Replacing a slice modifies multiple elements:
```python
tea_varieties[1:2] = ["Lemon"]  # Replaces one element
tea_varieties[1:3] = ["Green", "Masala"]  # Replaces two elements
```

## Adding Elements
- **`append()`**: Adds an element to the end.
- **`insert()`**: Inserts an element at a specific index.
```python
tea_varieties.append("Oolong")
tea_varieties.insert(1, "Green")
```

## Removing Elements
- **`pop()`**: Removes and returns the last element (or a specified index).
- **`remove()`**: Removes the first occurrence of a specified element.
- **`del`**: Deletes an element or slice.
```python
tea_varieties.pop()
tea_varieties.remove("Green")
del tea_varieties[0]
```

## Checking Membership
Use the `in` keyword to check if an element exists:
```python
if "Oolong" in tea_varieties:
    print("I have oolong tea")
```

## Iterating Over Lists
Using a loop to iterate through elements:
```python
for tea in tea_varieties:
    print(tea)
```

## Copying Lists
Copying lists creates a new reference:
```python
tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy.append("Lemon")
```

## Using Range with Lists
Creating lists from a range:
```python
print(list(range(10)))
```

## List Comprehensions
List comprehensions provide a concise way to create lists:
```python
squared_nums = [x**2 for x in range(10)]
cube_nums = [y**3 for y in range(5)]
```