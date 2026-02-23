# Day 8 User Input and while loops
# what I am going to learn today  input(), int() conversion, while loops, flags, break
# HOW THE input() FUNCTION WORKS
# The input() function pauses your program and waits for the user to enter
# some text. Once Python receives the user’s input, it assigns that input to
# a variable to make it convenient for you to work with.

# EXAMPLE
message = input("Tell me something and I will repeat it back to you: ")
print(message)
# The input() function takes one argument: the prompt, or instructions,that we want to display to the user so they know what to do.


# WRITING CLEAR PROMPTS
# you should use clear and easy to follow prompt that tells user exactly what kind of info you're looking for
# name = input("Please Enter your name: ")
# print(f"Hey {name}")

# Sometimes you’ll want to write a prompt that’s longer than one line. you can assign your prompt to a variable and pass that variable to the
# input() function
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name: "
name = input(prompt)
print(f"Hello {name}")

# USING int() TO ACCEPT NUMERICAL INPUT
# when we use input() function this will consider everything as string
# We can resolve this issue by using the int() function
age = input("How old are you: ")
age = int(age)
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote ")

# # ANOTHER EXAMPLE
height = input("how tall are you in inches?: ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nyou'll be able to ride when you're a little order")


# THE MODULO OPERATOR
# It divides one number by another number and returns the remainder
# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0.
number = input("Enter the number you want to check if it is even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\n{number} is an even number")
else:
    print(f"\n{number} is an odd number")






