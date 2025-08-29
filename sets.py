#sets
"""
- A set is a collection data type in Python.
- Sets are unordered, meaning the items have no defined order.
- Sets are mutable, meaning you can add or remove items.
- Sets do not allow duplicate values.
- Sets are defined using curly braces `{}` or the `set()` constructor.
"""

# creating a set
my_set = {1, 2, 3, "hello", 4.5, True, (5, 6)}
print(my_set)  # Output: {1, 2, 3, 'hello', 4.5, True, (5, 6)}
print(type(my_set))  # Output: <class 'set'>

# empty set
empty_set = set()
print(empty_set)  # Output: set()

# with elements
set_with_elements = {1, 2, 3}
print(set_with_elements)  # Output: {1, 2, 3}
print(type(set_with_elements))  # Output: <class 'set'>

# duplicate are removed
set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(set_with_duplicates)  # Output: {1, 2, 3, 4, 5}

# using the set() constructor
set_from_list = set("hello")
print(set_from_list)  # Output: {'h', 'e', 'l', 'o'}

# accessing set items
items = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
print("5 in items:", 5 in items)  # Output: True
print("10 in items:", 10 in items)  # Output: False

# adding items to a set
set = {1, 2, 3}
set.add(4)
print(set)  # Output: {1, 2, 3, 4}
set.update([5, 6], {7, 8})
print(set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}


# removing items from a set
myset = {1, 2, 3, 4, 5}
myset.remove(3)  # raises KeyError if 3 not found
print(myset)  # Output: {1, 2, 4, 5}
myset.discard(4)  # does not raise error if 4 not found
print(myset)  # Output: {1, 2, 5}
popped_item = myset.pop()  # removes and returns an arbitrary item
print("Popped item:", popped_item)
print(myset)  # Output: remaining items
myset.clear()  # removes all items
print(myset)  # Output: set()
del myset  # deletes the set entirely

# set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}  (union)
print(set1 & set2)  # Output: {3}              (intersection)
print(set1 - set2)  # Output: {1, 2}           (difference)
print(set1 ^ set2)  # Output: {1, 2, 4, 5}     (symmetric difference)
print(set1 <= set2)  # Output: False            (subset)


# frozenset
# - A frozenset is an immutable version of a set.
# - Once created, elements cannot be added or removed from a frozenset.
# - Frozensets are hashable and can be used as keys in dictionaries or elements in other sets.
fs = frozenset([1, 2, 3, 4, 5])
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})
print(type(fs))  # Output: <class 'frozenset'>



"""
example of remove duplicates from a list
"""
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5]




"""
example of find commen student in two classes
"""
class_a = {"rajiv", "kartik", "nikunj"}
class_b = {"rajiv", "anand", "rahul"}
print(class_a & class_b)  # Output: {'rajiv'}
print(class_a.intersection(class_b))  # Output: {'rajiv'}































