'''
Assignment 2: Retry Decorator
Write a Python decorator that retries a function call a specified number of times if an exception occurs.
'''


import time

def retry(num_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Exception occurred: {e}. Retrying...")
                    time.sleep(1)  # Wait before retrying
            raise Exception(f"Failed after {num_retries} retries")
        return wrapper
    return decorator

@retry(num_retries=10)

def potentially_unstable_function():
    import random
    if random.random() < 0.5:
        return "Success"
    else:
        raise ValueError("Random error")

# Test the function
print(potentially_unstable_function())
