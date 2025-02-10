# Create a function that copies any number of keyword arguments and prints them in key:value format.

# **kwargs is used to pass a keyworded, variable-length argument list.

def print_kwargs(name, power):
    print(f"Name: {name}, Power: {power}")

print_kwargs(name="Superman", power="Flying")
print_kwargs(power="Flying", name="Superman")

# print_kwargs(name="Batman", power="Rich", enemy="Joker") # This will throw an error as the function is not designed to accept extra keyword arguments.

#solution
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_kwargs(name="Faisal", power="Coding")
print_kwargs(name="Faisal", power="Coding", enemy="Procrastination")