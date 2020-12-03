"""
* Assignment: Type String Emoticon
* Filename: type_str_emoticon.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `name` with value `Mark Watney`
    2. Print `Hello NAME EMOTICON`, where:
        a. NAME is a name read from user
        b. EMOTICON is Unicode Codepoint "\U0001F642"
    3. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj `name` z wartością `Mark Watney`
    2. Wypisz `Hello NAME EMOTICON`, gdzie:
        a. NAME to imię wczytane od użytkownika
        b. EMOTICON to Unicode Codepoint "\U0001F642"
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'str'>
    >>> '\U0001F642' in result
    True
    >>> name in result
    True
    >>> result
    'Hello Mark Watney 🙂'
"""

# Solution
name = 'Mark Watney'
result = f'Hello {name} \U0001F642'
