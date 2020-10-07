"""
>>> is_pesel_valid('12345678901')
True
>>> is_pesel_woman('12345678901')
True
"""

import re

PESEL_REGEXP = r'^\d{11}$'


def is_pesel_valid(pesel):
    if re.match(PESEL_REGEXP, pesel):
        return True
    else:
        return False


def is_pesel_woman(pesel):
    """
    Check whether PESEL is woman's.
    If the second to last number is even,
    then PESEL is woman's, in other case PESEL is man's.
    """
    if int(pesel[-2]) % 2 == 0:
        return True
    else:
        return False
