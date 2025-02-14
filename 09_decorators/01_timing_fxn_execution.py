# Write a decorator that measures the time of a function takes to execute.
import time  

def timer(func):  # Decorator to measure execution time
    def wrapper(*args, **kwargs):  # Wrapper to replace the original function
        start = time.time()  # Start timing
        result = func(*args, **kwargs)  # Call the original function
        end = time.time()  # End timing
        print(f"{func.__name__} ran in {end - start} seconds")  # Print execution time
        return result  # Return the original function's result
    return wrapper  # Return the wrapper function

@timer  # Apply the timer decorator
def example_function(n):  # Example function to test the decorator
    time.sleep(n)  # Simulate work by sleeping for 'n' seconds

example_function(2)  # Call the decorated function