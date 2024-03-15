'''
9. Logging Exceptions
Logging exceptions can help in debugging and understanding the flow
of the program.

'''
import logging

try:
    pass
    # Some code
except Exception as e:
    logging.exception("An error occurred: %s", e)
