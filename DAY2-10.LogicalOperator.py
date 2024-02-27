'''
and Operator: Returns True if both the left and right expressions are true.
or Operator: Returns True if at least one of the expressions (left or right)
is true.
not Operator: Returns True if the following expression is false,
and False if it is true. It essentially reverses the logical state
of its operand.
'''
print(True and True)   # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False) # Output: False

print(True or True)   # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True
print(False or False) # Output: False

print(not True)  # Output: False
print(not False) # Output: True
