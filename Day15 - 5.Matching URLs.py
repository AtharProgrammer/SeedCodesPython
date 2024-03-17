'''
Matching URLs
'''
import re

pattern = r"\bhttps?://\S+\b"
text = "Visit our website at https://www.example.com"
urls = re.findall(pattern, text)
print("URLs:", urls)

# This pattern will match URLs starting with http:// or https://.

'''
Let's break down the regular expression pattern `r"\bhttps?://\S+\b"`:

1. `r`: Denotes a raw string literal.

2. `\b`: Matches a word boundary, ensuring that the URL is preceded
and followed by a non-word character (like whitespace or punctuation).
This ensures that the URL is not part of a larger word.

3. `https?://`: Matches the protocol part of the URL. Here:
   - `http`: Matches the characters "http" literally.
   - `s?`: Matches the character "s" zero or one time.
   This makes the "s" in "https" optional, allowing the pattern
   to match both "http://" and "https://".

4. `\S+`: Matches one or more non-whitespace characters.
This matches the domain part of the URL (e.g., "www.example.com").
The `\S` matches any character that is not a whitespace character, and `+` quantifier
specifies that it should match one or more such characters.

5. `\b`: Matches a word boundary, ensuring that the URL is preceded
and followed by a non-word character (like whitespace or punctuation).

Putting it all together, this regular expression pattern matches
URLs starting with either "http://" or "https://", followed by one
or more non-whitespace characters (the domain name), and ending at a word boundary.

Example matches: "https://www.example.com", "http://example.com/page.html"

Example non-matches: "abchttps://www.example.comdef", "www.example.com",
"http://www.example.com/path/to/page.html"

'''
