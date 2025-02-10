# Write a function to calculate and return the square of a number.


def square(num):
    return num * num


print(square(4))

# Write a function to thats asks the user for a number and returns the square of that number.

def square_input():
    num = int(input("Enter a number: "))
    return num * num

print(square_input())

# Write a function that takes two numbers as input and returns the sum of the two numbers.

def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2

print(add())

# Write a function that takes two numbers as input and returns the product of the two numbers.

def multiply():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 * num2

print(multiply())

# Write a function that takes cost price and selling price as input and returns the profit made.

def profit():
    cost_price = int(input("Enter cost price: "))
    selling_price = int(input("Enter selling price: "))
    return selling_price - cost_price


print(profit())

# Write a function that takes marks of a student as input and returns the grade of the student.

def grade():
    marks = int(input("Enter marks: "))
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade())

# Write a function that takes a number as input and returns True if the number is even, False otherwise.

def is_even():
    num = int(input("Enter a number: "))
    return num % 2 == 0
    

print(is_even())


# Write a function that takes a number list as input and returns the sum of all the numbers in the list.

def sum_list():
    num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
    return sum(num_list)

print(sum_list())

