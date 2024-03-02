def is_palindrome(s):
    return s == s[::-1]

# Test the function
palindrome_string = "level"
non_palindrome_string = "hello"
print(is_palindrome(palindrome_string))  # Output: True
print(is_palindrome(non_palindrome_string))  # Output: False
