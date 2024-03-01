'''local variables v/s global variables : different variable names

The variables which are declared inside the function are called
local variables.
The variables which are declared outside of the function are called
global variables.
'''
x, y=10, 20 #global variables
def add(a, b): #local variables
    print (a+b)
    print(x+y)

def mul(a, b): #local variables
    print (a*b)
    print(x*y)

add(4,4) # function calling
mul(5,5) # function calling
