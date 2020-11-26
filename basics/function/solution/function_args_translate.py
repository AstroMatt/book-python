"""
* Assignment: Function Arguments Translate
* Filename: function_args_translate.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 5 min

English:
    1. Define function ``translate`` with parameter ``text``
    2. Use ``str.join()`` with generator expression to iterate over ``text``
    3. If letter is in ``PL`` then use conversion value as letter, otherwise take letter
    4. Return from function translated ``text``
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję ``translate`` przyjmującą parametr ``text``
    2. Użyj ``str.join()`` z wyrażeniem generatorowym do iteracji po ``text``
    3. Jeżeli litera jest w ``PL`` to użyj skonwertowanej wartości jako litera, w przeciwnym przypadku to weź literę
    4. Zwróć z funkcji przetłumaczony ``text``
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> translate('zażółć')
    'zazolc'
    >>> translate('gęślą')
    'gesla'
    >>> translate('jaźń')
    'jazn'
    >>> translate('zażółć gęślą jaźń')
    'zazolc gesla jazn'
"""

# Given
PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}


# Solution
def translate(text):
    return ''.join(PL.get(x, x) for x in text)
