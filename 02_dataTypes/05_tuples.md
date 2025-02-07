# Python Tuples -

## Introduction to Tuples
A **tuple** is an immutable and ordered collection of elements. Tuples are similar to lists but cannot be modified after creation. They are defined using parentheses `()` and can contain elements of different data types.

### Syntax
```python
my_tuple = (1, 2, 3, "apple", True)
```

## Characteristics of Tuples
- **Immutable**: Elements cannot be changed, added, or removed after the tuple is created.
- **Ordered**: Elements have a fixed sequence.
- **Allows Duplicates**: Tuples can contain duplicate values.
- **Supports Multiple Data Types**: Elements can be of any data type.

## Creating Tuples
### 1. Empty Tuple
```python
empty_tuple = ()
```

### 2. Tuple with Elements
```python
numbers = (10, 20, 30)
fruits = ("apple", "banana", "cherry")
```

### 3. Tuple Without Parentheses (Tuple Packing)
```python
packed_tuple = 1, 2, 3, "Python"
```

### 4. Single Element Tuple (Comma is Required)
```python
single_element = (5,)  # Not just (5)
```

## Accessing Tuple Elements
### 1. Indexing
Tuples use **zero-based indexing**.
```python
tuple_example = ("a", "b", "c")
print(tuple_example[0])  # Output: 'a'
print(tuple_example[-1]) # Output: 'c' (negative indexing)
```

### 2. Slicing
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[:3])   # Output: (1, 2, 3)
print(my_tuple[2:])   # Output: (3, 4, 5)
```

## Tuple Immutability
Tuples **cannot** be modified after creation.
```python
tuple_example = (10, 20, 30)
tuple_example[1] = 50  # TypeError: 'tuple' object does not support item assignment
```

## Tuple Operations
### 1. Concatenation
```python
tuple1 = ("a", "b")
tuple2 = ("c", "d")
result = tuple1 + tuple2
print(result)  # ('a', 'b', 'c', 'd')
```

### 2. Repetition
```python
numbers = (1, 2, 3)
print(numbers * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### 3. Membership Test
```python
my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)  # True
print("grape" in my_tuple)   # False
```

## Tuple Methods
### 1. `count()`
Counts occurrences of an element.
```python
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))  # Output: 3
```

### 2. `index()`
Finds the first occurrence index.
```python
letters = ("a", "b", "c", "a")
print(letters.index("a"))  # Output: 0
```

## Tuple Packing and Unpacking
### 1. Packing
```python
tuple_packed = "Python", 3.8, "Programming"
```

### 2. Unpacking
```python
name, version, category = tuple_packed
print(name)    # Python
print(version) # 3.8
```

## Nested Tuples
Tuples can contain other tuples.
```python
nested_tuple = ("Python", (1, 2, 3), ["a", "b"])
print(nested_tuple[1][1])  # Output: 2
```

## When to Use Tuples
- When data should not be changed.
- To use as dictionary keys (since they are hashable).
- When memory efficiency is needed (tuples are faster than lists).

## Conclusion
Tuples are an essential part of Python, offering an immutable, ordered collection of elements. Their efficiency and immutability make them ideal for situations where data integrity is crucial.

