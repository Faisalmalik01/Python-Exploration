# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance. 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self._model = model   # Protected attribute

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self._model

    def display_info(self):
        return f"Car: {self.get_brand()} {self.get_model()}"


class Battery:
    def __init__(self, capacity_kwh):
        self.capacity_kwh = capacity_kwh

    def battery_info(self):
        return f"Battery Capacity: {self.capacity_kwh} kWh"


class Engine:
    def __init__(self, power_hp):
        self.power_hp = power_hp

    def engine_info(self):
        return f"Engine Power: {self.power_hp} HP"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity, engine_power):
        super().__init__(brand, model)
        self.battery = Battery(battery_capacity)  # Composition
        self.engine = Engine(engine_power)        # Composition

    def display_info(self):
        car_info = super().display_info()
        battery_info = self.battery.battery_info()
        engine_info = self.engine.engine_info()
        return f"{car_info}\n{battery_info}\n{engine_info}"



my_new_tesla = ElectricCar("Tesla", "Model S", 100, 500)

print(my_new_tesla.display_info())