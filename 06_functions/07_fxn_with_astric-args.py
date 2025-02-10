# Write a function that takes any number of arguments and returns the sum of the arguments.
# Astric (*) is used to pass a variable number of arguments to a function.

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))


def sum_all(*args):
    print(args)
    for i in args:
        print(i)
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))