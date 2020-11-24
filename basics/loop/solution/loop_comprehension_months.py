"""
* Assignment: Loop Comprehension Months
* Filename: loop_comprehension_months.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Use dict comprehension
    3. Convert `MONTH` into dict:
        a. Keys: month number
        b. Values: month name
    4. Month number must be two letter string (zero padded) - `f'{number:02}'`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj rozwinięcia słownikowego
    3. Przekonwertuj `MONTH` w słownik:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    4. Numer miesiąca ma być dwuznakowym stringiem (wypełnij zerem) - `f'{number:02}'`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'dict'>
    >>> '00' not in result
    True
    >>> '13' not in result
    True
    >>> result['01'] == 'January'
    True
    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(len(x) == 2 for x in result.keys())
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'01': 'January',
     '02': 'February',
     '03': 'March',
     '04': 'April',
     '05': 'May',
     '06': 'June',
     '07': 'July',
     '08': 'August',
     '09': 'September',
     '10': 'October',
     '11': 'November',
     '12': 'December'}
"""

# Given
MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

result: dict

# Solution
result = {f'{k:02}':v for k,v in enumerate(MONTHS, start=1)}
