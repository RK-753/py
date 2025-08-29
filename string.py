#String   <--'hello' is the same as "hello"

print("hello")   #print hello
print('hello')   #print hello

print("""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,                
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""")        # <--multi line string

s = "Hello"
print(s[0])          #print H
print(s[1])          #print e


print("Hello" + " " + "World")           #print Hello World

print("hi" * 3)       #print hihihi


s = "Python"
print(s[0])   #print P
print(s[-1])  #print n

s = "Python"
print(s[0:4])  #print Pyth

name = "Alice"
age = 25
print(f"My name is {name} and I am {age}")    #print My name is Alice and I am 25

a = "Hello, World!"
print(len(a))          #print 13


# Slicing Strings
b = "Hello, World!"
print(b[2:5])       #print llo

b = "Hello, World!"
print(b[:5])        #print Hello

b = "Hello, World!"
print(b[2:])        #print llo, World!

b = "Hello, World!"
print(b[-5:-2])      #print orl

#Modify Strings
a = "Hello, World!"
print(a.upper())        #print HELLO, WORLD!

a = "Hello, World!"
print(a.lower())        #print hello, world!

a = " Hello, World! "
print(a.strip())       #print Hello, World!  <-- removes whitespace from the beginning or the end

a = "Hello, World!"
print(a.replace("H", "J"))   #print Jello, World!

a = "Hello, World!"
print(a.split(","))        #print ['Hello', ' World!']  <-- returns ['Hello', ' World!']

#format Strings
age = 18
txt = "My name is Rajiv, and I am {}"
print(txt.format(age))      #print My name is Rajiv, and I am 18

#F-Strings
name = "Rajiv"
age = 18
txt = f"My name is {name}, and I am {age}"
print(txt)                 #print My name is Rajiv, and I am 18

txt = f"The price is {20 * 59} dollars"
print(txt)                 #print The price is 1180 dollars

#escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)                 #print We are the so-called "Vikings" from the north.  <--The escape character allows you to use double quotes when you normally would not be allowed:
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""















