#arithmatic operators
"""
| Operator | Description                     | Example             |
| -------- | ------------------------------- | ------------------- |
| `+`      | Addition                        | `10 + 5 = 15`       |
| `-`      | Subtraction                     | `10 - 5 = 5`        |
| `*`      | Multiplication                  | `10 * 5 = 50`       |
| `/`      | Division (float result)         | `10 / 3 = 3.333...` |
| `//`     | Floor Division (integer result) | `10 // 3 = 3`       |
| `%`      | Modulus (remainder)             | `10 % 3 = 1`        |
| `**`     | Exponentiation (power)          | `2 ** 3 = 8`        |

"""

x = 10
y = 4
print(x + y)  # Output: 14 (Addition)
print(x - y)  # Output: 6 (Subtraction)
print(x * y)  # Output: 40 (Multiplication)
print(x / y)  # Output: 2.5 (Division)
print(x // y) # Output: 2 (Floor Division)
print(x % y)  # Output: 2 (Modulus)
print(x ** y) # Output: 10000 (Exponentiation)

#Comparison (relation) operators
"""
| Operator | Description              | Example           |
| -------- | ------------------------ | ----------------- |
| `==`     | Equal to                 | `10 == 5 → False` |
| `!=`     | Not equal to             | `10 != 5 → True`  |
| `>`      | Greater than             | `10 > 5 → True`   |
| `<`      | Less than                | `10 < 5 → False`  |
| `>=`     | Greater than or equal to | `10 >= 10 → True` |
| `<=`     | Less than or equal to    | `5 <= 10 → True`  |

"""

x = 10
y = 4
print(x == y)  # Output: False (Equal to)
print(x != y)  # Output: True (Not equal to)
print(x > y)   # Output: True (Greater than)
print(x < y)   # Output: False (Less than)
print(x >= y)  # Output: True (Greater than or equal to)
print(x <= y)  # Output: False (Less than or equal to)


#logical operators
"""
| Operator | Description                                | Example                     |
| -------- | ------------------------------------------ | --------------------------- |
| `and`    | True if **both** conditions are true       | `(10 > 5 and 5 > 2) → True` |
| `or`     | True if **at least one** condition is true | `(10 > 5 or 2 > 5) → True`  |
| `not`    | Reverses the result                        | `not(10 > 5) → False`       |

"""
x = True
y = False
print(x and y)  # Output: False (Both conditions must be true)
print(x or y)   # Output: True (At least one condition is true)
print(not x)    # Output: False (Reverses the result)
print(not y)    # Output: True (Reverses the result)

#assignment operators
""" 
| Operator | Example   | Equivalent To |                     
| -------- | --------- | ------------- | 
| `=`      | `x = 5`   | `x = 5`       |                    
| `+=`     | `x += 3`  | `x = x + 3`   |                     
| `-=`     | `x -= 3`  | `x = x - 3`   |                     
| `*=`     | `x *= 3`  | `x = x * 3`   |                     
| `/=`     | `x /= 3`  | `x = x / 3`   |                    
| `//=`    | `x //= 3` | `x = x // 3`  |                     
| `%=`     | `x %= 3`  | `x = x % 3`   |                     
| `**=`    | `x **= 3` | `x = x ** 3`  |                     
| `&=`     | `x &= 3`  | `x = x & 3`   |                     
| `|=`     | `x |=3`   | `x = x | 3`   | 
| `^=`     | `x ^= 3`  | `x = x ^ 3`   |      
| `>>=`    | `x >>= 3` | `x = x >> 3`  |       
| `<<=`    | `x <<= 3` | `x = x << 3`  |                     
"""
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 12
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 24
x /= 4  # Equivalent to x = x / 4
print(x)  # Output: 6.0
x //= 2  # Equivalent to x = x // 2
print(x)  # Output: 3.0
x %= 2  # Equivalent to x = x % 2
print(x)  # Output: 1.0
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 1.0
x = 10
x &= 3  # Equivalent to x = x & 3
print(x)  # Output: 2
x |= 3  # Equivalent to x = x | 3
print(x)  # Output: 3
x ^= 2  # Equivalent to x = x ^ 2
print(x)  # Output: 1
x >>= 1  # Equivalent to x = x >> 1
print(x)  # Output: 0
x <<= 2  # Equivalent to x = x << 2
print(x)  # Output: 0

#bitwise operators
"""
| Operator | Description        | Example                             |                                  
| -------- | ------------------ | ----------------------------------  |
| `&`      | AND                | `5 & 3 = 1` (`0101 & 0011 = 0001`)  |                                      
| `|`      | OR                 | `5 \| 3 = 7` (`0101 \| 0011 = 0111`)|                          
| `^`      | XOR (exclusive OR) | `5 ^ 3 = 6` (`0101 ^ 0011 = 0110`)  |                                      
| `~`      | NOT (invert bits)  | `~5 = -6`                           |                                      
| `<<`     | Left Shift         | `5 << 1 = 10`                       |                                      
| `>>`     | Right Shift        | `5 >> 1 = 2`                        |                                      

"""
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x & y)  # Output: 1 (AND: 0101 & 0011 = 0001)
print(x | y)  # Output: 7 (OR: 0101 | 0011 = 0111)
print(x ^ y)  # Output: 6 (XOR: 0101 ^
print(~x)     # Output: -6 (NOT: ~0101 = 1010 in two's complement)
print(x << 1) # Output: 10 (Left Shift: 0101 << 1 = 1010)
print(x >> 1) # Output: 2 (Right Shift: 0101 >> 1 = 0010)

#identity operators
"""
| Operator | Description                                 | Example      |
| -------- | ------------------------------------------- | ------------ |
| `is`     | True if both variables point to same object | `x is y`     |
| `is not` | True if they are different objects          | `x is not y` |
"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)      # Output: False (Different objects)
print(x is z)      # Output: True (Same object)
print(x is not y)  # Output: True (Different objects)
print(x is not z)  # Output: False (Same object)
print(y is not z)  # Output: True (Different objects)


#membership operators
"""
| Operator | Description                      | Example                     |
| -------- | -------------------------------- | --------------------------- |
| `in`     | True if value exists in sequence | `"a" in "apple" → True`     |
| `not in` | True if value does not exist     | `"b" not in "apple" → True` |
"""
x = "hello"
print("h" in x)      # Output: True (Character 'h' is in the string)
print("z" in x)      # Output: False (Character 'z' is not
print("h" not in x)  # Output: False (Character 'h' is in the string)
print("z" not in x)  # Output: True (Character 'z' is not in the string)

#special operators
"""
| Operator | Description                     | Example                |
| -------- | ------------------------------- | ---------------------- |
| `:=`     | Assignment expression (walrus)  | `if (n := len(x)) > 5` |
"""
x = "hello world"
if (n := len(x)) > 5:
    print(f"String is too long ({n} characters).") # Output: String is too long (11 characters).


























































