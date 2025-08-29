from threading import Thread

#Tuples
"""
- A tuple in Python is an ordered, immutable (unchangeable) collection of items.
- It is similar to a list, but once created, you cannot modify, add, or remove elements.
- Tuples are written with parentheses `()`.
- Tuples can contain elements of different data types, including numbers, strings, lists, other tuples, and even dictionaries.
- They are hashable (if all elements are hashable), making them suitable for use as dictionary keys or elements of a set.
- Tuples are faster and consume less memory compared to lists, making them ideal for read-only or fixed data.
"""
# creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5, True, (5, 6), [7, 8], {9: "nine"}, {10, 11})
print(my_tuple)  # Output: (1, 2, 3, 'hello', 4.5, True, (5, 6), [7, 8], {9: 'nine'}, {10, 11})
print(type(my_tuple))  # Output: <class 'tuple'>


# empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# single element tuple (comma required)
single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
"""
single_element_tuple = (1)
print(single_element_tuple) # Output: 1
print(type(single_element_tuple))  # Output: <class 'int'>
"""


# without parentheses (tuple packing)
packed_tuple = 1, 2, 3
print(packed_tuple)  # Output: (1, 2, 3)
print(type(packed_tuple))  # Output: <class 'tuple'>


# using the tuple() constructor
constructed_tuple = tuple([1, 2, 3, 4, 5])
print(constructed_tuple)  # Output: (1, 2, 3, 4, 5)
print(type(constructed_tuple))  # Output: <class 'tuple'>


# accessing tuple elements
num = (10, 20, 30, 40, 50)
print(num[0])  # Output: 10
print(num[1])  # Output: 20
print(num[-1])  # Output: 50 (last element)
print(num[1:4])  # Output: (20, 30, 40) (slicing)


# tuple immutability
immutable_tuple = (1, 2, 3)
# immutable_tuple[1] = 20  # This will raise a TypeError
print(immutable_tuple)  # Output: (1, 2, 3)
# However, if a tuple contains a mutable element (like a list), that element can be modified
mutable_element_tuple = (1, 2, [3, 4])
mutable_element_tuple[2][0] = 30
print(mutable_element_tuple)  # Output: (1, 2, [30, 4])



# tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6) (concatenation)


#repetition
tuple = (1, 2, 3)
print(tuple * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3) (repetition)


# membership test
tuple = (1, 2, 3)
print(2 in tuple)  # Output: True
print(5 not in tuple)  # Output: True
print(4 in tuple) # Output: False


# length of a tuple
tuple = (1, 2, 3, 4, 5)
print(len(tuple))  # Output: 5

# tuple methods
tuple = (1, 2, 3, 2, 4, 2, 5, 3)
print(tuple.count(2))  # Output: 3 (counts occurrences of 2)
print(tuple.index(3))  # Output: 2 (index of first occurrence of 3)
# Note: Tuples have only two built-in methods: count() and index().


# iterating over tuples
tuple = ("apple", "banana", "cherry")
for item in tuple:
    print(item)    # Output: apple banana cherry


# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)  # Output: (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3



# Tuple unpacking
tuple = (1, 2, 3)
a, b, c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# If there are more variables than values, you can use an asterisk (*) to collect the remaining values into a list
tuple = (1, 2, 3, 4, 5)
a, b, *rest = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3, 4, 5]
print(a, b, rest)  # Output: 1 2 [3, 4, 5]


# tuple vs list 
# Comparison: Tuple vs List
"""
| Feature    | Tuple                     | List                                    |
| ---------- | ------------------------- | --------------------------------------- |
| Syntax     | `( )`                     | `[ ]`                                   |
| Mutability | ❌ Immutable              | ✅ Mutable                             |
| Methods    | Only `count()`, `index()` | Many methods (`append`, `remove`, etc.) |
| Speed      | Faster (less memory)      | Slower                                  |
| Use case   | Fixed data                | Dynamic data                            |
| Performance| Better for read-only data | Better for frequent modifications       |
| Hashable   | ✅ Hashable (can be used as dict keys) | ❌ Not hashable (cannot be used as dict keys) |
"""

# Use Cases of Tuples

# 1. Returning multiple values from a function
def calculate(a, b):
    return a + b, a * b, a - b

result = calculate(10, 5)
print(result)  # Output: (15, 50, 5)

# 2. Using tuples as dictionary keys
location = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
print(location[(40.7128, -74.0060)])  # Output: New York

# 3. Storing fixed data
rgb_color = (255, 0, 0)  # Red color in RGB
print(rgb_color)  # Output: (255, 0, 0)

# 4. Using tuples in sets
unique_tuples = {(1, 2), (3, 4), (1, 2)}
print(unique_tuples)  # Output: {(1, 2), (3, 4)}

# 5. Tuple as a lightweight alternative to classes
person = ("John", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")
# Output: Name: John, Age: 30, Profession: Engineer

# 6. Immutable data for thread safety
# Tuples are immutable, making them safer to use in multithreaded environments.

shared_data = (1, 2, 3)

def print_data():
    print(shared_data)

thread1 = Thread(target=print_data)
thread2 = Thread(target=print_data)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# 7. Tuple for unpacking in loops
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
for name, score in students:
    print(f"{name} scored {score}")
# Output:
# Alice scored 85
# Bob scored 90
# Charlie scored 78








































































































