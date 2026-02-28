# Day 9: Functions (Part 1)
# What I am going to learn today Defining functions, arguments, parameters, return values
# functions, which are named blocks of
# code that are designed to do one specific job. When you want to
# perform a particular task that you’ve defined in a function, you call the
# function responsible for it.

# DEFINING A FUNCTION
# Here’s a simple function named greet_user() that prints a greeting:
def greet_user():
    print("Heya")
greet_user()

# PASSING INFORMATION TO A FUNCTION
# Modified slightly, the function greet_user() can not only tell the user
# Hello! but also greet them by name.
def greet_user(username):
    print(f"Hello {username}")
greet_user("Saim")

# ARGUMENTS AND PARAMETERS
# In the preceding greet_user() function, we defined greet_user() to require
# a value for the variable username. Once we called the function and gave it
# the information (a person’s name), it printed the right greeting.
# The variable username in the definition of greet_user() is an example of
# a parameter, a piece of information the function needs to do its job. The
# value 'jesse' in greet_user('jesse') is an example of an argument. An
# argument is a piece of information that’s passed from a function call to a
# function. When we call the function, we place the value we want the
# function to work with in parentheses. In this case the argument 'jesse'
# was passed to the function greet_user(), and the value was assigned to the
# parameter username.

# PASSING ARGUMENTS
# Because a function definition can have multiple parameters, a function
# call may need multiple arguments. You can pass arguments to your
# functions in a number of ways. You can use positional arguments, which
# need to be in the same order the parameters were written; keyword
# arguments, where each argument consists of a variable name and a value;
# and lists and dictionaries of values. Let’s look at each of these in turn.

# POSITIONAL ARGUMENTS
# Matching argument in the function call with a parameter in the function definition.
# . The simplest
# way to do this is based on the order of the arguments provided. Values
# matched up this way are called positional arguments.
def describe_pet(animal_type,pet_name):
    print(f"\nI have {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")
describe_pet('hamster','hary')


# MULTIPLE FUNCTION CALLS
# You can call a function as many times as needed
def describe_pet(animal_type,pet_name):
    print(f"\nI have {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")
describe_pet('hamster','hary')
describe_pet('dog','pug')


# ORDER MATTERS IN POSITIONAL ARGUMENTS
# we can get unexpected results if you mix up the order of the arguments in a function call when using positional
# arguments
describe_pet('harry', 'hamster')
# In this function call we list the name first and the type of animal
# second. Because the argument 'harry' is listed first this time, that value is
# assigned to the parameter animal_type. Likewise, 'hamster' is assigned to
# pet_name. Now we have a “harry” named “Hamster”: I have a harry.
# My harry's name is Hamster
# If you get funny results like this, check to make sure the order of the
# arguments in your function call matches the order of the parameters in
# the function’s definition.




# KEYWORD ARGUMENTS
# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when
# you pass the argument to the function, there’s no confusion (you won’t
# end up with a harry named Hamster). Keyword arguments free you
# from having to worry about correctly ordering your arguments in the
# function call, and they clarify the role of each value in the function call.
# Let’s rewrite pets.py using keyword arguments to call describe_pet():
# def describe_pet(animal_type, pet_name):
# """Display information about a pet."""
# print(f"\nI have a {animal_type}.")
# print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry') The function
# describe_pet() hasn’t changed. But when we call the function, we
# explicitly tell Python which parameter each argument should be
# matched with. When Python reads the function call, it knows to assign
# the argument 'hamster' to the parameter animal_type and the argument
# 'harry' to pet_name. The output correctly shows that we have a hamster
# named Harry.
# The order of keyword arguments doesn’t matter because Python
# knows where each value should go. The following two function calls are
# equivalent: describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')



# DEFAULT VALUES
# When writing a function, you can define a default value for each
# parameter. If an argument for a parameter is provided in the function
# call, Python uses the argument value. If not, it uses the parameter’s
# default value. So when you define a default value for a parameter, you
# can exclude the corresponding argument you’d usually write in the
# function call. Using default values can simplify your function calls and
# clarify the ways in which your functions are typically used.
# For example, if you notice that most of the calls to describe_pet() are
# being used to describe dogs, you can set the default value of animal_type
# to 'dog'. Now anyone calling describe_pet() for a dog can omit that
# information: def describe_pet(pet_name, animal_type='dog'):
# """Display information about a pet."""
# print(f"\nI have a {animal_type}.")
# print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie')
# We changed the definition of describe_pet() to include a default value,
# 'dog', for animal_type. Now when the function is called with no animal_type
# specified, Python knows to use the value 'dog' for this parameter: I have
# a dog.
# My dog's name is Willie.
# Note that the order of the parameters in the function definition had
# to be changed. Because the default value makes it unnecessary to specify
# a type of animal as an argument, the only argument left in the function
# call is the pet’s name. Python still interprets this as a positional
# argument, so if the function is called with just a pet’s name, that
# argument will match up with the first parameter listed in the function’s
# definition. This is the reason the first parameter needs to be pet_name.
# The simplest way to use this function now is to provide just a dog’s
# name in the function call: describe_pet('willie') This function call would
# have the same output as the previous example. The only argument
# provided is 'willie', so it is matched up with the first parameter in the
# definition, pet_name. Because no argument is provided for animal_type,
# Python uses the default value 'dog'.
# To describe an animal other than a dog, you could use a function call
# like this: describe_pet(pet_name='harry', animal_type='hamster')
# Because an explicit argument for animal_type is provided, Python will
# ignore the parameter’s default value




# EQUIVALENT FUNCTION CALLS
# Because positional arguments, keyword arguments, and default values
# can all be used together, often you’ll have several equivalent ways to call
# a function. Consider the following definition for describe_pet() with one
# default value provided: def describe_pet(pet_name, animal_type='dog'):
# With this definition, an argument always needs to be provided for
# pet_name, and this value can be provided using the positional or keyword
# format. If the animal being described is not a dog, an argument for
# animal_type must be included in the call, and this argument can also be
# specified using the positional or keyword format.
# All of the following calls would work for this function: # A dog
# named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry') Each of these
# function calls would have the same output as the previous examples.



# RETURN VALUES
# A function doesn’t always have to display its output directly. Instead, it
# can process some data and then return a value or set of values. The
# value the function returns is called a return value.


# RETURNING A SIMPLE VALUE
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
user = get_formatted_name("saim","kazmi")
print(user)


# RETURNING A DICTIONARY
# example, the
# following function takes in parts of a name and returns a dictionary
# representing a person
def build_person(first_name,last_name,age = None):
    person = {'first':first_name,'last':last_name }
    if age:
        person['age']= age
    return person

full_name = build_person('Saim','Kazmi', 21)

print(full_name)


# USING A FUNCTION WITH A WHILE LOOP

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\n Please tell me your name: ")
    print("\nEnter q at any to time to quit")
    f_name = input("Enter Your First Name: ")
    l_name = input("Enter your Last Name:")
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"Hello {formatted_name}")
    if f_name == 'q':
        break

    if l_name == 'q':
        break

# PASSING A LIST
def greet_users(names):
    for name in names:
        msg = f"Hello {name}"
        print(msg)


username = ["Saim","Imaad","Musheer"]
greet_users(username)

# MODIFYING A LIST IN A FUNCTION
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models():
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_models():
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

print_models()
show_models()

# PREVENTING A FUNCTION FROM MODIFYING A LIST
# Even though you can preserve the contents of a list by passing a copy
# of it to your functions, you should pass the original list to functions
# unless you have a specific reason to pass a copy. It’s more efficient for a
# function to work with an existing list to avoid using the time and
# memory needed to make a separate copy, especially when you’re
# working with large lists.
