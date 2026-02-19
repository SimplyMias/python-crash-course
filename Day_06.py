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


# REMOVING KEY-VALUE PAIRS
# you can use del statement to completely remove a key-value pair
# the del need the name of the dictionary and the key that you want to remove
# let’s remove the key 'points' from the alien_0 dictionary
# along with its value
print(alien_0)
del alien_0['points']
print(alien_0)



# # A DICTIONARY OF SIMILAR OBJECTS
# A dictionary is useful for storing the results
# of a simple poll, like this: favorite_languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}")


# USING get() TO ACCESS VALUES
#  you can use the get() method
# to set a default value that will be returned if the requested key doesn’t
# exist
student = {
    "name": "Sam",
    "age": 20,
    "course": "CSE"
}

print(student.get("name"))
print(student.get("marks"))




# LOOPING THROUGH A DICTIONARY
# You can loop through all of a
# dictionary’s key-value pairs, through its keys, or through its values

# LOOPING THROUGH ALL KEY-VALUE PAIRS
# the following dictionary would store one person's username, first name and last name
user_0 = {
    'username' : 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")



# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY
# the keys() method is useful when you don't need to work with all of the values in a dictionary
for name in favorite_languages.keys():
    print(name)




# You can access the value associated with any key you care about
# inside the loop by using the current key
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())
if name in friends:
     language = favorite_languages[name].title()
     print(f"\t{name.title()}, I see you love {language}!")



