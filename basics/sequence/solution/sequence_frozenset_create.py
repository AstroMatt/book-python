"""
* Assignment: Sequence Frozenset Create
* Filename: sequence_frozenset_create.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 2 min

English:
    1. Create frozenset ``result`` with elements:
        a. ``'a'``
        b. ``1``
        c. ``2.2``
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz frozenset ``result`` z elementami:
        a. ``'a'``
        b. ``1``
        c. ``2.2``
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'frozenset'>
    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

# Solution
result = frozenset({'a', 1, 2.2})
