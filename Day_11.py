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

