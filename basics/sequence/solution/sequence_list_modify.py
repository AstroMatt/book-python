"""
* Assignment: Sequence List Modify
* Filename: sequence_list_modify.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Insert at the begin of ``a`` last element popped from ``b``
    3. Append to the ``b`` last element popped from ``a``
    4. For getting elements use ``list.pop()``
    5. From list ``c`` using ``del`` delete last element
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Na początek ``a`` wstaw ostatni element wyciągnięty z ``b``
    3. Na koniec ``b`` wstaw ostatni element wyciągnięty z ``a``
    4. Do wyciągnięcia używaj ``list.pop()``
    5. Z listy ``c`` za pomocą ``del`` usuń ostatni element
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(a)
    <class 'list'>
    >>> type(b)
    <class 'list'>
    >>> type(c)
    <class 'list'>
    >>> a
    ['versicolor', 4.7, 3.2, 1.3, 0.2]
    >>> b
    [7.0, 3.2, 4.7, 1.4, 'setosa']
    >>> c
    [7.6, 3.0, 6.6, 2.1]
"""

# Given
a = [4.7, 3.2, 1.3, 0.2, 'setosa']
b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
c = [7.6, 3.0, 6.6, 2.1, 'virginica']

# Solution
a.insert(0, b.pop())
b.append(a.pop())
del c[4]
