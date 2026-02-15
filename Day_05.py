# Day 5 If Statements
# What I am going to learn today is Conditional tests, if-elif-else, checking lists
# If else are conditional statements
# Programming involves examining a set of conditions and deciding which action to take based on that conditions
# EXAMPLE
# Imagine you have a list of cars and you want
# to print out the name of each car. Car names are proper names, so the
# names of most cars should be printed in title case. However, the value
# 'bmw' should be printed in all uppercase
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# The loop in this example first checks if the current value of car is
# 'bmw If it is, the value is printed in uppercase. If the value of car is other than bmw its printed in title case


# CONDITIONAL TESTS
# At the heart of every if statement is an expression that can be evaluated as True or False and is called  a conditional test
# if conditional test is true the code is executed following the if statements, if the value is false the code will be ignored following the if statement


# CHECKING THE EQUALITY
# The simplest conditional test checks whether the value of a variable is equal to the value of interest
# car == 'bmw'

# (==). This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match.

# Testing for equality is case sensitive in Python
# For Example two values with different capitalization are not considered equal


# CHECKING FOR INEQUALITY
# When you want to determine whether two values are not equal, you can combine an exclamation point and an equal sign (!=)
# Example
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("hold the anchovies")

# NUMERICAL COMPARISONS
# testing numerical values is pretty straightforward
# EXAMPLE
age = 18
print(age == 18)
# You can also test to see if two numbers are equal
#EXAMPLE
answer = 17
if answer != 42:
    print("That is not correct answer. Please try again")
# You can include various mathematical comparisons in conditional statements as well
# such as less than, less than or equal to, greater than and greater than or equal to


# We can check Multiple conditions at the same time
# USING and TO CHECK MULTIPLE CONDITIONS
#To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the
# overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("Both conditions are True")
else:
    print("One of the condition is False")

# USING or TO CHECK MULTIPLE CONDITIONS

# The keyword or allows you to check multiple conditions as well, but it
# passes when either or both of the individual tests pass. An or expression
# fails only when both individual tests fail.
if age_0 >= 21 or age_1 >= 21:
    print("If any condition is True")
else:
    print("Both conditions are False")

# CHECKING WHETHER A VALUE IS IN A LIST
# Sometimes we want to check weather a list contains a certain value or not
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Yes it is available")
# the keyword in tells Python to check for the existence of 'mushrooms'  in the list requested_toppings.



# CHECKING WHETHER A VALUE IS NOT IN A LIST
# You can use the keyword not in this situation.
banned_users = ['andrew', 'carolina', 'david']
user = 'Marie'
if user not in banned_users:
    print(f"{user.title()} You can post a response if you wish")




















