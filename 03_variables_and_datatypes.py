# Lesson 3: Variables & Data Types
# ---------------------------------
# In this lesson, we will learn what variables are, why we use them, and the different types of data we can store in Python.


# -------------------------------------------------
# 1. What is a variable?
# -------------------------------------------------
# A variable is a named location in memory that stores a value.
# Variables allow us to store data and refer to it by name, making our code more readable and maintainable.
# You can imagine variable like a container (or a box) that holds a value.
# Instead of using the value directly, we give it a name and store it inside a variable, so we can reuse it later in our program.
#
# Think of it as a label on a jar: the jar contains the value, and the label (variable name) tells us what’s inside.
#
# Example:
name = "Alice"   # storing a string in a variable
age = 25         # storing a number in a variable
print(f"Name: {name}")
print(f"Age: {age}")
# Output: Name: Alice
#         Age: 25
print("---------------------------------")


# -------------------------------------------------
# 2. Why use variables?
# -------------------------------------------------
# Variables make our code more flexible and easier to read.
# Instead of hardcoding values, we can use variables to store them.
# This allows us to change the value in one place without having to search through our code.
# For example, if we want to change the name from "Alice" to "Bob", we only need to change it in one place:
name = "Bob"
print(f"Updated Name: {name}")
# Output: Updated Name: Bob
print("---------------------------------")


# -------------------------------------------------
# 3. Reassignment and dynamic typing
# -------------------------------------------------
# In Python, you can reassign a variable to a new value.
# This is known as reassignment.
value = 10                  # int
print(value, type(value))
value = "ten"               # now a string
print(value, type(value))
# Output: 10 <class 'int'>
#         ten <class'str'>
# Dynamic typing is a feature of Python where the type of a variable is determined at runtime (when it's being executed) unlike other languages.
# This means that a variable can hold different types of data at different times.
# This makes Python a great language for scripting, data analysis, and web development.
print("---------------------------------")


# -------------------------------------------------
# 4. Multiple assignment
# -------------------------------------------------
# In Python, you can assign multiple values to multiple variables simultaneously.
x, y, z = 10, 20, 30    # where x = 10, y = 20, z = 30
print(x, y, z)
# Output: 10 20 30
# Note: In some other languages, you can only assign a single value to a variable at a time.
# In Python, you can use multiple assignment to swap values between two variables:
x, y = y, x    # Swapping values
print(x, y)
# Output: 20 10
print("---------------------------------")


# -------------------------------------------------
# 5. Rules for naming variables
# -------------------------------------------------
# - Variable names can only contain letters, numbers, and underscores (_).
# - They cannot start with a number.
# - They cannot be a reserved keyword (like "for", "if", "while").
# - Use descriptive names for clarity.
# Python is case-sensitive: "Name" and "name" are different variables.
#
# Example of valid names:
user_name = "Bob"
userAge = 30
#
# Example of invalid names (do not try to run these):
# 2name = "Error"
# for = "Error"


# -------------------------------------------------
# 6. Combining strings with variables
# -------------------------------------------------
# When printing variables with text, you can:
# - Use commas in print() (adds spaces automatically)
# - Use string concatenation (+) if variables are strings
# - Use f-strings for a cleaner style
# Examples:
name = "John"
age = 21
#
# Using commas:
print("Hello,", name, "your age is", age)  
# Output: Hello, John your age is 21          
# When using commas, Python automatically adds spaces between the items so you don't need to worry about spacing.
# Even if you wrote the print statement like this:
print("Hello,",name,"your age is",age)  # Without spaces after commas
# Output: Hello, John your age is 21    # You still get spaces between the words.
#
# While using string concatenation (make sure to convert non-string types):
# Using concatenation (both must be strings):
print("Hello " + name + ", your age is " + str(age))
# Output: Hello John, your age is 21
# Don't forget to add spaces manually when using concatenation, as it does not add spaces automatically.
#
# Using f-strings:
print(f"Hello {name}, your age is {age}")
# Output: Hello John, your age is 21
print("---------------------------------")


# -------------------------------------------------
# 7. Data Types in Python
# -------------------------------------------------
# A data type tells Python what kind of value is stored in a variable.

# Python is dynamically typed, meaning we don't need to declare the type of a variable when we create it.
# The type is determined automatically based on the value assigned to the variable.
# [The above line is a bit advanced, you can skip it for now if you're new to programming. But in general, it means that Python figures out the type of a variable on its own when you assign a value to it, unlike the other languages where you have to specify the type of the variable explicitly.]
#
# For example, if we assign a number to a variable, Python knows it's an integer or float, and if we assign a string, it knows it's a string. But in some other programming language like C or Java, you have to specify the type of the variable when you declare it.
#
# Let's see some examples:
#
# In C:
# int age = 25; // Here, we specify that 'age' is an integer.
# In Java:
# String name = "Alice"; // Here, we specify that 'name' is a string.
# In Python, we simply write:
age = 25 # Python automatically knows 'age' is an integer.
name = "Alice"  # Python automatically knows 'name' is a string and 'age' is an integer.
#
# Python has several built-in data types that we can use to store different kinds of values.
# Common data types you will use often:
# 1. String (str) - text values (inside quotes " " or ' ')
# 2. Integer (int) - whole numbers (positive or negative)
# 3. Float (float) - decimal numbers
# 4. Boolean (bool) - True or False values
#
# Examples:
text_value = "Hello"        # string
integer_value = 10          # integer
float_value = 3.14          # float
boolean_value = True        # boolean
print(f"Text: {text_value}")
print(f"Integer: {integer_value}")
print(f"Float: {float_value}")
print(f"Boolean: {boolean_value}")
# Output: Text: Hello
#         Integer: 10
#         Float: 3.14
#         Boolean: True
print("---------------------------------")


# -------------------------------------------------
# 9. Type Conversion
# -------------------------------------------------
# Sometimes, we need to convert one data type to another.
# For example, converting a string to an integer or a float.
# Python provides built-in functions for type conversion:
# - `int()` to convert to integer
# - `float()` to convert to float
# - `str()` to convert to string
#
# Example:
number_str = "42" # string representation of a number
number_int = int(number_str)  # converting string to integer
print(f"Converted Integer: {number_int}")
# Output: Converted Integer: 42
# If we try to convert a string that doesn't represent a number, it will raise an error:
# invalid_str = "Hello"
# invalid_int = int(invalid_str)  # This will raise a ValueError
# Uncomment the above lines to see the error in action.
# To avoid errors, ensure the string can be converted to the desired type.
#
# You can also convert numbers, like float to integer:
number_float = 3.99
number_int_from_float = int(number_float)  # converting float to integer
print(f"Converted Integer from Float: {number_int_from_float}")
# Output: Converted Integer from Float: 3
# Note that converting a float to an int truncates the decimal part.
print("---------------------------------")


# -------------------------------------------------
# 10. Checking the type of a variable
# -------------------------------------------------
# You can check what type of data a variable holds using the type() function.
#
# Examples:
text_value = "Hello!"        # string
integer_value = 13           # integer
float_value = 9.2            # float
boolean_value = False        # boolean
print(f"Type of text_value: {type(text_value)}")      
# Output: Type of text_value: <class 'str'>
print(f"Type of integer_value: {type(integer_value)}")  
# Output: Type of integer_value: <class 'int'>
print(f"Type of float_value: {type(float_value)}")  
# Output: Type of float_value: <class 'float'>
print(f"Type of boolean_value: {type(boolean_value)}")
# Output: Type of boolean_value: <class 'bool'>
print("---------------------------------")


# -------------------------------------------------
# 11. Practice Exercise
# -------------------------------------------------
# Create a Band name generator using variables and string operations.
#
# # Let's use what we've learned so far to create a simple Band Name Generator.
# # The program will ask the user for the city they grew up in and their pet's name, then combine these to suggest a band name.
print("Welcome to the Band Name Generator!")

city = input("Enter the city you grew up in: ")    # Get user input for city
pet = input("Enter your pet's name: ")             # Get user input for pet's name

band_name = city + " " + pet                       # Combine city and pet name to create band name

print(f"Your band name could be: " + band_name)     # Display the generated band name
# Example Output: Welcome to the Band Name Generator!
#                 Enter the city you grew up in: New York
#                 Enter your pet's name: Buddy
#                 Your band name could be: New York Buddy 
print("---------------------------------")


# -------------------------------------------------
# 12. Summary
# -------------------------------------------------
# - Variables are named locations in memory that store values.
# - They are like containers for data that holds a value. Instead of using the value directly, we give it a name and store it inside a variable, so we can reuse it later in our program.
# - They make code more readable and maintainable.
# - Follow naming rules for variables (letters, numbers, underscores, no keywords, no starting with numbers).
# - Common data types: str (text), int (whole numbers), float (decimals), bool (True/False).
# - Variables can change values, and we can convert between types using functions like int(), float(), and str().
# - Use type() to check what type of value a variable holds.
# - You can combine variables with text using commas, + (concatenation), or f-strings.

# -------------------------------------
