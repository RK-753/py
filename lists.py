# Lists in Python
"""
A list in Python is:
- Ordered: Elements have a defined order.
- Mutable: Elements can be changed after the list is created.
- Heterogeneous: Can contain mixed data types.
- Indexed: Elements can be accessed using their index.
- Allows duplicates: Can contain duplicate elements.

Lists are defined using square brackets [].
"""

# Example of a list with mixed data types
my_list = [1, 2, 3, "hello", 4.5, True, [5, 6], (7, 8), {9: "nine"}, {10, 11}]
print(my_list)  # Output: [1, 2, 3, 'hello', 4.5, True, [5, 6], (7, 8), {9: 'nine'}, {10, 11}]
print(type(my_list))  # Output: <class 'list'>

# Creating different types of lists
empty_list = []  # Empty list
numbers = [1, 2, 3, 4, 5]  # List of numbers
mixed_list = [1, "two", 3.0, True]  # Mixed data types
nested_list = [1, 2, [3, 4], [5, 6]]  # Nested list (list inside a list)

# Printing the lists
print(empty_list)  # Output: []
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed_list)  # Output: [1, 'two', 3.0, True]
print(nested_list)  # Output: [1, 2, [3, 4], [5, 6]]

# Accessing list elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print(fruits[-1])  # Output: cherry (last element)

# Modifying list elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
fruits[1:3] = ["kiwi", "mango"]
print(fruits)  # Output: ['apple', 'kiwi', 'mango']

# Adding elements to a list
fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds an element at the end
fruits.insert(1, "blueberry")  # Adds an element at a specific index
fruits.extend(["date", "elderberry"])  # Adds multiple elements at the end
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# Removing elements from a list
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")  # Removes the first occurrence of a value
popped_fruit = fruits.pop()  # Removes and returns the last element
fruits.pop(0)  # Removes and returns the element at the specified index
del fruits[0]  # Deletes the element at the specified index
print(fruits)  # Output: []

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # Concatenation
repeated_list = list1 * 3  # Repetition
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(2 in list1)  # Membership test, Output: True
print(5 not in list1)  # Membership test, Output: True

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Output: [2, 3, 4]
print(numbers[:4])  # Output: [0, 1, 2, 3]
print(numbers[5:])  # Output: [5, 6, 7, 8, 9]
print(numbers[-3:])  # Output: [7, 8, 9]
print(numbers[::2])  # Output: [0, 2, 4, 6, 8]
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# List methods
fruits = ["apple", "banana", "cherry", "date", "banana"]
fruits.clear()  # Removes all elements
print(fruits)  # Output: []

fruits = ["apple", "banana", "cherry", "date", "banana"]
print(fruits.index("banana"))  # Returns the index of the first occurrence, Output: 1
print(fruits.count("banana"))  # Returns the number of occurrences, Output: 2

fruits = ["apple", "banana", "cherry", "date", "mango", "fig"]
fruits.sort()  # Sorts the list in ascending order
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'fig', 'mango']
fruits.reverse()  # Reverses the order of the list
print(fruits)  # Output: ['mango', 'fig', 'date', 'cherry', 'banana', 'apple']

copied_fruits = fruits.copy()  # Creates a shallow copy of the list
print(copied_fruits)  # Output: ['mango', 'fig', 'date', 'cherry', 'banana', 'apple']

# List comprehension
squares = [x**2 for x in range(10)]  # List of squares from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]  # List of even numbers from 0 to 9
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(evens)  # Output: [0, 2, 4, 6, 8]


# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # Output: [1, 2, 3]
print(matrix[1][2])  # Output: 6
print(matrix[2][0])  # Output: 7


# list construction using list()
list_from_string = list("hello")  # Converts a string to a list of characters
print(list_from_string)  # Output: ['h', 'e', 'l', 'l', 'o']


#Loop Through the Index Numbers
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])     #output: apple banana cherry      








































