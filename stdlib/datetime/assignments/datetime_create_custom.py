"""
* Assignment: Datetime Create Custom
* Filename: datetime_create_custom.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `date` object with date of your birth
    2. Create `time` object with time of your birth
    3. Create `datetime` object with date and time of your birth

Polish:
    1. Stwórz obiekt `date` z datą Twojego urodzenia
    2. Stwórz obiekt `time` z czasem Twojego urodzenia
    3. Stwórz obiekt `datetime` z datą i czasem Twojego urodzenia

Tests:
    TODO
"""

# Given
from datetime import datetime, date, time


# Solution
d = date(1970, 1, 1)
t = time(0, 0)
dt = datetime(1970, 1, 1, 0, 0, 0)
