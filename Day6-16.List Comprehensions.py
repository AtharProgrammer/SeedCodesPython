'''
List Comprehensions: Python allows you to create lists using a concise and expressive syntax known as list comprehensions.
They provide a compact way to create lists based on existing lists.
'''
# Example 1: Create a list of squares of numbers from 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 ==0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
