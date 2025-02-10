# Create a recursive function that calculates the factorial of a number.
# Recursive function is a function that calls itself during its execution until a base condition is met to return the result.
# Factorial of a number is the product of all positive integers less than or equal to that number.
# For example, the factorial of 5 is 5*4*3*2*1 = 120.

def factorial(num):
    if num == 1: # Base condition
        return 1
    else:
        return num * factorial(num - 1) # Recursive call

num = int(input("Enter a number: "))
print(factorial(num))

# Write a recursive function to calculate the sum of natural numbers.

def sum_natural(num):
    if num == 1:
        return 1
    else:
        return num + sum_natural(num - 1)

num = int(input("Enter a number: "))
print(sum_natural(num))

# Write a recursive function to calculate the nth Fibonacci number.
# Fibonacci series is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
# For example, the Fibonacci series up to 10 is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter a number: "))
print(fibonacci(num))

