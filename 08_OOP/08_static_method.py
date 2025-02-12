# Add a ststic method to the Cars class that returns a general description of car. 

class Vehicle:
    def __init__(self, make, kind, power_source, battery_capacity=None):  # Added battery_capacity as optional
        self._make = make
        self.kind = kind
        self.power_source = power_source
        self.battery_capacity = battery_capacity  # Could be None for non-electric

    # def get_make(self):
    #     return self._make

    # def set_make(self, make):
    #     self._make = make

    def vehicle_description(self):
        description = f"{self._make} {self.kind} ({self.power_source})"
        if self.battery_capacity:  # Only add battery info if it exists
            description += f" (Battery: {self.battery_capacity})"
        return description

    @staticmethod      # This is the staticmethod decorator
    def general_info():
        return "A vehicle is a machine used for transportation."


# Using the static method
print(Vehicle.general_info())

# Creating instances (both electric and non-electric)
my_car = Vehicle("Tesla", "Sedan", "Electric", "75kWh")  
my_motorcycle = Vehicle("Harley-Davidson", "Cruiser", "Gasoline")  
my_van = Vehicle("Toyota", "Van", "Hybrid") 

# Printing details
print(my_car.vehicle_description())
print(my_motorcycle.vehicle_description())
print(my_van.vehicle_description())