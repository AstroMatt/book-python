"""
* Assignment: Datetime Parse ISO
* Filename: datetime_parse_iso.py
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. The date and time is given in ISO format:
    3. Convert it to `datetime` object

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dana jest data w formacie ISO
    3. Przedstaw datę jako obiekt `datetime`

Tests:
    >>> type(result)
    <class 'datetime.datetime'>
    >>> result
    datetime.datetime(1969, 7, 21, 2, 56, 15, 123000)
"""

# Given
from datetime import datetime

DATA = '1969-07-21T02:56:15.123Z'

# Solution
format = '%Y-%m-%dT%H:%M:%S.%fZ'
result = datetime.strptime(DATA, format)
