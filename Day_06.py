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



#LOOPING THROUGH A DICTIONARY
# You can loop through all of a dictionary's key-value pairs, through its keys or through its values


# LOOPING THROUGH ALL KEY-VALUE PAIRS
# Consider a new dictionary designed to store info about a user on a website
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
#you could loop through the dictionary using a for loop
for key,value in user_0.items():
    print(f"\n Key: {key} ")
    print(f"\n Value: {value}")


# looping through all key value pairs works particularly well for dictionaries  which stores the same kind of info for
# many different keys

for name,language in favorite_languages.items():
    print(f"\n{name.title()}'s favourite language is {language.title()}")


# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY
# the keys() method is useful when you don't need to work with all of the values in a dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# LOOPING THROUGH A DICTIONARY'S KEYS IN  A PARTICULAR ORDER
#looping through a dictionary returns the items in the same order they were inserted
#sometimes though you'll want to loop through a dictionary in a different order
# One way to do this is to sort the keys as they're returned in the for loop
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} thank you for taking thee poll")



# LOOPING THROUGH ALL VALUES IN A DICTIONARY
#If you are primarily interested in the values that a dictionary contains you can use the values() method to
# return a list of values without any keys
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

# To see each language chosen without
# repetition, we can use a set.
# A set is a collection in which each item must be unique
for language in set(favorite_languages.values()):
    print(language.title())
# When you wrap set() around a lis that contains duplicate items, Python identifies the unique items in the
# list and builds a set from those items



# You can build a set directly using braces and separating the elements with commas
languages = {'python', 'ruby', 'python', 'C'}
print(languages)
# You can build a set directly using braces and separating the elements with braces.
# When you see braces but no key-value pairs, you’re probably looking at a set.
# Unlike lists and dictionaries, sets do not retain items in any specific order





# NESTING
# Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting
# we can nest dictionaries inside a list
# we can nest list of items in a dictionary
# we can nest dictionary inside another dictionary


# A LIST OF DICTIONARIES
# EXAMPLE
alien_0 = {'color': 'blue', 'points': 5,}
alien_1 = {'color': 'green', 'points': 10,}
alien_2 = {'color': 'red', 'points': 5,}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# A more realistic example would involve more than three aliens with
# code that automatically generates each alien
aliens = []
for alien_numbers in range(30):
    new_alien = {'color': 'red', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'red':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# to see first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens : {len(aliens)}")

#  A LIST IN A DICTIONARY
# Rather than putting a dictionary inside a list, it’s sometimes useful to put
# a list inside a dictionary
# Store information about a pizza being ordered.
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
   print("\t" + topping)



favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
   print(f"\n{name.title()}'s favorite languages are:")
for language in languages:
   print(f"\t{language.title()}")





# A DICTIONARY IN A DICTIONARY
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
location = user_info['location']
print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {location.title()}")





