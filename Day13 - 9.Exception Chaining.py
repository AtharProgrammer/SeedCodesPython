'''
8. Exception Chaining
You can chain exceptions using from keyword.

'''
try:
    # Some code
    pass
except ValueError as e:
    raise TypeError("Custom message") from e
