# calculate the factorial of a number using a while loop.
#Factorial of a number is the product of all positive integers less than or equal to that number.
#For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

num = input("Enter a number: ")
num = int(num)

factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(f"The factorial is {factorial}")

