# Day 2 Variables and simple data types
#What I have learned today is Strings, numbers, comments, naming conventions

# VARIABLES
# variables are like container to store some kind of values
message = "Hello Python World" # Here message is a variable "Hello Python World" is a value associated with variable message
print(message)
# Rules for naming a variable
#1 Variable names can contain only letters, numbers, and underscores
#2 Spaces are not allowed in variable names
#3 Avoid using Python keywords and function names as variable names
#4 Variable names should be short but descriptive
#5 variable name as uppercase and as lowercase are two different things

# STRINGS
# It is a datatype
# A string is a series of characters.
# anything inside quotes is considered a string in Python (both single and double quotes)
# "Saim Kazmi" -- it is a string

# OPERATIONS ON STRINGS
name = "saim kazmi"
print(name.title())
# .title() is method in python used to capitalise the first character of word in python
# A method is an action that python can perform on a piece of data

print(name.upper())
# .upper() is a method to  change string to all uppercase
print(name.lower())
# .lower() is a method to change string to all lowercase

# USING VARIABLES IN STRINGS
# To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark
# These strings are called f-strings. the f is for format
first_name = "Saim"
last_name = "Kazmi"
full_name = f"{first_name} {last_name}"
print(full_name)
#Also you can use it like this also
print(f"Hello, {full_name}")


# ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES
#whitespaces === nonprinting character
# to add tab in your text you can use \t
print("\t Saim")
# to add newline in your text you can use \n
print("python\n")
print("Java\n")
print("Rust\n")

# STRIPPING WHITESPACE
#To programmers 'python' and 'python ' look pretty much the same. But to a program, they
# are two different strings.
# To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
fav_language = 'Python '
print(fav_language)
fav_language = fav_language.rstrip()
print(fav_language)
# You can also strip whitespace from the left side of a string using the
# lstrip() method, or from both sides at once using strip():
fav_language = ' python'
fav_language = fav_language.lstrip()
print(fav_language)
fav_language = ' python '
fav_language = fav_language.strip()
print(fav_language)



# NUMBERS
#Integers
# Operations on integers
print(2+3) # Addition
print(5-2) # Subtraction
print(2*3) # Multplication
print(3/2) # Division
print(2**2) # Exponents

# Python supports the order of operations too, so you can use multiple
# operations in one expression. You can also use parentheses to modify
# the order of operations so Python can evaluate your expression in the
# order you specify.
print(2+ 3*4)
print((2+3) * 4)

#Floats
# Python calls any number with a decimal point a float.
print(0.1+0.1)
print(0.4 - 0.2)
print(2 * 0.1)

# When you divide any two numbers, even if they are integers that result
# in a whole number, you’ll always get a float
print(4/2)
#If you mix an integer and a float in any other operation, you’ll get a
# float as well
print(1 + 2.0)

# Underscores in Numbers
#When you print a number that was defined using underscores, Python prints only the digits:
number = 12_000_000_000
print(number)

# Multiple Assignments
# You can assign values to more than one variable using just a single line
x, y, z = 1,4,7
print(x)
print(y)
print(z)
# u just need to separate variables using commas


# Constants
#A constant is like a variable whose value stays the same throughout the life of a program
# To make variable constant make the name of the variable all capital letters
MAX_CONNECTIONS = 5000

# COMMENTS
# Comments are used to add notes in the program files
# In python you can add comment by adding # in front of the line you want to comment out













