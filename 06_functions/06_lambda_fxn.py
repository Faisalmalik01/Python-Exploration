# Create a lambda function to compute the cube of a number.

#A lambda function in Python is a small, anonymous function defined using the lambda keyword. 
# Lambda functions can have any number of arguments but only one expression. 
# They are syntactically restricted to a single expression. 
# It is used when you require a nameless function for a short period of time.


def cube(num):
    return num ** 3

print(cube(3))

# The above function can be written as a lambda function as shown below:
cube = lambda x: x ** 3
print(cube(3)) 


# Write a lambda function to add two numbers.

add = lambda x, y: x + y
print(add(4, 5))

# Write a lambda function to determine if a number is even.

is_even = lambda x: x % 2 == 0
num = int(input("Enter a number: "))
print(is_even(num))

