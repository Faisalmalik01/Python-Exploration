# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self._model = model

    
class ElectricCar(Car):  # ElectricCar class (for demonstration)
    def __init__(self, brand, model):
        super().__init__(brand, model)



my_tesla = Car("Tesla", "Model S") 
my_leaf = ElectricCar("Nissan", "Leaf") 


print(f"Is my_tesla an instance of Car? {isinstance(my_tesla, Car)}")  

print(f"Is my_tesla an instance of ElectricCar? {isinstance(my_tesla, ElectricCar)}") 

print(f"Is my_leaf an instance of Car? {isinstance(my_leaf, Car)}")  # Output: True (because ElectricCar inherits from Car)

print(f"Is my_leaf an instance of ElectricCar? {isinstance(my_leaf, ElectricCar)}")  # Output: True


my_regular_car = Car("Toyota", "Camry")

print(f"Is my_regular_car an instance of Car? {isinstance(my_regular_car, Car)}") # Output: True
print(f"Is my_regular_car an instance of ElectricCar? {isinstance(my_regular_car, ElectricCar)}") # Output: False