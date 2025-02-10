# Generate a function that yeilds even numbers up to a given number.

# yeild is a keyword in Python that is used to return a generator object.
# A generator is a special type of iterator that generates values on the fly.
# Generators are used to create iterators, but with a different approach.
# Generators are simple functions that return an iterable set of items, one at a time, in a special way.


def even_numbers(n):
    for i in range(2, n+1, 2):
        print(i)

even_numbers(10)


def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i 

for i in even_numbers(10):
    print(i)
