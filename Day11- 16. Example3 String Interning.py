# Demonstrating string interning behavior
s1 = "hello"
s2 = "hello"
print(id(s1))  # Output: A unique identifier for s1
print(id(s2))  # Output: The same unique identifier for s2 as s1

s3 = "world"
s4 = "world"
print(id(s3))  # Output: A unique identifier for s3
print(id(s4))  # Output: The same unique identifier for s4 as s3
