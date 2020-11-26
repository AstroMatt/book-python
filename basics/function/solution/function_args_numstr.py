"""
* Assignment: Function Arguments Numbers to Str
* Filename: function_args_numstr.py
* Complexity: medium
* Lines of code to write: 5 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Given is pilot's alphabet for numbers
    3. Convert ``DATA: dict[int, str]`` to ``data: dict[str, str]`` (keys as ``str``)
    4. Define function ``pilot_say`` converting ``int`` or ``float`` to text form in Pilot's Speak
    5. You cannot change ``DATA``, but you can modify ``data``
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dany jest alfabet pilotów dla numerów
    3. Przekonwertuj ``DATA: dict[int, str]`` na ``data: dict[str, str]`` (klucze jako ``str``)
    4. Zdefiniuj funkcję ``pilot_say`` konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów
    5. Nie możesz zmieniać ``DATA``, ale możesz modyfikować ``data``
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pilot_say(1969)
    'one niner six niner'
    >>> pilot_say(31337)
    'tree one tree tree seven'
    >>> pilot_say(13.37)
    'one tree and tree seven'
    >>> pilot_say(31.337)
    'tree one and tree tree seven'
    >>> pilot_say(-1969)
    'minus one niner six niner'
    >>> pilot_say(-31.337)
    'minus tree one and tree tree seven'
    >>> pilot_say(-49.35)
    'minus fower niner and tree fife'
"""

# Given
DATA = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'tree',
    4: 'fower',
    5: 'fife',
    6: 'six',
    7: 'seven',
    8: 'ait',
    9: 'niner',
}

# Solution
data = {str(k):v for k,v in DATA.items()}
data['-'] = 'minus'
data['.'] = 'and'


def pilot_say(number):
    return ' '.join(data[x] for x in str(number))
