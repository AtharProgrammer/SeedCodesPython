'''
String formatting in Python allows you to create formatted strings by
embedding values within a string. There are several ways to perform
string formatting in Python.


Using the % operator (old-style formatting):
This method uses the % operator to format strings.
It's an older approach and is less recommended compared to newer
methods like f-strings and the str.format() method.

'''
name = "Alice"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)


'''
Using the str.format() method:
This method uses the format() method of strings to insert values into a string.
'''

name = "Bob"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)


'''
Using f-strings (formatted string literals):
This is the most modern and preferred method introduced in Python 3.6.
It allows you to embed expressions directly into string literals.
'''
name = "Charlie"
age = 35
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)


