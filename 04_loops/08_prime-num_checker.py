# Check if a given number is prime or not.
# A prime number is a number greater than 1 that is only divisible by 1 and itself.
# For example, 2, 3, 5, 7, 11, 13, 17, etc.


number = int(input("Enter a number: "))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i == 0):
            is_prime = False
            break


if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

    