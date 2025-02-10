# Write a function that greets a user. if no name is provided, it should greet with a default name.

def greet(name = "User"):
    return f"Hello, {name}!"

print(greet("Faisal"))
print(greet())

# Write a function that takes two numbers as input and returns the sum of the two numbers. If no numbers are provided, it should return the sum of 0 and 0.

def sum(num1 = 0, num2 = 0):
    return num1 + num2

print(sum(4, 5))
print(sum())


