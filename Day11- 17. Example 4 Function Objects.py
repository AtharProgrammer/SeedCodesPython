# Identifying function objects
def greet():
    print("Hello, world!")

func1 = greet
func2 = greet
print(id(func1))  # Output: A unique identifier for func1
print(id(func2))  # Output: The same unique identifier for func2 as func1
