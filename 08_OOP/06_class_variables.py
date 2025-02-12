# Add class variable to Car that keeps track of the number of cars created.

class Car:
    
    number_of_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model

        # Increment the class variable whenever a new instance is created
        Car.number_of_cars += 1

    
    def get_brand(self):
        return self.__brand + "!"

    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

# Creating instances of Car
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")
car3 = Car("Ford", "Mustang")

# Accessing the class variable to check the number of cars created
print("Number of cars created:", Car.number_of_cars)  


