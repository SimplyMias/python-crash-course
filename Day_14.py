# Day 14 Testing your Code
# TESTING A FUNCTION
# To learn about testing, we need code to test. Here’s a simple function
# that takes in a first and last name, and returns a neatly formatted full
# name
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
get_formatted_name("Sexxy","Baby")