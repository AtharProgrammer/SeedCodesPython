'''
Matching HTML Tags
'''
import re

pattern = r"<[^>]*>"
html = "<p>This is a <strong>bold</strong> text.</p>"
tags = re.findall(pattern, html)
print("HTML Tags:", tags)

# This pattern will match HTML tags in a string.

'''
Let's break down the regular expression pattern `r"<[^>]*>"`:

1. `r`: Denotes a raw string literal.

2. `<`: Matches the literal character "<", indicating the start of an HTML tag.

3. `[^>]*`: This part is a negated character class, represented by `[^>]`,
which matches any character except ">" (the closing bracket of the HTML tag).
   - `^>`: Negates the characters inside the square brackets, meaning
   it matches any character that is not ">".
   - `*`: Matches zero or more occurrences of the preceding character class.
   This means it will match any sequence of characters that are not ">".

4. `>`: Matches the literal character ">", indicating the end of an HTML tag.

Putting it all together, this regular expression pattern matches HTML
tags (including any attributes inside the tag) by searching for sequences of
characters enclosed in "<" and ">".

Example matches: "<p>", "<div id='content'>", "<a href='example.com'>"

Example non-matches: "This is a paragraph of text.", "Some <em>italic</em> text."
'''
