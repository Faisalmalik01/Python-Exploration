# Implement a decorator that caches the return value of a function, so that when its called with the same argumnets, the cached value is returned instead of re_executing the function.

import time  

# Decorator to cache the return value of a function
def cache(func):
    cache_value = {}  # Dictionary to store cached results
    print("Initial cache:", cache_value)  # Print initial cache (empty)

    def wrapper(*args):
        # If the result for these arguments is already cached, return it
        if args in cache_value:
            print(f"Cache hit for {args}: {cache_value[args]}")  # Log cache hit
            return cache_value[args]
        
        # If not cached, compute the result
        result = func(*args)  # Call the original function
        cache_value[args] = result  # Cache the result
        print(f"Cache miss for {args}: {result}")  # Log cache miss
        return result  # Return the computed result

    return wrapper  # Return the wrapper function

# Apply the cache decorator to the function
@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate a time-consuming operation
    return a + b  # Return the sum of a and b

# Test the decorated function
print(long_running_function(2, 3))  # First call (cache miss)
print(long_running_function(2, 3))  # Second call (cache hit)
print(long_running_function(4, 5))  # Third call (cache miss)