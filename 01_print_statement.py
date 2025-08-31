# Lesson 1: The print() Statement
# --------------------------------
# In this lesson, you will learn how to use Python's print() function.
#
# The print() function is used to display output of a program to the console/terminal (screen).
# It’s one of the most commonly used functions in Python.
# You can print strings (texts), numbers, and even variables.
# The basic syntax of the print() function is:
# Syntax:
#   print(value1, value2, ..., valueN)


# -------------------------------------------------
# 1. Printing text (called a "string")
# -------------------------------------------------
# Strings are written inside quotes:
# - Double quotes: "Hello"
# - Single quotes: 'Hello'
print("Hello, Python!")   # using double quotes
# Output: Hello, Python!
print('Hello, Python!')   # using single quotes
# Output: Hello, Python!
# (Both work the same, but be consistent for readability.)
print("---------------------------------")


# -------------------------------------------------
# 2. Printing numbers
# -------------------------------------------------
# Numbers don't need quotes.
print(2025)
# Output: 2025
# Python automatically converts numbers to strings when printing.
print("---------------------------------")


# -------------------------------------------------
# 3. Printing multiple values
# -------------------------------------------------
# Use commas ( , ) between values.
print("The year is", "perfect!")  # prints strings
# Output: The year is perfect!
print("The year is", 2025)  # prints strings and number together
# Output: The year is 2025
# You can mix strings and numbers in the same print statement.
# Python adds a space automatically between values.
print("---------------------------------")


# -------------------------------------------------
# 4. Controlling spaces between values (sep)
# -------------------------------------------------
print("Hello", "World")          # default: Hello World
# Output: Hello World
print("Hello", "World", sep="")  # no space
# Output: HelloWorld
print("Hello", "World", sep=" ") # space added
# Output: Hello World
print("Hello", "World", sep="-") # custom separator
# Output: Hello-World
# The sep parameter controls how values are separated in the output.
# You can use any string as a separator, including empty strings.
print("---------------------------------")


# -------------------------------------------------
# 5. Joining strings together (concatenation)
# -------------------------------------------------
# Concatenation means combining strings.
# Use the + operator to concatenate strings.
print("Hello" + "World!")       # no space
# Output: HelloWorld!
# Concatenation combines strings into one. 
# Remember to add spaces manually if needed.
print("Hello" + " " + "World!") # space added manually
# Output: Hello World!
# You can also concatenate strings with numbers, but numbers must be converted to strings first.
# We can use str() to convert numbers to strings.
print("The year is " + str(2025))  # converting number to string
# Output: The year is 2025
#
# ..................
# Why do we need string concatenation?
# Concatenation refers to the process of combining two or more strings into a single, new string.
# Concatenation is especially useful when you want to include variable values in your output.
# For example, you can create a message that includes a variable value:
year = 2025                                # variable 'year' holding a number
print("The current year is " + str(year))  # Concatenating a string with a variable
# Output: The current year is 2025
# Concatenation is also useful for creating dynamic messages based on user input or program state.
print("Hello, " + input("What is your name? ") + "!")  # Asking for user input
# When you run this code, it will ask you for an input.
# After you enter your name, it will print a personalized greeting.
# For example, if you enter "Alice", it will print: Hello, Alice!
# This demonstrates how concatenation can be used to create dynamic and personalized messages. 
# This allows you to create personalized messages based on user input.
# Concatenation is a fundamental concept in programming and is widely used in various applications.
# You"ll understand more about variables and input() and how to use them in future lessons.
print("---------------------------------")


# -------------------------------------------------
# 6. New lines (\n) and tabs (\t)
# -------------------------------------------------
print("Line 1\nLine 2")         # \n = newline
# Output: Line 1
#         Line 2
print("Item 1\tItem 2")         # \t = tab space
# Output: Item 1    Item 2
# The \n character creates a new line, while \t adds a tab space.
# These are called escape sequences and are used to format text output.
print("---------------------------------")


# -------------------------------------------------
# 7. Ending a print differently (end)
# -------------------------------------------------
# By default, print() ends with a newline.
# Use end="" to change it.
print("Hello", end=" ")
print("there!") # same line
# Output: Hello there!
# The end parameter allows you to specify what to print at the end of the output.
# You can use it to avoid new lines or add custom endings.
print("Hello", end="...")  # custom ending
print("World!")            
# Output: Hello...World!
# You can use any string as the end character, including empty strings.
# You can also use end="" to avoid a newline at the end of the print statement.
print("---------------------------------")


# -------------------------------------------------
# 8. Preserving spaces inside strings
# -------------------------------------------------
print("  surrounded by spaces  ") # spaces are kept as they are
# Output:   surrounded by spaces
# Python preserves spaces inside strings, so leading and trailing spaces are kept.
# This is useful when you want to maintain formatting in your output.
print("---------------------------------")


# -------------------------------------------------
# 9. Printing special characters
# ------------------------------------------------- 
print("\"Hello\"")  # using backslash to escape quotes
# Output: "Hello"
print('\'Hello\'')  # using backslash to escape quotes
# Output: 'Hello'
# Use a backslash (\) to escape special characters like quotes inside strings.
# This allows you to include quotes without ending the string prematurely.
# You can also escape other special characters like backslashes themselves.
print("This is a backslash: \\")  # escaping a backslash
# Output: This is a backslash: \
print("---------------------------------")


# -------------------------------------------------
# 10. Printing formatted strings (f-strings)
# -------------------------------------------------
# F-strings allow you to embed expressions inside string literals.
name = "Alice" # variable holding a name
age = 30       # variable holding an age
print(f"My name is {name} and I am {age} years old.") # using f-string
# Output: My name is Alice and I am 30 years old.
# F-strings are a powerful way to format strings in Python.
# They allow you to include variables and expressions directly in the string.
# You can use curly braces {} to include variables or expressions inside the string.
# This makes it easy to create dynamic messages based on variable values.
# F-strings are prefixed with 'f' or 'F'.
# F-strings are available in Python 3.6 and later.
print("---------------------------------")


# -------------------------------------------------
# Summary of Key Points
# -------------------------------------------------
# - The print() function is used to display output.
# - You can print strings, numbers, and variables.
# - Strings can be written in single or double quotes.
# - Numbers are written without quotes.
# - Use commas to print multiple values with spaces.
# - The sep parameter is used to control spaces between values.
# - Concatenation combines strings using the + operator (convert numbers with str() if needed).
# - Use escape sequences like \n and \t for formatting, where \n adds a new line; \t adds a tab.
# - Use the end parameter to change the ending of the print statement.
# - Spaces inside quotes are preserved.
# - Use backslashes to escape special characters like quotes and backslashes.
# - Use f-strings for formatted strings with variables.

# -------------------------------------------------