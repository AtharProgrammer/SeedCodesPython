'''
In Python, static methods are a way to define methods within a class
that don't require access to the instance or the class itself.
They are similar to regular functions, but they are defined within a
class and can be called using the class name
or an instance of the class.
'''


class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")

# You can call the static method using the class name
MyClass.my_static_method()

# Or using an instance of the class
obj = MyClass()
obj.my_static_method()

'''
Static methods are defined using the @staticmethod decorator.
When you define a method as static,
it doesn't receive the self (or cls for class methods)
parameter as the first argument, which means you can't
access instance or class variables inside the method directly.

Static methods are useful when you have a method that doesn't rely
on instance or class variables and you want it to be logically grouped
within a class. They can be used for utility functions or operations that
don't depend on the state of the object.
'''
