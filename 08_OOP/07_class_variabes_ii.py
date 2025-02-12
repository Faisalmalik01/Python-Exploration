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

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return f"{self.get_brand()} {self.model} (Battery: {self.battery_size})"




# Create a list to store all car instances
cars = []


cars.append(Car("Tesla", "Model S"))
cars.append(Car("Toyota", "Corolla"))
cars.append(Car("Ford", "Mustang"))
cars.append(ElectricCar("Tesla", "Model 3", "75kWh"))


print("Details of all cars:")
for car in cars:
    print(car.full_name())

# Print the total number of cars created
print("\nTotal number of cars created:", Car.number_of_cars)