'''
Method overloading, in traditional object-oriented programming languages like Java or C++, refers to the ability to
define multiple methods with the same name but different parameter lists in the same class. However, Python doesn't support method
overloading in the same way.

In Python, you can only have one method with a particular name in a class. If you define multiple methods with the same name,
the last one defined will overwrite the previous ones. However, you can achieve similar behavior to method overloading in Python
by using default arguments or variable arguments.

Let's see an example using default arguments:
'''

class MathOperations:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

math = MathOperations()
print('example using default arguments')
print(math.add(2, 3))       # Output: 5
print(math.add(2, 3, 4))    # Output: 9

'''
In this example, the add method takes three parameters, but the third parameter c is optional and has a default value of None.
If the method is called with only two arguments, it performs addition of the first two arguments. If it's called with three arguments,
it adds all three.

Similarly, you can achieve method overloading behavior using variable arguments:
'''
class MathOperations:
    def add(self, *args):
        return sum(args)

math = MathOperations()

print('using variable arguments')
print(math.add(2, 3))           # Output: 5
print(math.add(2, 3, 4))        # Output: 9
print(math.add(2, 3, 4, 5))     # Output: 14

'''
In this example, the add method takes a variable number of arguments using the *args syntax. It then simply sums up all the
arguments passed to it.

Although Python doesn't have true method overloading like some other languages, these techniques provide similar
flexibility and can be used to achieve similar functionality.
'''
