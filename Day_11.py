# Day 11: Classes (Part 1)
# What I am going to learn today is Creating and using a class & working with classes and Instances
# CREATING AND USING A CLASS
# You can model almost anything using classes. Let’s start by writing a
# simple class, Dog, that represents a dog—not one dog in particular, but
# any dog. What do we know about most pet dogs? Well, they all have a
# name and age. We also know that most dogs sit and roll over. Those
# two pieces of information (name and age) and those two behaviors (sit
# and roll over) will go in our Dog class because they’re common to most
# dogs. This class will tell Python how to make an object representing a
# dog. After our class is written, we’ll use it to make individual instances,
# each of which represents one specific dog

# CREATING THE DOG CLASS
# Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over()
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

# MAKING AN INSTANCE FORM A CLASS
my_dog = Dog('Willie',6)
print(f"My dog name is {my_dog.name}")
print(f"My dog  is {my_dog.age} years old")

# ACCESSING ATTRIBUTES
# To access the attributes of an instance, we use dot notation.


# CALLING METHODS
# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. Let’s make our dog sit and roll over:
my_dog.sit()
my_dog.roll_over()

# CREATING MULTIPLE INSTANCES
your_dog = Dog('Lucy',2)
print(f"Your dog name is {your_dog.name}")
print(f"Your dog is {your_dog} old")
your_dog.sit()
your_dog.roll_over()
# Even if we used the same name and age for the second dog, Python
# would still create a separate instance from the Dog class. You can make as
# many instances from one class as you need, as long as you give each
# instance a unique variable name or it occupies a unique spot in a list or
# dictionary

# WORKING WITH CLASSES AND INSTANCES
# You can use classes to represent many real-world situations. Once you
# write a class, you’ll spend most of your time working with instances
# created from that class


# THE CAR CLASS
# Let’s write a new class representing a car. Our class will store information about the kind of car we’re working with, and it will have a
# method that summarizes this information
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_second_car = Car('BMW','M5',2024)
print(my_second_car.get_descriptive_name())


# To make the class more interesting, let’s add an attribute that
# changes over time. We’ll add an attribute that stores the car’s overall
# mileage.

# SETTING A DEFAULT VALUE FOR AN ATTRIBUTE
# When an instance is created, attributes can be defined without being
# passed in as parameters. These attributes can be defined in the __init__()
# method, where they are assigned a default value.
# Adding another attribute
my_second_car.read_odometer()

# MODIFYING ATTRIBUTE VALUES
# You can change an attribute’s value in three ways: you can change the
# value directly through an instance, set the value through a method, or
# increment the value (add a certain amount to it) through a method.

# MODIFYING AN ATTRIBUTE'S VALUE DIRECTLY
# The simplest way to modify the value of an attribute is to access the
# attribute directly through an instance
my_new_car.odometer_reading = 23
my_new_car.get_descriptive_name()
my_new_car.read_odometer()


# MODIFYING AN ATTRIBUTE'S VALUE THROUGH A MODEL
# It can be helpful to have methods that update certain attributes for you.
# Instead of accessing the attribute directly, you pass the new value to a
# method that handles the updating internally
my_new_car.update_odometer(90)
my_new_car.read_odometer()

# INCREMENTING AN ATTRIBUTE'S VALUE THROUGH A METHOD
# Sometimes you’ll want to increment an attribute’s value by a certain
# amount rather than set an entirely new value

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()









