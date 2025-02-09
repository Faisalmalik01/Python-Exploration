# Calculate the sum of even up to a given number

num = input("Enter a number: ")
num = int(num)

sum_even = 0
for i in range(0, num + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers up to {num} is {sum_even}")

