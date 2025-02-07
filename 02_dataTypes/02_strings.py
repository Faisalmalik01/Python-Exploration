# Strings in Python

# Creating Strings
print("HelloWorld")
print('HelloWorld')
print("""HelloWorld""")

# Assigning Strings to Variables
coffee = "Cappuccino"
print(coffee)

# Updating Strings
coffee = "coldCoffee"
print(coffee)

# Accessing Characters
first_char = coffee[0]
print(first_char)  # Output: 'c'

# String Slicing
slice_coffee = coffee[0:4]
print(slice_coffee)  # Output: 'cold'

# Negative Indexing
print(coffee[-1])  # Output: 'e'

# String Operations
num_list = "0123456789"
print(num_list[:])      # Full string
print(num_list[3:])     # From index 3 to end
print(num_list[:7])     # From start to index 6
print(num_list[0:7:2])  # Step slicing

# String Methods
print(coffee.lower())  # Lowercase
print(coffee.upper())  # Uppercase

coffee = "  cold coffee  "
print(coffee.strip())  # Trim spaces

# Replacing in Strings
tea = "Lemon Tea"
print(tea.replace("Lemon", "Ginger"))

# Splitting Strings
tea = "Lemon, Ginger, Mint"
print(tea.split(", "))  # ['Lemon', 'Ginger', 'Mint']

# Finding Substrings
print(tea.find("Tea"))   # Position of 'Tea'
print(tea.count("Tea"))  # Count occurrences of 'Tea'

# String Formatting
quantity = 2
tea_type = "Lemon"
order = "I ordered {} cups of {} tea".format(quantity, tea_type)
print(order)

# Joining Strings
tea_variety = ["Lemon", "Masala", "Ginger"]
print(", ".join(tea_variety))

# String Length
tea = "Lemon Tea"
print(len(tea))

# Iterating through a String
for letter in tea:
    print(letter)

# Escape Characters
tea = "He said, \"Lemon Tea is awesome\" "
print(tea)

# Raw Strings
tea = r"lemon\nTea"
print(tea)  # Prints raw string with \n
# Checking Substring Presence
tea = "Mint Tea"
print("Mint" in tea)  # True