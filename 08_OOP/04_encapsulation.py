# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    # Getter method for brand
    def get_brand(self):
        return self.__brand + "!"

    # Setter method for brand
    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} {self.model}"


# Creating an instance of Car
my_car = Car("Tesla", "Model S")

# Accessing the private attribute directly will raise an error
# print(my_car.__brand)  # This will raise an AttributeError

# Using the getter method to access the private attribute
print(my_car.get_brand())  # Output: Tesla!

# Using the setter method to modify the private attribute
my_car.set_brand("Toyota")
print(my_car.get_brand())  # Output: Toyota!

# Printing the full name of the car
print(my_car.full_name())  # Output: Toyota Model S