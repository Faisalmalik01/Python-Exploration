# Demonstrate Polymorphism by defining a mothod fuel_type in both Car and ElectricCar but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


# Creating instances
petrol_car = Car("Tata", "Safari")
electric_car = ElectricCar("Tesla", "Model S", "85kWh")

# Demonstrating polymorphism
print(petrol_car.full_name())         
print(petrol_car.fuel_type())         

print(electric_car.full_name())       
print(electric_car.fuel_type())       