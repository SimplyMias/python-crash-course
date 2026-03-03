from my_car import Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = None
        self.battery_size = 75
    def describe_battery(self):
        print(f"this car had a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

class Battery:
    def __int__(self,battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


