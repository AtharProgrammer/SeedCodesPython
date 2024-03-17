'''
Matching Dates
'''

import re

pattern = r"\b\d{1,2}/\d{1,2}/\d{4}\b"
text = "Date: 12/31/2022, Meeting on 1/15/2023"
dates = re.findall(pattern, text)
print("Dates:", dates)


# This pattern will match dates in the format MM/DD/YYYY.

'''
Certainly! Let's break down the regular expression pattern `r"\b\d{1,2}/\d{1,2}/\d{4}\b"`:

1. `r`: Denotes a raw string literal.

2. `\b`: Matches a word boundary, ensuring that the date is preceded
and followed by a non-word character (like whitespace or punctuation).
This ensures that the date is not part of a larger word.

3. `\d{1,2}`: Matches one or two digits. `{1,2}` specifies that there can be
either one or two digits. This is for the month and day components of the date.

4. `/`: Matches a literal forward slash (`/`), which separates the month, day,
and year components of the date.

5. `\d{1,2}`: Matches one or two digits. This is for the month and day components of the date.

6. `/`: Matches another literal forward slash (`/`), separating the day and year components.

7. `\d{4}`: Matches exactly four digits. This is for the year component of the date.

8. `\b`: Matches a word boundary, ensuring that the date is preceded and followed by a
non-word character (like whitespace or punctuation).

Putting it all together, this regular expression pattern matches dates in the format `MM/DD/YYYY`, where:
- `MM` can be one or two digits (1-12).
- `DD` can be one or two digits (1-31).
- `YYYY` must be exactly four digits.

Example matches: "12/31/2022", "1/15/2023"

Example non-matches: "abc12/31/2022def", "12/32/2022", "1/15/23"
'''
