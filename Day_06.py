# Day 6 Dictionaries
# What I am going to learn today Key-value pairs, accessing values, looping, nesting
# Dictionaries can store an almost limitless amount of information

# A SIMPLE DICTIONARY
alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# WORKING WITH DICTIONARIES
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value
# associated with that key. A key’s value can be a number, a string, a list, or even another dictionary

# In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces, as shown in the earlier example: alien_0
# A key-value pair is a set of values associated with each other.

# ACCESSING VALUES IN A DICTIONARY
# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
print(alien_0['color'])
# You can use it like this
new_points = alien_0['points']
print(f"You just earned {new_points} points.")

# ADDING NEW KEY-VALUE PAIRS
# Dictionaries are dynamic structures, and you can add new key-value
# pairs to a dictionary at any time. For example, to add a new key-value
# pair, you would give the name of the dictionary followed by the new key
# in square brackets along with the new value.
print(alien_0)
alien_0['x-coordinates'] = 0
alien_0['y-coordinates'] = 25
print(alien_0)

# STARTING WITH AN EMPTY DICTIONARY
#  To start filling an empty dictionary, define a dictionary with an empty set of braces and then add
# each key-value pair on its own line. For example, here’s how to build the
# alien_0 dictionary using this approach
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# MODIFYING VALUES IN A DICTIONARY
#  give the name of the dictionary with
# the key in square brackets and then the new value you want associated
# with that key.
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")




