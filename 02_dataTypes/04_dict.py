# Creating a dictionary
dictionary = {"name": "Alice", "age": 25, "city": "New York"}
print(dictionary)

# Accessing values
print(dictionary["name"])  # Output: Alice
print(dictionary.get("age"))  # Output: 25
print(dictionary.get("country", "Not Found"))  # Output: Not Found

# Modifying values
dictionary["age"] = 26
print(dictionary)

# Adding new key-value pairs
dictionary["gender"] = "Female"
print(dictionary)

# Removing key-value pairs
del dictionary["city"]
print(dictionary)

# Using pop() method
age = dictionary.pop("age")
print("Removed Age:", age)
print(dictionary)

# Using popitem() method (removes last inserted item)
dictionary.popitem()
print(dictionary)

# Iterating over dictionary
for key in dictionary:
    print(key, dictionary[key])

# Using items() to iterate over key-value pairs
for key, value in dictionary.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Checking if a key exists
if "name" in dictionary:
    print("Name exists in dictionary")

# Getting dictionary length
print(len(dictionary))

# Copying a dictionary
dict_copy = dictionary.copy()
print(dict_copy)

# Merging two dictionaries
extra_info = {"hobby": "Reading", "language": "English"}
dictionary.update(extra_info)
print(dictionary)

# Clearing a dictionary
dictionary.clear()
print(dictionary)  # Output: {}

# Nested dictionary
nested_dict = {
    "student1": {"name": "Alice", "age": 22},
    "student2": {"name": "Bob", "age": 24}
}
print(nested_dict)
print(nested_dict["student1"]["name"])  # Output: Alice

# Creating a dictionary from keys
default_values = dict.fromkeys(["a", "b", "c"], 0)
print(default_values)
