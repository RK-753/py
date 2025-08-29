
#Global Variables
x = "awesome"        #<--  this is Global Variable
def myfunc():
  print("python is " + x)  #print python is awesome  <--inside function
myfunc()
print("python is " + x)    #print python is awesome  <--outside function


x = 5
def mychangefunc():
  x = 10               #<--  this is Local Variable
  print(x)            #print 10  <--inside function
mychangefunc()
print(x)              #print 5   <--outside function


x = 8
def myglobalfunc():
    global x
    x = 15              #<--  this is Global Keyword
    print(x)            #print 15  <--inside function
myglobalfunc()
print(x)              #print 15  <--outside function

"""
x = 100
def updatefunc():
    global()['x'] = 200  # Accesses the global variable 'x' and updates its value to 200.
    print(x)             # Prints the updated value of 'x' (200).   
updatefunc()             # Calls the 'update' function.
print(x)                 # Prints the global value of 'x' after the function call (200).
"""

a, b = 5, 10
def addfunc():     
    global a, b
    a += 2
    b += 3
addfunc()
print(a, b)             #print 7 13  <--outside function


PI = 3.14         #<--  this is Constant Variable
def mycirclefunc(r):
    area = PI * (r**2)   
    return area
print(mycirclefunc(5))   #print 78.5  