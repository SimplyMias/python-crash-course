# # Day 8 User Input and while loops
# # what I am going to learn today  input(), int() conversion, while loops, flags, break
# # HOW THE input() FUNCTION WORKS
# # The input() function pauses your program and waits for the user to enter
# # some text. Once Python receives the user’s input, it assigns that input to
# # a variable to make it convenient for you to work with.
#
# # EXAMPLE
# message = input("Tell me something and I will repeat it back to you: ")
# print(message)
# # The input() function takes one argument: the prompt, or instructions,that we want to display to the user so they know what to do.
#
#
# # WRITING CLEAR PROMPTS
# # you should use clear and easy to follow prompt that tells user exactly what kind of info you're looking for
# # name = input("Please Enter your name: ")
# # print(f"Hey {name}")
#
# # Sometimes you’ll want to write a prompt that’s longer than one line. you can assign your prompt to a variable and pass that variable to the
# # input() function
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your name: "
# name = input(prompt)
# print(f"Hello {name}")
#
# # USING int() TO ACCEPT NUMERICAL INPUT
# # when we use input() function this will consider everything as string
# # We can resolve this issue by using the int() function
# age = input("How old are you: ")
# age = int(age)
# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote ")
#
# # # ANOTHER EXAMPLE
# height = input("how tall are you in inches?: ")
# height = int(height)
#
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nyou'll be able to ride when you're a little order")
#
#
# # THE MODULO OPERATOR
# # It divides one number by another number and returns the remainder
# # When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0.
# number = input("Enter the number you want to check if it is even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\n{number} is an even number")
# else:
#     print(f"\n{number} is an odd number")
#
#
#
#
# # INTRODUCING WHILE LOOPS
# # The for loop takes a collection of items and executes a block of code
# # once for each item in the collection. In contrast, the while loop runs as
# # long as, or while, a certain condition is true.
#
# # THE WHILE LOOP IN ACTION
# # You can use a while loop to count up through a series of numbers.
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number+=1
# The programs you use every day most likely contain while loops. For
# example, a game needs a while loop to keep running as long as you want
# to keep playing, and so it can stop running as soon as you ask it to quit.
# Programs wouldn’t be fun to use if they stopped running before we told
# them to or kept running even after we wanted to quit, so while loops are
# quite useful


# LETTING THE USER CHOOSE WHEN TO QUIT
#FOR EXAMPLE
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter quit to end the program"
# message = " "
# while message != "quit":
#     message = input(prompt)
#     print(message)


# USING A FLAG
# If we have many conditions for stopping  program putting all the test in a single while loop statement is quit difficult
# we can define  one variable that determines whether the entire program is active or not
# This variable is called a flag
# . We can write our programs so they run while the flag is
# set to True and stop running when any of several events sets the value of
# the flag to False.
# so that our while loop need to check only one condition
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter quit to end the program "
# message = " "
# active = True
# while active :
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# USING BREAK TO EXIT A LOOP
# To exit a while loop immediately without running any remaining code in
# the loop, regardless of the results of any conditional test, use the break
# statement.
# For Example consider a program that asks the user about places
# they’ve visited.
# prompt = "\nPlease enter the name of city you have visited: "
# prompt += "\nEnter 'quit' when you are finished: "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")
# You can use the break statement in any of Python’s loops



# USING CONTINUE IN A LOOP
# Rather than breaking out of a loop entirely without executing the rest of
# its code, you can use the continue statement to return to the beginning of
# the loop based on the result of a conditional test.
#
# current_number = 0
# while current_number<10:
#     current_number+=1
#     if current_number%2==0:
#         continue
#     print(current_number)

# AVOIDING INFINITE LOOPS
# Every while loop needs a way to stop running so it won’t continue to run
# forever
# x = 1
# while x <= 5:
#  print(x)
#  x = x+1
#  if you accidentally omit the line x += 1 , the loop
# will run forever:


# USING A WHILE LOOP WITH LISTS AND DICTIONARIES
# to keep track of many users and pieces of
# information, we’ll need to use lists and dictionaries with our while loops.


# MOVING ITEMS FROM ONE LIST TO ANOTHER
# unconfirmed_user = ['Alice','David','Thomas']
# confirmed_user = []
# while unconfirmed_user:
#     current_user = unconfirmed_user.pop()
#     confirmed_user.append(current_user)
#     print(f"{current_user} is verified")
# print("users which are verified: ")
# print(confirmed_user)

# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST
# we used remove() to remove a specific value from a list. The
# remove() function worked because the value we were interested in
# appeared only once in the list. But what if you want to remove all
# instances of a value from a list?
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)


# FILLING A DICTIONARY WITH USER INPUT
# You can prompt for as much input as you need in each pass through a
# while loop. Let’s make a polling program in which each pass through the
# loop prompts for the participant’s name and response. We’ll store the
# data we gather in a dictionary, because we want to connect each
# response with a particular user
responses = {}
polling_active = True
while polling_active:
    name = input("/nWhat is your name: ")
    response = input("/nWhich car do you like the most: ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False
print("\n--- Poll Results ---")
for name,response in responses.items():
   print(f"{name} like  {response}.")












