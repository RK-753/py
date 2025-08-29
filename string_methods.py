# String Methods in Python

# title() - Capitalizes the first letter of each word in the string
text = "hello world"
result = text.title()
print(result)  # Output: Hello World (First letter of each word is capitalized)

# capitalize() - Capitalizes the first letter of the string and makes the rest lowercase
text = "HeLlo woRld"
result = text.capitalize()
print(result)  # Output: Hello world (First letter of the string is capitalized, rest are lowercase)

# swapcase() - Swaps uppercase letters to lowercase and vice versa
text = "Hello WoRld"
result = text.swapcase()
print(result)  # Output: hELLO wOrLD (Uppercase to lowercase and vice versa)

# find() - Returns the index of the first occurrence of a substring, or -1 if not found
text = "Hello world"
print(text.find("world"))  # Output: 6 (Index of the first occurrence of "world")
print(text.find("Python"))  # Output: -1 (Substring not found)

# find() with start index - Searches for the substring starting from a specific index
text = "Hello world, welcome to the world"
print(text.find("world", 10))  # Output: 19 (Search starts at index 10)
print(text.find("world", 20))  # Output: -1 (Substring not found after index 20)

# rfind() - Returns the highest index of the substring, or -1 if not found
print(text.rfind("world"))  # Output: 21 (Highest index of "world")
print(text.rfind("Python"))  # Output: -1 (Substring not found)

# index() - Similar to find(), but raises ValueError if the substring is not found
text = "Hello world"
print(text.index("world"))  # Output: 6 (Index of the first occurrence of "world")
# print(text.index("Python"))  # Raises ValueError: substring not found

# rindex() - Similar to rfind(), but raises ValueError if the substring is not found
text = "Hello world, welcome to the world"
print(text.rindex("world"))  # Output: 21 (Highest index of "world")
# print(text.rindex("Python"))  # Raises ValueError: substring not found

# startswith() - Checks if the string starts with the specified prefix
text = "Hello world"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("world"))  # Output: False

# endswith() - Checks if the string ends with the specified suffix
print(text.endswith("world"))  # Output: True
print(text.endswith("Hello"))  # Output: False

# replace() - Replaces occurrences of a substring with another substring
text = "Hello world"
result = text.replace("world", "Python")
print(result)  # Output: Hello Python

# strip(), lstrip(), rstrip() - Removes leading/trailing whitespace or specified characters
text = "   Hello world   "
print(text.strip())   # Output: Hello world (Removes leading and trailing spaces)
print(text.lstrip())  # Output: "Hello world   " (Removes leading spaces)
print(text.rstrip())  # Output: "   Hello world" (Removes trailing spaces)

# split() and rsplit() - Splits the string into a list based on a delimiter
text = "Hello,world,Python"
print(text.split(","))  # Output: ['Hello', 'world', 'Python'] (Splits from the left)
print(text.rsplit(",", 1))  # Output: ['Hello,world', 'Python'] (Splits from the right)

# splitlines() - Splits the string into a list at line breaks
text = "Hello world\nWelcome to Python\nEnjoy coding"
print(text.splitlines())  # Output: ['Hello world', 'Welcome to Python', 'Enjoy coding']

# partition() and rpartition() - Splits the string into a tuple at the first/last occurrence of a separator
text = "Hello world, welcome to Python"
print(text.partition("welcome"))  # Output: ('Hello world, ', 'welcome', ' to Python')
print(text.rpartition("welcome"))  # Output: ('Hello world, ', 'welcome', ' to Python')

# join() - Joins elements of an iterable into a single string with a specified separator
mylist = ["Hello", "world", "Python"]
print(" ".join(mylist))  # Output: Hello world Python

# isalnum(), isalpha(), isdigit(), isnumeric(), isdecimal() - String checks for specific properties
text = "Hello123"
print(text.isalnum())  # Output: True (Alphanumeric check)
print(text.isalpha())  # Output: False (Alphabetic check)
print("12345".isdigit())  # Output: True (Digit check)
print("½".isnumeric())  # Output: True (Numeric check)
print("12345".isdecimal())  # Output: True (Decimal check)

# isspace(), islower(), isupper(), istitle() - String checks for whitespace, case, and title case
print("   ".isspace())  # Output: True (Whitespace check)
print("hello".islower())  # Output: True (Lowercase check)
print("HELLO".isupper())  # Output: True (Uppercase check)
print("Hello World".istitle())  # Output: True (Title case check)

# isascii() - Checks if all characters in the string are ASCII
print("Hello".isascii())  # Output: True
print("Helloñ".isascii())  # Output: False

# center(), ljust(), rjust() - Aligns the string within a specified width using a fill character
text = "Hello"
print(text.center(20, "*"))  # Output: *******Hello******** (Centers the string)
print(text.ljust(20, "*"))   # Output: Hello*************** (Left-aligns the string)
print(text.rjust(20, "*"))   # Output: ***************Hello (Right-aligns the string)

# zfill() - Pads the string with zeros on the left to fill the specified width
text = "42"
print(text.zfill(10))  # Output: 0000000042

# format() and format_map() - Formats strings using placeholders
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Using format()
person = {"name": "Bob", "age": 25}
print("My name is {name} and I am {age} years old.".format_map(person))  # Using format_map()

# f-strings (Python 3.6+) - String interpolation using variables
name = "Charlie"
age = 35
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Charlie and I am 35 years old.

# encode() - Encodes the string into bytes using the default or specified encoding
text = "Hello world"
print(text.encode())  # Output: b'Hello world'

# maketrans() and translate() - Creates a translation table and translates the string
text = "hello world"
translation_table = text.maketrans("hel", "HEL", "o")  # Maps 'h'->'H', 'e'->'E', 'l'->'L', and removes 'o'
print(text.translate(translation_table))  # Output: HELL wrLd

# count() - Counts the occurrences of a substring in the string
text = "hello world, welcome to the world"
print(text.count("world"))  # Output: 2

# expandtabs() - Replaces tabs in the string with spaces of a specified width
text = "Hello\tworld\tPython"
print(text.expandtabs(4))  # Output: Hello   world   Python

# casefold() - Converts the string to lowercase for case-insensitive comparisons
text = "HELLO WORLD"
print(text.casefold())  # Output: hello world

# removeprefix() and removesuffix() (Python 3.9+) - Removes a prefix or suffix from the string
text = "Hello world"
print(text.removeprefix("Hello "))  # Output: world
print(text.removesuffix(" world"))  # Output: Hello

# Global Variables - Demonstrates the use of global variables and the global keyword
x = "awesome"  # Global Variable
def myglobalfunc():
    global x  # Global Keyword
    x = "fantastic"
    print("Python is " + x)  # Output: Python is fantastic (inside function)

myglobalfunc()
print("Python is " + x)  # Output: Python is fantastic (outside function)
