# Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        # Convert positional arguments to a string
        args_value = ', '.join(str(arg) for arg in args)
        # Convert keyword arguments to a string
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        # Print function name and arguments
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        # Call the original function with its arguments
        return func(*args, **kwargs)
    return wrapper  # Return the wrapper function

# Apply the debug decorator to hello
@debug
def hello():
    print("hello")

# Apply the debug decorator to greet
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# Call the decorated functions
hello()
greet("Faisal", greeting="yo")
greet("Grace")