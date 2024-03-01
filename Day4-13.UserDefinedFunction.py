'''
Local vs. global variables: same variable name

if the application contains both local & global variables same
name then to represent global variables use globals() function.
'''
a, b=10, 20 #global variables

def add(a, b): #local variables
    print(a+b)
    print (globals()['a']+globals()['b'])

add(4,4) # function calling
