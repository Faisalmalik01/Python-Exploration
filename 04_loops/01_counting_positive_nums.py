# Given a list of numbers, count how many of them are positive and print the result.

numbers = [1, 2, 3, -1, -2, -3]

count = 0
for num in numbers:
    if num > 0:
        count += 1

print(count)
