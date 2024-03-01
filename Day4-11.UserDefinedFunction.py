#global variable : we can access global variables in all
#functions.

a, b=10, 20 # global variable

def add():
    print(a+b)

def mul():
    print(a*b)

add()
mul()
