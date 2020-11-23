"""
* Assignment: Type String Emoticon
* Filename: type_str_emoticon.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    1. Define `name` with value `Mark Watney`
    2. Print `hello NAME EMOTICON`, where:
        a. NAME is a name read from user
        b. EMOTICON is Unicode Codepoint "\U0001F642"
    3. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj `name` z wartością `Mark Watney`
    2. Wypisz `hello NAME EMOTICON`, gdzie:
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
