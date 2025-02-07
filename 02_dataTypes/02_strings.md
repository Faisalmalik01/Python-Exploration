# Strings in Python

## 1. Introduction to Strings
Strings in Python are sequences of characters enclosed within single (`'`), double (`"`), or triple (`'''` or `"""`) quotes.

'HelloWorld' → 'HelloWorld'
"HelloWorld" → 'HelloWorld'
"""HelloWorld""" → 'HelloWorld'

2. Assigning Strings to Variables

coffee = "Cappuccino"
print(coffee)
# Output: Cappuccino

3. String Immutability

Strings in Python are immutable, meaning their content cannot be changed after assignment. However, they can be reassigned.

coffee = "coldCoffee"
print(coffee)
# Output: coldCoffee

4. Accessing Characters in Strings

Characters in a string can be accessed using indexing.

first_char = coffee[0]
print(first_char)
# Output: c

Negative indexing allows access from the end of the string.

print(coffee[-1])
# Output: e

5. Slicing Strings

String slicing allows extracting portions of a string using [start:end] or [start:end:step].

slice_coffee = coffee[0:4]
print(slice_coffee)
# Output: cold

Examples with step:

num_list = "0123456789"
print(num_list[:])
# Output: 0123456789
print(num_list[3:])
# Output: 3456789
print(num_list[:7])
# Output: 0123456
print(num_list[0:7:2])
# Output: 0246
print(num_list[0:7:3])
# Output: 036

6. String Methods

Python provides several built-in string methods.
Convert Case

print(coffee.lower())
# Output: coldcoffee
print(coffee.upper())
# Output: COLDCOFFEE

Stripping Spaces

coffee = "  cold coffee  "
print(coffee.strip())
# Output: cold coffee

Replacing Substrings

tea = "Lemon Tea"
print(tea.replace("Lemon", "Ginger"))
# Output: Ginger Tea

Splitting Strings

tea = "Lemon, Ginger, Mint"
print(tea.split())
# Output: ['Lemon,', 'Ginger,', 'Mint']
print(tea.split(", "))
# Output: ['Lemon', 'Ginger', 'Mint']

Finding Substrings

tea = "Ginger Tea"
print(tea.find("Tea"))
# Output: 7
print(tea.find("tea"))
# Output: -1  # Case-sensitive search

Counting Substrings

tea = "Ginger Tea Tea Tea"
print(tea.count("Tea"))
# Output: 3

7. String Formatting

Using .format():

tea_type = "Lemon"
quantity = 2
order = "I ordered {} cups of {} tea"
print(order.format(quantity, tea_type))
# Output: I ordered 2 cups of Lemon tea

8. Joining Strings

The .join() method joins elements of an iterable into a single string.

tea_variety = ["Lemon", "Masala", "Ginger"]
print(" ".join(tea_variety))
# Output: Lemon Masala Ginger
print(", ".join(tea_variety))
# Output: Lemon, Masala, Ginger

9. String Length

tea = "Lemon Tea"
print(len(tea))
# Output: 9

10. Iterating Over a String

for letter in tea:
    print(letter)
# Output: 
# L
# e
# m
# o
# n
# T
# e
# a

11. Escape Characters

Escape characters allow inserting special characters in strings.

tea = "He said, \"Lemon Tea is awesome\""
print(tea)
# Output: He said, "Lemon Tea is awesome"

Newline \n:

tea = "lemon\nTea"
print(tea)
# Output: 
# lemon
# Tea

Raw Strings r"":

tea = r"lemon\nTea"
print(tea)
# Output: lemon\\nTea

12. Checking Substrings

tea = "Mint Tea"
print("Miint" in tea)
# Output: False
print("Mint" in tea)  
# Output: True