# Day 13 Files & Exceptions
# What I am going to learn today is  Reading/writing files, try-except blocks, storing data

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
# whitespace in it:
file_name = 'pie_digits.txt'
with open(file_name, 'r') as f:
    lines = f.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))