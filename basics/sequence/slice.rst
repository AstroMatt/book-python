.. _Sequence Slice:

**************
Sequence Slice
**************


Rationale
=========
.. highlights::
    * Slice argument must be ``int`` (positive, negative or zero)
    * Negative slices starts from the end and go right to left


Ordered Sequences
=================
.. code-block:: python
    :caption: Slicing ``str``

    data = 'abcde'

    data[0:3]           # 'abc'
    data[3:5]           # 'de'
    data[:3]            # 'abc'
    data[3:]            # 'de'

    data[::1]           # 'abcde'
    data[::-1]          # 'edcba'
    data[::2]           # 'ace'
    data[::-2]          # 'eca'
    data[1::2]          # 'bd'
    data[1:4:2]         # 'bd'

.. code-block:: python
    :caption: Slicing ``tuple``

    data = ('a', 'b', 'c', 'd', 'e')

    data[0:3]           # ('a', 'b', 'c')
    data[3:5]           # ('d', 'e')
    data[:3]            # ('a', 'b', 'c')
    data[3:]            # ('d', 'e')

    data[::2]           # ('a', 'c', 'e')
    data[::-1]          # ('e', 'd', 'c', 'b', 'a')
    data[1::2]          # ('b', 'd')
    data[1:4:2]         # ('b', 'd')

.. code-block:: python
    :caption: Slicing ``list``

    data = ['a', 'b', 'c', 'd', 'e']

    data[0:3]           # ['a', 'b', 'c']
    data[3:5]           # ['d', 'e']
    data[:3]            # ['a', 'b', 'c']
    data[3:]            # ['d', 'e']

    data[::2]           # ['a', 'c', 'e']
    data[::-1]          # ['e', 'd', 'c', 'b', 'a']
    data[1::2]          # ['b', 'd']
    data[1:4:2]         # ['b', 'd']


Unordered Sequences
===================
.. code-block:: python
    :caption: Slicing ``set`` is not possible

    data = {'a', 'b', 'c', 'd', 'e'}

    data[:3]
    # TypeError: 'set' object is not subscriptable

.. code-block:: python
    :caption: Slicing ``set`` is not possible

    data = frozenset({'a', 'b', 'c', 'd', 'e'})

    data[:3]
    # TypeError: 'frozenset' object is not subscriptable


Slice Forwards
==============
.. highlights::
    * ``my_sequence[start:stop]``

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0:2]       # 'We'
    text[:2]        # 'We'

    text[0:9]       # 'We choose'
    text[:9]        # 'We choose'

    text[23:28]     # 'Moon!'
    text[23:]       # 'Moon!'


Slice Backwards
===============
.. highlights::
    * Negative index starts from the end and go right to left

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:-13]      # 'We choose to go'
    text[:-19]      # 'We choose'

    text[-12:]      # 'to the Moon!'
    text[-5:]       # 'Moon!'

    text[-12:-6]    # 'to the'
    text[-5:-1]     # 'Moon'

    text[23:-2]     # 'Moo'
    text[13:-2]     # 'go to the Moo'

    text[-1:0]      # ''
    text[-2:0]      # ''
    text[-2:2]      # ''
    text[-5:5]      # ''


Step
====
.. highlights::
    * Every ``n``-th element
    * ``my_sequence[start:stop:step]``

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'

    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Out of Range
============
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]      # 'We choose to go to the Moon!'
    text[100:]      # ''


Nested Sequences
================
.. code-block:: python

    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    data[::2]
    # [[1, 2, 3],
    #  [7, 8, 9]]

    data[::2][1]
    # [7, 8, 9]

    data[::2][:1]
    # [[1, 2, 3]]

    data[::2][1][1:]
    # [8, 9]


Slice All
=========
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:]         # 'We choose to go to the Moon!'

.. code-block:: python
    :caption: Used in ``numpy`` to get all rows or columns

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    data[:, 1]
    # array([2, 5, 8])

    data[1, :]
    # array([4, 5, 6])

.. code-block:: python
    :caption: This unfortunately does not work on ``list``

    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    data[:]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    data[:, 1]
    # TypeError: list indices must be integers or slices, not tuple

    data[:][1]
    # [4, 5, 6]

.. code-block:: python
    :caption: Used in ``pandas`` to get all rows or columns

    import pandas as pd

    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]})

    df.loc[:, ('A','B')]
    #    A  B
    # 0  1  4
    # 1  2  5
    # 2  3  6

    df.loc[1, :]
    # A    2
    # B    5
    # C    8
    # Name: 1, dtype: int64


Index Arithmetic
================
.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 23
    last = 28
    step = 2

    text[first:last]            # 'Moon!'
    text[first:last-1]          # 'Moon'
    text[first:last:step]       # 'Mo!'
    text[first:last-1:step]     # 'Mo'


Slice Function
==============
.. code-block:: python

    text = 'We choose to go to the Moon!'

    q = slice(23, 27)
    text[q]
    # 'Moon'

    q = slice(None, 9)
    text[q]
    # 'We choose'

    q = slice(23, None)
    text[q]
    # 'Moon!'

    q = slice(23, None, 2)
    text[q]
    # 'Mo!'

    q = slice(None, None, 2)
    text[q]
    # 'W hoet ot h on'


Example
=======
.. code-block:: python

    from pprint import pprint

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ]

    pprint(DATA[1:])
    # [(5.8, 2.7, 5.1, 1.9, 'virginica'),
    #  (5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    #  (6.3, 2.9, 5.6, 1.8, 'virginica'),
    #  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    #  (4.7, 3.2, 1.3, 0.2, 'setosa')]

    pprint(DATA[1::2])
    # [(5.8, 2.7, 5.1, 1.9, 'virginica'),
    #  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    #  (6.4, 3.2, 4.5, 1.5, 'versicolor')]

    pprint(DATA[1::-2])
    # [(5.8, 2.7, 5.1, 1.9, 'virginica')]

    pprint(DATA[:1:-2])
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    #  (6.3, 2.9, 5.6, 1.8, 'virginica'),
    #  (5.1, 3.5, 1.4, 0.2, 'setosa')]

    pprint(DATA[:-5:-2])
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'), (6.3, 2.9, 5.6, 1.8, 'virginica')]

    pprint(DATA[1:-5:-2])
    # []


Assignments
===========

Sequence Slice Substr
---------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_slice_substr.py`

:English:
    #. Use data from "Input" section (see below)
    #. Use ``str.find()`` and slicing
    #. Print ``TEXT`` without text in ``REMOVE``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj ``str.find()`` oraz wycinania
    #. Wypisz ``TEXT`` bez tekstu z ``REMOVE``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        TEXT = 'We choose to go to the Moon!'
        REMOVE = 'to go to '

:Output:
    .. code-block:: python

    result: str
    # 'We choose the Moon!'


Sequence Slice Sequence
-----------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_slice_sequence.py`

:English:
    #. Create tuple ``a`` with digits: 0, 1, 2, 3
    #. Create list ``b`` with digits: 2, 3, 4, 5
    #. Create set ``c`` with every second element from ``a`` and ``b``
    #. Print ``c``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz tuplę ``a`` z cyframi: 0, 1, 2, 3
    #. Stwórz listę ``b`` z cyframi: 2, 3, 4, 5
    #. Stwórz zbiór ``result`` z co drugim elementem ``a`` i ``b``
    #. Wypisz ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        result: set
        # {0, 2, 4}

:The whys and wherefores:
    * Defining and using ``list``, ``tuple``, ``set``
    * Slice data structures
    * Type casting

Sequence Slice Text
-------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/sequence_slice_text.py`

:English:
    #. Use data from "Input" section (see below)
    #. Remove title and military rank in each variable
    #. Remove also whitespaces at the beginning and end of a text
    #. Use only ``slice`` to clean text
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Usuń tytuł naukowy i stopień wojskowy z każdej zmiennej
    #. Usuń również białe znaki na początku i końcu tekstu
    #. Użyj tylko ``slice`` do oczyszczenia tekstu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Example:
    .. code-block:: python

        text = 'lt. Mark Watney, PhD'
        text[4:-5]
        # 'Mark Watney'

:Input:
    .. code-block:: python

        a = 'dr hab. inż. Jan Twardowski, prof. AATC'
        b = 'gen. pil. Jan Twardowski'
        c = 'Mark Watney, PhD'
        d = 'lt. col. ret. Melissa Lewis'
        e = 'dr n. med. Ryan Stone'
        f = 'Ryan Stone, MD-PhD'
        g = 'lt. col. Jan Twardowski\t'

:Output:
    .. code-block:: python

        print(a == 'Jan Twardowski')       # True
        print(b == 'Jan Twardowski')       # True
        print(c == 'Mark Watney')          # True
        print(d == 'Melissa Lewis')        # True
        print(e == 'Ryan Stone')           # True
        print(f == 'Ryan Stone')           # True
        print(g == 'Jan Twardowski')       # True

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Slicing strings
    * Cleaning text input

Sequence Slice Split
--------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/sequence_slice_split.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Write header (first line) to ``header`` variable
    #. Write data without header to ``data`` variable
    #. Calculate pivot point: number records in ``data`` multiplied by PERCENT (division ratio below)
    #. Divide ``data`` into two lists:

        * ``train``: 60% - training data
        * ``test``: 40% - testing data

    #. From ``data`` write training data from start to pivot
    #. From ``data`` write test data from pivot to end
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    #. Zapisz dane bez nagłówka do zmiennej ``data``
    #. Wylicz punkt podziału: ilość rekordów w ``data`` razy PROCENT (proporcja podziału poniżej)
    #. Podziel ``data`` na dwie listy:

        * ``train``: 60% - dane do uczenia
        * ``test``: 40% - dane do testów

    #. Z ``data`` zapisz do uczenia rekordy od początku do punktu podziału
    #. Z ``data`` zapisz do testów rekordy od punktu podziału do końca
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        header: tuple
        # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

        train: List[tuple]
        # [(5.8, 2.7, 5.1, 1.9, 'virginica'),
        #  (5.1, 3.5, 1.4, 0.2, 'setosa'),
        #  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        #  (6.3, 2.9, 5.6, 1.8, 'virginica'),
        #  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        #  (4.7, 3.2, 1.3, 0.2, 'setosa'),
        #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
        #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
        #  (4.9, 2.5, 4.5, 1.7, 'virginica'),
        #  (7.1, 3.0, 5.9, 2.1, 'virginica'),
        #  (4.6, 3.4, 1.4, 0.3, 'setosa')]

        test: List[tuple]
        # [(5.4, 3.9, 1.7, 0.4, 'setosa'),
        #  (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        #  (5.0, 3.6, 1.4, 0.3, 'setosa'),
        #  (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        #  (6.5, 3.0, 5.8, 2.2, 'virginica'),
        #  (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        #  (6.3, 3.3, 6.0, 2.5, 'virginica'),
        #  (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        #  (4.6, 3.1, 1.5, 0.2, 'setosa')]

:The whys and wherefores:
    * Using nested sequences
    * Using slices
    * Type casting
    * Magic Number
