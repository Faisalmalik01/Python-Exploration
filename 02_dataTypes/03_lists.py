
# Creating a list
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)

# Accessing elements
print(tea_varieties[0])  # First element
print(tea_varieties[-1]) # Last element
print(tea_varieties[1:3])  # Slicing
print(tea_varieties[2:])  # Slicing from index 2 onward
print(tea_varieties[3])  # Accessing element at index 3

# Modifying lists
tea_varieties[3] = "Herbal"
print(tea_varieties)

# Slicing and replacing elements
tea_varieties[1:2] = "Lemon"
print(tea_varieties)
tea_varieties = ["Black", "Green", "Oolong", "White"]  # Resetting list
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)
tea_varieties[1:3] = ["Green", "Masala"]
print(tea_varieties)

# Inserting elements
tea_varieties[1:1] = ["Test", "Test"]
print(tea_varieties)

# Removing elements
tea_varieties.pop()  # Removes last element
print(tea_varieties)
tea_varieties.remove("Green")  # Removes 'Green'
print(tea_varieties)
tea_varieties.insert(1, "Green")  # Inserting 'Green' back
print(tea_varieties)

del tea_varieties[0]  # Removes first element
print(tea_varieties)
tea_varieties[1:3] = []  # Removes elements from index 1 to 2
print(tea_varieties)

# Iterating over lists
for tea in tea_varieties:
    print(tea)

for tea in tea_varieties:
    print(tea, end="-")
print()

# Checking membership
if "Oolong" in tea_varieties:
    print("I have oolong tea")

tea_varieties.append("Oolong")  # Adding 'Oolong' back
print(tea_varieties)
if "Oolong" in tea_varieties:
    print("I have oolong tea")

# Copying lists
tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy.append("Lemon")
print(tea_varieties)
print(tea_varieties_copy)

# Using range with lists
print(range(10))  # Printing range object
print(list(range(10)))  # Converting range to list

# List comprehensions
squared_nums = [x**2 for x in range(10)]
print(squared_nums)
cube_nums = [y**3 for y in range(5)]
print(cube_nums)
