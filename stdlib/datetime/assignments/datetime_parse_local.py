"""
* Assignment: Datetime Parse Local
* Filename: datetime_parse_local.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create `datetime` object by parsing the given date
    3. Using formatting parameters print the date and time in ISO format
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Podaną datę przekonwertuj do obiektu `datetime`
    3. Używając parametrów formatujących wyświetl datę i czas w formacie ISO
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Add string `local time` to format statement

Tests:
    >>> type(result)
    <class 'str'>
    >>> result
    '1961-04-12T06:07:00.000000Z'
"""

# Given
from datetime import datetime


DATA = 'April 12, 1961 6:07 local time'

# Solution
format = '%B %d, %Y %H:%M local time'
dt = datetime.strptime(DATA, format)
result = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

