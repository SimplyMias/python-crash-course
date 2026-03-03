# Day 12: Classes (Part 2)
# What I am going to learn today is Inheritance and Importing Classes
# INHERITANCE
# When one class inherits from another, it takes on
# the attributes and methods of the first class. The original class is called
# the parent class, and the new class is the child class. The child class can
# inherit any or all of the attributes and methods of its parent class, but it’s
# also free to define new attributes and methods of its own

# THE __init__() METHOD FOR A  CHILD CLASS
# When you’re writing a new class based on an existing class, you’ll often
# want to call the __init__() method from the parent class. This will
# initialize any attributes that were defined in the parent __init__() method
# and make them available in the child class.
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles



# DEFINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS
# Once you have a child class that inherits from a parent class, you can
# add any new attributes and methods necessary to differentiate the child
# class from the parent class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"this car had a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.describe_battery())

# OVERRIDING METHODS FROM THE PARENT CLASS
# Say the class Car had a method called fill_gas_tank(). This method is
# meaningless for an all-electric vehicle, so you might want to override
# this method. Here’s one way to do that: class ElectricCar(Car):
# --snip--
# def fill_gas_tank(self):
# """Electric cars don't have gas tanks."""
# print("This car doesn't need a gas tank!") Now if someone tries to call
# fill_gas_tank() with an electric car, Python will ignore the method
# fill_gas_tank() in Car and run this code instead. When you use
# inheritance, you can make your child classes retain what you need and
# override anything you don’t need from the parent class.

# INSTANCES AS ATTRIBUTES
# When modeling something from the real world in code, you may find
# that you’re adding more and more detail to a class. You’ll find that you
# have a growing list of attributes and methods and that your files are
# becoming lengthy. In these situations, you might recognize that part of
# one class can be written as a separate class. You can break your large
# class into smaller classes that work together

class Battery:
    def __int__(self,battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-KWh battery")
















