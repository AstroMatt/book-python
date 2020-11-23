"""
* Assignment name: Type String Quotes
* Suggested filename: type_str_quotes.py
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 8 min

English:
    1. Define ``name`` with value ``José Jiménez``
    2. To print use f-string formatting
    3. Note, that second line starts with tab
    4. Value ``NAME`` in double quotes is a name read from user
    5. Mind the different quotes, apostrophes, tabs and newlines
    6. Do not use neither space not enter - use ``\n`` and ``\t``
    7. Do not use string addition (``str + str``)
    8. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj ``name`` z wartością ``José Jiménez``
    2. Do wypisania użyj f-string formatting
    3. Zauważ, że druga linijka zaczyna się od tabulacji
    4. Wartość ``NAME`` w podwójnych cudzysłowach to ciąg od użytkownika
    5. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
    6. Nie używaj spacji ani klawisza enter - użyj ``\n`` i ``\t``
    7. Nie korzystaj z dodawania stringów (``str + str``)
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    '''My name... "José Jiménez".
        I'm an \"\"\"astronaut!\"\"\"'''
"""

name = 'José Jiménez'
result = f"""'''My name... "{name}".\n\tI\'m an \"\"\"astronaut!\"\"\"'''"""
