
# Creating tuples
empty_tuple = ()
single_element = (5,)  # Single element tuple requires a comma
numbers = (10, 20, 30)
fruits = ("apple", "banana", "cherry")
packed_tuple = 1, 2, 3, "Python"  # Tuple without parentheses

print(numbers)
print(fruits)
print(packed_tuple)

# Accessing elements using indexing
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Slicing a tuple
tuple_example = (1, 2, 3, 4, 5)
print(tuple_example[1:4])  # Output: (2, 3, 4)

# Tuple immutability
tuple_example = (10, 20, 30)
# tuple_example[1] = 50  # Uncommenting this will raise TypeError

# Concatenation and repetition
tuple1 = ("a", "b")
tuple2 = ("c", "d")
print(tuple1 + tuple2)  # ('a', 'b', 'c', 'd')
print(numbers * 3)  # (10, 20, 30, 10, 20, 30, 10, 20, 30)

# Membership test
print("banana" in fruits)  # True
print("grape" in fruits)  # False

# Tuple methods
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))  # Output: 3
print(numbers.index(3))  # Output: 3

# Packing and unpacking
tuple_packed = "Python", 3.8, "Programming"
name, version, category = tuple_packed
print(name)    # Python
print(version) # 3.8
print(category) # Programming

# Nested tuples
nested_tuple = ("Python", (1, 2, 3), ["a", "b"])
print(nested_tuple[1][1])  # Output: 2

# Creating a tuple from a list
list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)
print(tuple_from_list)

# Converting a tuple to a list
tuple_data = ("a", "b", "c")
list_from_tuple = list(tuple_data)
print(list_from_tuple)
