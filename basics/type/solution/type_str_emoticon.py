"""
* Assignment name: Type String Emoticon
* Suggested filename: type_str_emoticon.py
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    #. Define ``name`` with value ``Mark Watney``
    #. Print ``hello NAME EMOTICON``, where:

        * NAME is a name read from user
        * EMOTICON is Unicode Codepoint "\U0001F642"

    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj ``name`` z wartością ``Mark Watney``
    #. Wypisz ``hello NAME EMOTICON``, gdzie:

        * NAME to imię wczytane od użytkownika
        * EMOTICON to Unicode Codepoint "\U0001F642"

    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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

name = 'Mark Watney'
result = f'Hello {name} \U0001F642'
