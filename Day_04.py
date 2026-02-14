# Day 4 Working with Lists
# What I am going to  learn is  Looping through lists, list comprehensions, slices, tuples

# LOOPING THROUGH AN ENTIRE LIST
# Use loop when you want to run through all entries in a list, performing the same task each time
# Example Printing items of list using loop
magicians =  ['alice', 'david', 'carolina'] # Begining with defining a list
for magician in magicians: # defining a for loop (magicians(list name) associating it with magician(variable))
    print(magician.title()) # printing each entry of list
# the first line tells Python to retrieve the first value from the list magicians
# and associate it with the variable magician. This first value is 'alice'.
# Python then reads the next line
# Python prints the current value of magician, which is still 'alice'.
# Because the list contains more values, Python returns to the first line of
# the loop

# DOING SOMETHING AFTER A FOR LOOP
# Any lines of code after the for loop that are not indented are executed once without repetition
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")


# python's range() function makes it easy to generate a series of numbers
#Example
for value in range(1,5):
    print(value)
# range function has off by one the output never contains the last value

# If we pass only one argument in the range function it will start counting from 0 also off it by one
# Example
for count in range(6):
    print(count)



# USING range() TO MAKE A LIST OF NUMBERS
# wrap list() around a call to to the range() function, the output will be a list of numbers
numbers = list(range(1,6))
print(numbers)

# TO SKIP NUMBERS IN A GIVEN RANGE pass third argument in range() function
for i in range(2, 11, 2):
    print(i)

#  list of the first 10 square numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
for i in  squares:
    print(i)
#Another method (Shorthand omitting temporary variable)
Squares = []
for i in range(1,11):
    Squares.append(i ** 2)
print(Squares)


# SIMPLE STATISTICS WITH A LIST OF NUMBERS
digit = [2,5,9,7,5]
print(min(digit))
print(max(digit))
print(sum(digit))


# LIST COMPREHENSIONS
# (its kind of reducing lines of codes )
# List comprehension combines the for loop and the creation  of new elements into one line and automatically appends
# each new element
squares = [value ** 2 for value in range(1,11)]
print(squares)

# WORKING WITH PART OF A LIST
# you can work with a specific group of items in a list, which python called a slice

# SLICING A LIST
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[1:4])
# If we omit the first index, slicing automatically start from index 0
print(players[:4])
# If you want all item from third item start from index 2 and skip the second index
print(players[2:])
# This syntax allows you to output all the  elements from any point
# in your list to the end regardless of the length of the list

# negative index returns an element a certain distance from the end of the list
print(players[-3:])

# LOOPING THROUGH A SLICE
# we can use a slice in a for loop if we want to loop through a subset of the elements in a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player)




# COPYING A LIST
# To copy a list, you can make a slice that includes the entire original
# list by omitting the first index and the second index ([:])

my_food = ["pizza","falafel","cheesecake"]
friends_food = my_food[:]

print("My favourite foods are: ")
print(my_food)

print("\n My friend's favourite food are: ")
print(friends_food)

my_food.append("Ice Cream")
friends_food.append("Cannoli")

print("My favourite foods are: ")
print(my_food)

print("\n My friend's favourite food are: ")
print(friends_food)




# TUPLES





















