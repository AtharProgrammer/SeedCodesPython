'''
3. Handling Multiple Exceptions
You can handle multiple exceptions in a single except block or handle them
individually.
'''
try:
    # Some code
except (ValueError, TypeError):
    # Handling multiple exceptions
    print("Value or type error occurred")
except FileNotFoundError:
    # Handling a specific exception
    print("File not found")
