"""
* Assignment: Type String Normalize
* Filename: type_str_normalize.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Use `str` methods to clean `DATA`
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wykorzystaj metody `str` do oczyszczenia `DATA`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'str'>
    >>> result
    'Jana Twardowskiego III'
"""

# Given
DATA = 'UL. jana \tTWArdoWskIEGO 3'

# Solution
result = (
    DATA.replace('UL. ', '')
        .replace('\t', '')
        .title()
        .replace('3', 'III')
)

