'''
Regular expressions (regex) in Python are a powerful tool for pattern matching and text processing. They allow you to search,
extract, and manipulate text based on specific patterns. Here's a basic examples on how to use regular expressions in Python:

1. **Importing the `re` Module**: Python's `re` module provides support for regular expressions. Start by importing it:

'''
import re

'''
2. **Basic Patterns**: Regular expressions consist of ordinary characters (such as letters and digits) and special characters
(such as `.` or `*`). For example, the pattern `hello` will match the string `hello`. 

3. **Special Characters**:
   - `.`: Matches any single character except newline.
   - `^`: Matches the start of the string.
   - `$`: Matches the end of the string.
   - `*`: Matches zero or more occurrences of the preceding character.
   - `+`: Matches one or more occurrences of the preceding character.
   - `?`: Matches zero or one occurrence of the preceding character.
   - `[]`: Matches any single character within the brackets.
   - `|`: Matches either the pattern to the left or the pattern to the right.
   - `()` : Groups patterns together.
   - `\`: Escapes special characters, allowing them to be treated as literals.

4. **Using Regular Expressions**:
   - **`re.match(pattern, string)`**: Attempts to match the pattern from the beginning of the string.
   - **`re.search(pattern, string)`**: Searches for the first occurrence of the pattern in the string.
   - **`re.findall(pattern, string)`**: Finds all occurrences of the pattern in the string and returns them as a list.
   - **`re.sub(pattern, replacement, string)`**: Replaces occurrences of the pattern with the replacement string.
   - **`re.split(pattern, string)`**: Splits the string based on the occurrences of the pattern and returns a list of substrings.

5. **Example**:

'''
import re

# Search for a pattern in a string
text = "Python is fun!"
pattern = "Python"
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")

# Extracting email addresses from a string
text = "Email me at emaile@xample.com or contact me at contact@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print("Email addresses:", emails)

'''
In Python, the `r` prefix before a string denotes a raw string literal.
Raw strings treat backslashes (`\`) as literal characters, rather than interpreting them as escape sequences.
This is particularly useful when working with regular expressions, as it allows you to write patterns without
having to escape backslashes.

Let's break down the regular expression pattern you provided:


pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


- `r`: Denotes a raw string literal.
- `\b`: Matches a word boundary, ensuring that the email address is preceded and followed by a non-word character
(like whitespace or punctuation).
- `[A-Za-z0-9._%+-]+`: Matches one or more occurrences of letters (both uppercase and lowercase),
digits, or the characters `.`, `_`, `%`, `+`, and `-`.
- `@`: Matches the `@` symbol.
- `[A-Za-z0-9.-]+`: Matches one or more occurrences of letters (both uppercase and lowercase), digits,
or the characters `.`, and `-`, which constitute the domain name.
- `\.`: Matches a literal dot (`.`). Since dot (`.`) is a special character in regular expressions and matches any character,
we need to escape it with a backslash to match a literal dot.
- `[A-Z|a-z]{2,}`: Matches two or more occurrences of letters (uppercase or lowercase) that represent the top-level domain (TLD).
`{2,}` specifies that there must be at least 2 characters.
- `\b`: Matches a word boundary, ensuring that the email address is preceded and followed by a non-word character
(like whitespace or punctuation).

This regular expression pattern is designed to match email addresses with the format `local-part@domain.tld`,
where the local-part can include letters, digits, and special characters like `.`, `_`, `%`, `+`, and `-`, and
the domain and TLD can include letters, digits, and the characters `.` and `-`.
'''
