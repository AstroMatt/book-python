"""
* Assignment: Loop Unpacking Months
* Filename: loop_unpacking_months.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `enumerate()` to convert `MONTH` into dict:
        a. Keys: month number
        b. Values: month name
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `enumerate()` do konwersji `MONTH` w słownik:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'}

"""

# Given
MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

result: dict = {}

# Solution
for i, month in enumerate(MONTHS, start=1):
    result[i] = month
