'''
In Python, lambda is a keyword used to create anonymous functions, also known as lambda functions. Lambda functions are small,
inline functions that can have any number of parameters but can only have one expression.
'''

#Here's the basic syntax of a lambda function:
# lambda arguments: expression

'''
The arguments are the input parameters to the lambda function, and expression is the computation performed by the function.
The result of the expression is implicitly returned by the lambda function.

Lambda functions are typically used in situations where you need a small function for a short period and don't want
to define a separate named function using the def keyword.

'''



#Simple Addition:

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
