def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test the function
my_string = "Hello, world!"
print(count_vowels(my_string))  # Output: 3
