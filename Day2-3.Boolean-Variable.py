#Creating Boolean Variables
#You can directly assign True or False to a variable:

is_active = True
print(is_active)  # Output: True

has_access = False
print(has_access)  # Output: False


# Examples of Boolean operations
print(True and False)  # Output: False
print(True or False)  # Output: True
print(not True)  # Output: False

# Examples of truth value testing
print(bool(None))  # Output: False
print(bool(0))  # Output: False
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool([1, 2, 3]))  # Output: True
print(bool([]))  # Output: False
