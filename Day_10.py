

# Day 10: Functions (Part 2)
# What I am going to learn today is Arguments and Modules

# PASSING AN ARBITRARY NUMBER OF ARGUMENTS

# Sometimes you won’t know ahead of time how many arguments a
# function needs to accept. Fortunately, Python allows a function to
# collect an arbitrary number of arguments from the calling statement.

# The function in the following
# example has one parameter, *toppings, but this parameter collects as
# many arguments as the calling line provides

# def make_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
# make_pizza("pepproni")
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# MIXING POSITIONAL AND ARBITRARY ARGUMENTS
# If you want a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be
# placed last in the function definition. Python matches positional and
# keyword arguments first and then collects any remaining arguments in
# the final parameter.
# def make_pizza(size,*toppings):
#     print(f"Making a {size}-inches pizza with the following toppings:  ")
#     for topping in toppings:
#         print(topping)
#
# make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
#

# USING ARBITRARY KEYWORD ARGUMENTS
# def build_profile(first,last,**user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
# location='princeton',
# field='physics')
# print(user_profile)




# STORING YOUR FUNCTIONS IN MODULES
# One advantage of functions is the way they separate blocks of code from
# your main program. By using descriptive names for your functions, your
# main program will be much easier to follow. You can go a step further
# by storing your functions in a separate file called a module and then
# importing that module into your main program. An import statement tells
# Python to make the code in a module available in the currently running
# program file.
# Storing your functions in a separate file allows you to hide the details
# of your program’s code and focus on its higher-level logic. It also allows
# you to reuse functions in many different programs. When you store
# your functions in separate files, you can share those files with other
# programmers without having to share your entire program. Knowing
# how to import functions also allows you to use libraries of functions that
# other programmers have written.



# IMPORTING AN ENTIRE MODULE
# To start importing functions, we first need to create a module. A module
# is a file ending in .py that contains the code you want to import into
# your program.
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# IMPORTING SPECIFIC FUNCTIONS
# You can also import a specific function from a module. Here’s the
# general syntax for this approach: from module_name import
# function_name You can import as many functions as you want from a
# module by separating each function’s name with a comma: from
# module_name import function_0, function_1, function_2

#USING as TO GIVE A FUNCTION AN ALIAS
# If the name of a function you’re importing might conflict with an
# existing name in your program or if the function name is long, you can
# use a short, unique alias—an alternate name similar to a nickname for
# the function. You’ll give the function this special nickname when you
# import the function.
# The general syntax for providing an alias is: from module_name
# import function_name as fn
# from  pizza import make_pizza as mp
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# USING as TO GIVE A MODULE AN ALIAS
# You can also provide an alias for a module name. Giving a module a
# short alias, like p for pizza, allows you to call the module’s functions
# more quickly. Calling p.make_pizza() is more concise than calling
# pizza.make_pizza(): import pizza as p
# The general syntax for this approach is: import module_name as mn

# IMPORTING ALL FUNCTIONS IN A MODULE
# You can tell Python to import every function in a module by using the
# asterisk (*) operator: from pizza import *