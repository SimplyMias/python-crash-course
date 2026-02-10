# Day 3 Introducing Lists
# What I have learned today is Creating, Accessing, Modifying lists
# LIST
# A lst is a collection of items in a particular order
# a list can be of numbers, alphabets, or anything like name of all  family members
# square brackets indicates a list [], and the elements are separated by the commas
# Example of list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# ACCESSING ELEMENTS IN A LIST
# we can access element in a list by using position or index of the element
# To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
print(bicycles[0])

# Index position start from 0 not from 1
# Means to access the fourth item in a
# list, you request the item at index 3
print(bicycles[3])

# To access the last element of the list you can ask for item at index -1
print(bicycles[-1])
#The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

# Using individual values from the list
# Let’s try pulling the first bicycle from the list and composing a
# message using that value.
message = f"My first bicycle was {bicycles[2].title()}"
print(message)


# CHANGING, ADDING AND REMOVING ELEMENTS
# Modifying elements in a list
# the syntax of modifying an element is similar to accessing element
#Example
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# To modify let say 2nd element
motorcycles[1] = 'Ducati'
print(motorcycles)

# ADDING ELEMENT TO A LIST
# Python provides several ways to add new data to existing lists.

# 1. Appending elements to the end of a list
# When we append the list the new element is added at the end of the list
motorcycles.append('yamaha')
print(motorcycles)

# append() helps to build list dynamically you can start with empty list and then add elements to the list using a
# series of append() calls
# Example
bikes = []
bikes.append('KTM')
bikes.append('Gixxer')
bikes.append('Bullet')
print(bikes)

# 2. Inserting Elements into a list
# you can add element at any position in the list using insert() method
# specify the index of the new element and the value of the new element
bikes.insert(1,'GT')
print(bikes)



# REMOVING ELEMENTS FROM A LIST
# 1. Removing an element using the del Statement
# If you know the position of the element you want to remove from a list you can use the del statement
del bikes[0]
print(bikes)

# 2. Removing an item using the pop() method
# the pop method remove the last element in a list but it lets you work with that item after removing it
popped_bike = bikes.pop()
print(bikes)
print(popped_bike)
print(f"The last bike i owned was a {popped_bike}")

# 3. Popping items from any position in a list
# by including the index of the item you want to remove in parentheses
bikes.pop(1)
print(bikes)

# 4. Removing an element by Value
# If you only know the value of the item you want to
# remove, you can use the remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that’s being removed from a list
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me")




