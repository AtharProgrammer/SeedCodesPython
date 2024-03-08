# Write a Python decorator to measure the execution time of a function.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    return sum(range(n))

# Test the function
print(example_function(1000000))
