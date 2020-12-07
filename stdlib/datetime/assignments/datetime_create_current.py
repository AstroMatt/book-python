"""
* Assignment: Datetime Create Current
* Filename: datetime_create_current.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `date` object with current date
    2. Create `datetime` object with current date and time
    3. Create `time` object with current time
    4. Date and time must be from system, not hardcoded in code

Polish:
    1. Stwórz obiekt `date` z obecną datą
    2. Stwórz obiekt `datetime` z obecną datą i czasem
    3. Stwórz obiekt `time` z obecnym czasem
    4. Data i czas ma być pobierana z systemu, nie zapisana w kodzie

Tests:
    TODO
"""

# Given
from datetime import datetime, date


# Solution
dt = datetime.now()
d = dt.date()
t = dt.time()
