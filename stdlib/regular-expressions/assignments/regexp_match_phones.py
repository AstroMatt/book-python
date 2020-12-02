"""
>>> is_valid_phone('+48 (12) 355 5678')
False
>>> is_valid_phone('+48 123 555 678')
True
>>> is_valid_phone('123 555 678')
False
>>> is_valid_phone('+48 12 355 5678')
True
>>> is_valid_phone('+48 123-555-678')
False
>>> is_valid_phone('+48 123 555 6789')
False
>>> is_valid_phone('+1 (123) 555-6789')
False
>>> is_valid_phone('+1 (123).555.6789')
False
>>> is_valid_phone('+1 800-python')
False
>>> is_valid_phone('+48123555678')
False
>>> is_valid_phone('+48 123 555 678 wew. 1337')
False
>>> is_valid_phone('+48 123555678,1')
False
>>> is_valid_phone('+48 123555678,1,2,3')
False
"""

import re

MOBILE = r'\+\d{2} \d{3} \d{3} \d{3}'
WORK = r'\+\d{2} \d{2} \d{3} \d{4}'
PATTERN = f'^({MOBILE}|{WORK})$'


def is_valid_phone(number):
    if re.match(PATTERN, number):
        return True
    else:
        return False
