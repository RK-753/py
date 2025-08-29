# Boolean Examples in Python

# Comparison Operators
print(10 > 9)   # True: 10 is greater than 9
print(10 == 9)  # False: 10 is not equal to 9
print(10 < 9)   # False: 10 is not less than 9
print(10 >= 9)  # True: 10 is greater than or equal to 9
print(10 <= 9)  # False: 10 is not less than or equal to 9
print(10 != 9)  # True: 10 is not equal to 9

# Boolean Values of Different Data Types
print(bool("Hello"))  # True: Non-empty string
print(bool(15))       # True: Non-zero integer
print(bool(0))        # False: Zero is considered False
print(bool(""))       # False: Empty string
print(bool(None))     # False: None is considered False
print(bool(False))    # False: Explicit False value
print(bool(True))     # True: Explicit True value

# Boolean Values of Collections
print(bool([]))       # False: Empty list
print(bool({}))       # False: Empty dictionary
print(bool(()))       # False: Empty tuple
print(bool([1, 2, 3]))  # True: Non-empty list
print(bool({"name": "John", "age": 36}))  # True: Non-empty dictionary
print(bool((1, 2, 3)))  # True: Non-empty tuple
print(bool(set()))     # False: Empty set
print(bool({1, 2, 3}))  # True: Non-empty set

# Boolean Values of Other Data Types
print(bool(3.14))     # True: Non-zero float
print(bool(range(0)))  # False: Empty range
print(bool(range(3)))  # True: Non-empty range
