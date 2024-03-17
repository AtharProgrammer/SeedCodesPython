import re

pattern = r"\b\d{3}-\d{3}-\d{4}\b"
text = "Contact us at 123-456-7890 or 987-654-3210"
phone_numbers = re.findall(pattern, text)
print("Phone Numbers:", phone_numbers)

'''
Let's break down the regular expression pattern `r"\b\d{3}-\d{3}-\d{4}\b"`:

1. `r`: Denotes a raw string literal.

2. `\b`: Matches a word boundary, ensuring that the phone number is preceded
and followed by a non-word character (like whitespace or punctuation).
This ensures that the phone number is not part of a larger word.

3. `\d{3}`: Matches exactly three digits. This is for the first part of
the phone number, typically the area code.

4. `-`: Matches a literal hyphen (`-`), which separates the different
parts of the phone number.

5. `\d{3}`: Matches exactly three digits. This is for the second part
of the phone number, typically the exchange code.

6. `-`: Matches another literal hyphen (`-`), separating the different
parts of the phone number.

7. `\d{4}`: Matches exactly four digits. This is for the third part of
the phone number, typically the subscriber number.

8. `\b`: Matches a word boundary, ensuring that the phone number is
preceded and followed by a non-word character (like whitespace or punctuation).

Putting it all together, this regular expression pattern matches phone
numbers in the format `###-###-####`, where each `#` represents a digit.

Example matches: "123-456-7890", "987-654-3210"

Example non-matches: "abc123-456-7890def", "123-456-789", "1234-567-8901"
'''
