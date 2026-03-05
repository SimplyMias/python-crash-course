# Day 13 Files & Exceptions
# What I am going to learn today is  Reading/writing files, try-except blocks, storing data
from fontTools.merge.util import first

from Day_05 import answer

# READING FROM A FILE
# An incredible amount of data is available in text files. Text files can
# contain weather data, traffic data, socioeconomic data, literary works,
# and more. Reading from a file is particularly useful in data analysis
# applications, but it’s also applicable to any situation in which you want
# to analyze or modify information stored in a file

# For example, you can
# write a program that reads in the contents of a text file and rewrites the
# file with formatting that allows a browser to display it.

#READING AN ENTIRE FILE
# To begin, we need a file with a few lines of text in it

# Here’s a program that opens this file, reads it, and prints the contents
# of the file to the screen
# with open('pie_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# FILE PATHS
#  relative file path tells Python to look
# for a given location relative to the directory where the currently
# running program file is stored. For example, you’d write: with
# open('text_files/filename.txt') as file_object

# You can also tell Python exactly where the file is on your computer
# regardless of where the program that’s being executed is stored. This is
# called an absolute file path


# READING LINE BY LINE
# When you’re reading a file, you’ll often want to examine each line of
# the file. You might be looking for certain information in the file, or you
# might want to modify the text in the file in some way.

# You can use a for loop on the file object to examine each line from a
# file one at a time:
# file_name = 'pie_digits.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# MAKING A LIST OF LINES FROM A FILE
# file_name = 'pie_digits.txt'
# with open(file_name) as file_object:
#     lines = file_object.read()
#
# for line in lines:
#     print(line.rstrip())
# The readlines() method takes each line from the file and stores it
# in a list

# WORKING WITH A FILE'S CONTENTS
# After you’ve read a file into memory, you can do whatever you want
# with that data, so let’s briefly explore the digits of pi. First, we’ll attempt
# to build a single string containing all the digits in the file with no
# # whitespace in it:
# file_name = 'pie_digits.txt'
# with open(file_name, 'r') as f:
#     lines = f.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))


# LARGE FILES: ONE MILLION DIGITS
# So far we’ve focused on analyzing a text file that contains only three
# lines, but the code in these examples would work just as well on much
# larger files. If we start with a text file that contains pi to 1,000,000
# decimal places instead of just 30, we can create a single string
# containing all these digits. We don’t need to change our program at all
# except to pass it a different file.
# file_name = 'pie_million_digits.txt'
# with open(file_name) as f:
#     lines = f.readlines()
#     pi_string = ''
#     for line in lines:
#         pi_string += line.strip()
# # print(f"{pi_string[:52]}...")
# # print(len(pi_string))
#
#
# # IS YOUR BIRTHDAY CONTAINED IN PIE
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pie!")
# else:
#     print("Your birthday does not appear in the first million digits of pie!")
#

# WRITING TO A FILE
# One of the simplest ways to save data is to write it to a file. When you
# write text to a file, the output will still be available after you close the
# terminal containing your program’s output. You can examine output
# after a program finishes running, and you can share the output files with
# others as well. You can also write programs that read the text back into
# memory and work with it again later.


# WRITING TO AN EMPTY FILE
# To write text to a file, you need to call open() with a second argument
# telling Python that you want to write to the file
# file_name = 'programming.txt'
# with open(file_name, 'w') as f:
#     f.write("I love programming")

# WRITING MULTIPLE LINES
# The write() function doesn’t add any newlines to the text you write. So if
# you write more than one line without including newline characters,
# file_name = 'programming.txt'
# with open(file_name, 'w') as f:
#     f.write("I love programming.\n")
#     f.write("I love creating new games.\n")

# APPENDING TO A FILE
# If you want to add content to a file instead of writing over existing
# content, you can open the file in append mode. When you open a file in
# append mode, Python doesn’t erase the contents of the file before
# returning the file object. Any lines you write to the file will be added at
# the end of the file. If the file doesn’t exist yet, Python will create an
# empty file for you.
file_name = 'random.txt'
with open(file_name, 'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")


# EXCEPTIONS
# Python uses special objects called exceptions to manage errors that arise
# during a program’s execution. Whenever an error occurs that makes
# Python unsure what to do next, it creates an exception object
# If you
# write code that handles the exception, the program will continue
# running. If you don’t handle the exception, the program will halt and
# show a traceback, which includes a report of the exception that was raised
# Exceptions are handled with try-except blocks. A try-except block asks
# Python to do something, but it also tells Python what to do if an
# exception is raised. When you use try-except blocks, your programs will
# continue running even if things start to go wrong. Instead of tracebacks,
# which can be confusing for users to read, users will see friendly error
# messages that you write


# HANDLING THE ZeroDivisonError EXCEPTION
# Let’s look at a simple error that causes Python to raise an exception. You
# probably know that it’s impossible to divide a number by zero, but let’s
# ask Python to do it anyway: division_calculator.py
# print(5/0)
# Of course Python can’t do this, so we get a traceback: Traceback
# (most recent call last):
# File "division_calculator.py", line 1, in <module>
# print(5/0)
# ZeroDivisionError: division by zero The error reported at  in the
# traceback, ZeroDivisionError, is an exception object. Python creates this
# kind of object in response to a situation where it can’t do what we ask it
# to. When this happens, Python stops the program and tells us the kind
# of exception that was raised. We can use this information to modify our
# program. We’ll tell Python what to do when this kind of exception
# occurs; that way, if it happens again, we’re prepared.


# USING try-except BLOCKS
# When you think an error may occur, you can write a try-except block to
# handle the exception that might be raised. You tell Python to try
# running some code, and you tell it what to do if the code results in a
# particular kind of exception
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")

# USING EXCEPTIONS TO PREVENT CRASHES
# Handling errors correctly is especially important when the program has
# more work to do after the error occurs. This happens often in programs
# that prompt users for input. If the program responds to invalid input
# appropriately, it can prompt for more valid input instead of crashing.
# for example
# print("give me two numbers and i'll divide them")
# print("enter q to quit")
# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break
#     second_num = input("\nSecond number: ")
#     if second_num == 'q':
#         break
#     answer = int(first_num) / int(second_num)
#     print(answer)
# It’s bad that the program crashed, but it’s also not a good idea to let
# users see tracebacks. Nontechnical users will be confused by them, and
# in a malicious setting, attackers will learn more than you want them to
# know from a traceback. For example, they’ll know the name of your
# program file, and they’ll see a part of your code that isn’t working
# properly. A skilled attacker can sometimes use this information to
# determine which kind of attacks to use against your code.


# THE ELSE BLOCK
# We can make this program more error resistant by wrapping the line
# that might produce errors in a try-except block. The error occurs on the
# line that performs the division, so that’s where we’ll put the try-except
# block. This example also includes an else block. Any code that depends
# on the try block executing successfully goes in the else block
# print("give me two numbers and i'll divide them")
# print("enter q to quit")
# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break
#     second_num = input("\nSecond number: ")
#     if second_num == 'q':
#         break
#     try:
#        answer = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#        print("You can't divide by 0!")
#     else:
#           print(answer)

# HANDLING THE FileNotFoundError EXCEPTION
# One common issue










