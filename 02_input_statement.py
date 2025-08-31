# Lesson 2: The input() Statement
# --------------------------------
# In this lesson, you will learn how to use Python's input() function.
#
# The input() function is used to take input from the user.
# It allows your program to interact with the user by asking for input.
# You can ask the user to enter text, numbers, or any other data.
# The input is always returned as a string, even if the user enters a number.
# The basic syntax of the input() function is:
# Syntax:
#   input(prompt)
#   where prompt is an optional string that is displayed to the user.


# -------------------------------------------------
# 1. Taking input from the user
# -------------------------------------------------
# Use input() to ask the user for input.
# For example, we are using string concatenation to greet the user.
print("Hello" + input("What is your name? ") + "!")  # asks for name
# Output: What is your name? Alice (If the user types "Alice" as input and presses Enter)
#         Hello Alice! (This is the output printed to the console)
# Here, we use the input() function to ask the user for their name.
# The prompt "What is your name? " is displayed to the user.
# The input() function displays the prompt and waits for the user to type something.
# After the user presses Enter, the input is returned as a string.
# And finally, it is concatenated with "Hello" and "!" to form the complete greeting and printed.
print("---------------------------------")


# ------------------------------------------------
# 2. Using input() with variables
# -------------------------------------------------
# You can store the input in a variable for later use.
# This is useful when you want to use the input multiple times or in different parts of your program.
# For example, instead of asking the user for their name every time we want to greet them, we can store the input in a variable and use that variable later.
# This way, we can reuse the input without asking the user again.
#
# ..................
# But first let us know what a variable is (we will cover this in detail in the next lesson).
# A variable is a named location in memory that stores a value.
# You can think of it as a container for data that you can use later in your program.
# Variables can hold different types of data, such as strings, numbers, lists, etc.
# You can create a variable by giving it a name and assigning it a value using the equals sign (=).
# For example:
#   name = "Alice"
# This creates a variable named `name` and assigns it the value "Alice".
#
# -------------------------------------------------
# Now, let's use the input() function to ask for the user's name and store it in a variable.
# We will then use that variable in a print statement to greet the user.
# This allows us to reuse the input without asking the user again.
name = input("What is your name? ")  # store input in a variable
print("Hello " + name + "!")  # use the variable in a print statement
# Output: What is your name? Bob
#         Hello Bob!
# Here, we store the user's input in the variable `name` and then use it in the print statement.
# This way, we can greet the user without asking for their name again.
print("---------------------------------")


# -------------------------------------------------
# 3. Converting input to numbers
# -------------------------------------------------
# Sometimes, you may want to take numeric input from the user.
# However, the input() function always returns a string.
# To convert the input to a number, you can use the int() or float() functions.
# The int() function converts a string to an integer, and the float() function converts a string to a floating-point number (decimal).
# For example, if you want to ask the user for their age and use it in a calculation, you can do the following:
age_number = int(input("Enter your age in years: "))  # convert input to an integer
print("In 5 years, you will be:", age_number + 5)
# Output: Enter your age in years: 20
#         In 5 years, you will be: 25
# Here, we ask the user for their age, convert the input to an integer using int(), and then add 5 to it.
# This allows us to perform calculations with the user's input.
# Let's also see how to convert input to a float:
height_number = float(input("Enter your height in meters: ")) # convert input to a float
print("Your height in centimeters is:", height_number * 100)
# Output: Enter your height in meters: 1.75
#         Your height in centimeters is: 175.0
# Here, we ask the user for their height, convert the input to a float using float(), and then multiply it by 100 to convert it to centimeters.
print("---------------------------------")


# -------------------------------------------------
# 4. Using input with commas in print()
# -------------------------------------------------
# You can also use commas in the print() function to separate multiple items.
# This allows you to print multiple values without needing to concatenate them.
# For example, you can print the user's name and age like this:
name = input("What is your name? ")  # store input in a variable
age = int(input("What is your age? "))  # convert input to an integer
print("Hello", name, "you are", age, "years old!")
# Output: What is your name? David
#         What is your age? 30
#         Hello David you are 30 years old!
# Here, we use commas to separate the items in the print() function.
# This automatically adds spaces between the items in the output.
print("---------------------------------")


# -------------------------------------------------
# 5. Combining input with f-strings
# -------------------------------------------------
# Python also provides a convenient way to format strings using f-strings (formatted string literals).
# F-strings allow you to embed expressions inside string literals, using curly braces {}.
# This makes it easy to include variables and expressions in your strings.
# For example, you can use an f-string to greet the user like this:
name = input("What is your name? ")  # store input in a variable
print(f"Hello {name}!")  # use an f-string to format the output
# Output: What is your name? Charlie
#         Hello Charlie!
# Here, we use an f-string to include the variable `name` directly in the string.
# This makes the code cleaner and easier to read compared to string concatenation.
print("---------------------------------")


# -------------------------------------------------
# 6. Multiple inputs in one line
# -------------------------------------------------
# You can also take multiple inputs in one line by using the input() function with a prompt that asks for multiple values.
# For example, you can ask the user for their name and age in one line:
name, age = input("Enter your name and age (separated by a space): ").split()
# Here, we use the split() method to separate the input into two parts based on spaces.
print(f"Hello {name}, you are {age} years old!")
# Output: Enter your name and age (separated by a space): Jack 25
#         Hello Jack, you are 25 years old!
# In this example, we ask the user to enter their name and age in one line, separated by a space.
# The split() method splits the input string into a list of values, which we then unpack into the variables `name` and `age`.
# Note: Do not forget to use a comma between the variables in the input() function to unpack the values correctly. And ensure to use spaces to separate the inputs when the user types them.
print("---------------------------------")


# -------------------------------------------------
# Summary of Key Points
# -------------------------------------------------
# - The input() function lets the user type something during program execution.
# - You can use the prompt message inside input() to guide the user.
# - Whatever the user types is stored as a string (text) by default.
# - To work with numbers, convert the input using int() or float() to integer or float (decimal) types.
# - You can use commas in the print() function to separate multiple items. This allows you to print multiple values without needing to concatenate them.
# - You can combine input with f-strings or commas in print() for better output.
# - You can take multiple inputs in one line using the split() method.

# -------------------------------------------------