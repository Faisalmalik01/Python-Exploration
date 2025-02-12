"""
Python Scope and Closures

This script demonstrates:
1. Global vs Local Scope
2. Using the `global` keyword (not recommended in most cases)
3. Nested Functions and Closures
4. Practical Example of Closures with Power Functions
"""


global_username = "admin"  # Global variable

def show_username():
    local_username = "Faisal"  # Local variable
    print(local_username)  # Output: Faisal

print(global_username)  # Output: admin (Global scope)
show_username()


# Using the `global` Keyword (NOT recommended)
global_counter = 10  # Global variable

def modify_global_variable():
    global global_counter  # Declaring global
    global_counter = 20  # Modifying global variable

modify_global_variable()
print(global_counter)  # Output: 20


# Nested Functions and Closures
def outer_function():
    greeting = "Hello"  # Variable inside enclosing function

    def inner_function():
        print(greeting)  # Accessing variable from outer function

    return inner_function

closure_instance = outer_function()
closure_instance()  # Output: Hello


# Practical Example: Power Function Using Closures
def power_function(exponent):
    """ Returns a function that raises numbers to the given exponent """
    def calculate_power(base):
        return base ** exponent  # base^exponent

    return calculate_power  # Returns a function

# Creating specific power functions using closures
square_function = power_function(2)
cube_function = power_function(3)

print(square_function(4))  # Output: 16 (4^2)
print(cube_function(4))    # Output: 64 (4^3)
