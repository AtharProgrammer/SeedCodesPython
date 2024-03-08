'''
In Python, the destructor is a special method called __del__ that
is automatically invoked when an object is about to be destroyed.
The destructor is primarily used to perform cleanup actions before
the object is removed from memory. However, unlike languages like C++,
where destructors are guaranteed to be called when an object goes
out of scope, the invocation of Python's __del__ method
is not guaranteed.
'''
class MyClass:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

# Creating an instance of MyClass
obj = MyClass()

# The object goes out of scope and will be destroyed
del obj

'''
In this example, when the MyClass object is created, the constructor (__init__) is called,
and "Constructor called" is printed. When the object goes out of scope
and is explicitly deleted using del obj, Python automatically calls the destructor (__del__), and
"Destructor called" is printed.
'''
