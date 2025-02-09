# Print the multiplication table of a number up to 10, but skip the fifth iteration.

num = input("Enter a number: ")
num = int(num)

for i in range(1, 11):
    if i == 5:
        continue # skip the fifth iteration
    print(f"{num} x {i} = {num * i}")

