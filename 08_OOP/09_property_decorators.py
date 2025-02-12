# Use a property decorator in the Car class to make the model attribute read-only. 

class Car:
    def __init__(self, brand, model, battery_size=None):  # battery_size is now optional
        self.__brand = brand
        self.__model = model
        self.battery_size = battery_size 


    def full_name(self):
        name = f"{self.__brand} {self.__model}"
        if self.battery_size:  # Add battery info only if it exists
            name += f" (Battery: {self.battery_size})"
        return name

    @property
    def model(self):
        return self.__model

    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation."



my_car = Car("Tesla", "Model S")
print(my_car.model) 

# my_car.model = "New Model"  # This will now raise an AttributeError: can't set attribute

print(my_car.full_name())


