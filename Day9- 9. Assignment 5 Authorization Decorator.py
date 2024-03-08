'''
Assignment 5: Authorization Decorator
Write a Python decorator that checks if the user is authorized to call a
function.
'''
def authorize(user_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role == "admin":
                return func(*args, **kwargs)
            else:
                raise PermissionError("You are not authorized to call this function")
        return wrapper
    return decorator

@authorize(user_role="admin")
def sensitive_operation():
    return "You are authorized to call this function"

# Test the function
print(sensitive_operation())
