# Create a function that takes two parameters and returns the sum of them.

def add(num1, num2):
    return num1 + num2

print(add(4, 5))

# Create a function that takes two parameters from the user and returns the product of them.

def multiply(num1, num2):
    return num1 * num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(multiply(num1, num2))

# Create a function that takes two parameters from the user and returns greater of the two numbers.

def greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(greater(num1, num2))
