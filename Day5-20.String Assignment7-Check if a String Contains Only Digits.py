def contains_only_digits(s):
    return s.isdigit()

# Test the function
string1 = "12345"
string2 = "123abc"
print(contains_only_digits(string1))  # Output: True
print(contains_only_digits(string2))  # Output: False
