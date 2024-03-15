'''
5. Finally Block
The finally block is executed regardless of whether an exception occurs or not.
It's useful for cleanup code, like closing files or releasing resources.

'''
try:
    # Some code
    pass
except Exception:
    # Exception handling
    print("An error occurred")
finally:
    # Cleanup code
    print("Cleanup code executed")
