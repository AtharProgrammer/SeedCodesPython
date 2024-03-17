'''
Matching IP Addresses:
'''
import re

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
text = "IP addresses: 192.168.0.1 and 10.0.0.1"
ip_addresses = re.findall(pattern, text)
print("IP Addresses:", ip_addresses)

# This pattern will match IP addresses in the format XXX.XXX.XXX.XXX,
# where each X represents a number between 0 and 255.

'''
Let's break down the regular expression pattern `r"\b(?:\d{1,3}\.){3}\d{1,3}\b"`:

1. `r`: Denotes a raw string literal.

2. `\b`: Matches a word boundary, ensuring that the IP address is preceded and followed
by a non-word character (like whitespace or punctuation). This ensures that the IP address is not part of a larger word.

3. `(?:\d{1,3}\.){3}`:
   - `(?: ... )`: This is a non-capturing group. It groups together the pattern inside but does not capture the matched text.
   - `\d{1,3}`: Matches one to three digits. This is for each part of the IP address (e.g., 192, 168, 0).
   - `\.`: Matches a literal dot (`.`), which separates the different parts of the IP address.
   - `{3}`: Specifies that the preceding group (one to three digits followed by a dot) must be repeated exactly three times.
   This ensures that there are three parts to the IP address separated by dots.

4. `\d{1,3}`: Matches one to three digits. This is for the fourth part of the IP address (e.g., 1 in 192.168.0.1).

5. `\b`: Matches a word boundary, ensuring that the IP address is preceded and followed by a non-word character
(like whitespace or punctuation).

Putting it all together, this regular expression pattern matches IP addresses in the format `XXX.XXX.XXX.XXX`,
where each `XXX` can be one to three digits.

Example matches: "192.168.0.1", "10.0.0.1"

Example non-matches: "abc192.168.0.1def", "256.0.0.1", "192.168.0.1.2"
'''
