#variable
x = 5
y = "Rajiv"
print(x)
print(y)

x = 6                  # x is now of type int
x = "Hello python"     # x is now of type str
print(x)               #print Hello python

x = str(3)    
y = int(3)            #<--  this is Casting
z = float(3)
print(x)              #print 3
print(y)              #print 3
print(z)              #print 3.0

x, y, z = "Orange", "Banana", "Cherry"  #<--  this is Multiple Variables
print(x)              #print Orange
print(y)              #print Banana
print(z)              #print Cherry

x = y = z = "Orange"  #<--  this is One Value to Multiple Variables
print(x)              #print Orange

x = "python"
y = "is"
z = "awesome"
print(x, y, z)        #print python is awesome  

x = "my"
y = "name"
z = "Rajiv"
print(x +" "+ y + " " + z)  #print my name Rajiv
