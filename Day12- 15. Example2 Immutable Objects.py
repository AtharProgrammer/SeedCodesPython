# Integers are immutable objects
x = 5
y = 5
print(id(x))  # Output: A unique identifier for x
print(id(y))  # Output: The same unique identifier for y as x

y += 1
print(id(x))  # Output: The identifier remains the same for x
print(id(y))  # Output: A new unique identifier for y after modification
