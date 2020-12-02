.. _Sequence Slice:

**************
Sequence Slice
**************


Rationale
=========
.. highlights::
    * Slice argument must be ``int`` (positive, negative or zero)
    * Positive Index starts with ``0``
    * Negative index starts with ``-1``


Slice Forwards
==============
.. highlights::
    * ``sequence[start:stop]``

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
    text[-5:-1]     # 'Moon'
    text[23:-2]     # 'Moo'

    text[-1:0]      # ''
    text[-2:0]      # ''
    text[-2:2]      # ''
    text[-5:5]      # ''


Step
====
.. highlights::
    * Every ``n``-th element
    * ``sequence[start:stop:step]``
    * ``start`` defaults to ``0``
    * ``stop`` defaults to ``len(sequence)``
    * ``step`` defaults to ``1``

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::1]       # 'We choose to go to the Moon!'
    text[::2]       # 'W hoet ot h on'
    text[::-1]      # '!nooM eht ot og ot esoohc eW'
    text[::-2]      # '!oMeto go soce'


Out of Range
============
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]
    # 'We choose to go to the Moon!'

    text[100:]
    # ''


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
    # Traceback (most recent call last):
    # TypeError: 'set' object is not subscriptable

.. code-block:: python
    :caption: Slicing ``set`` is not possible

    data = frozenset({'a', 'b', 'c', 'd', 'e'})

    data[:3]
    # Traceback (most recent call last):
    # TypeError: 'frozenset' object is not subscriptable


Nested Sequences
================
.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]

    DATA[1:]
    # [(5.8, 2.7, 5.1, 1.9, 'virginica'),
    #  (5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    #  (6.3, 2.9, 5.6, 1.8, 'virginica'),
    #  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    #  (4.7, 3.2, 1.3, 0.2, 'setosa')]

    DATA[-3:]
    # [(6.3, 2.9, 5.6, 1.8, 'virginica'),
    #  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    #  (4.7, 3.2, 1.3, 0.2, 'setosa')]


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
    # Traceback (most recent call last):
    # TypeError: list indices must be integers or slices, not tuple

    data[:][1]
    # [4, 5, 6]

.. code-block:: python
    :caption: Used in ``pandas`` to get all rows or columns

    import pandas as pd

    df = pd.DataFrame([
        {'A': 1, 'B': 2, 'C': 3},
        {'A': 4, 'B': 5, 'C': 6},
        {'A': 7, 'B': 8, 'C': 9}])

    df
    #    A  B  C
    # 0  1  2  3
    # 1  4  5  6
    # 2  7  8  9

    df.loc[:, ('A','B')]
    #    A  B
    # 0  1  2
    # 1  4  5
    # 2  7  8

    df.loc[::2, ::2]
    #    A  C
    # 0  1  3
    # 2  7  9

    df.loc[1, :]
    # A    2
    # B    5
    # C    8


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
.. highlights::
    * Every ``n``-th element
    * ``sequence[start:stop:step]``
    * ``start`` defaults to ``0``
    * ``stop`` defaults to ``len(sequence)``
    * ``step`` defaults to ``1``

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


    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]

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

.. literalinclude:: assignments/sequence_slice_substr.py
    :caption: :download:`Solution <assignments/sequence_slice_substr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_slice_sequence.py
    :caption: :download:`Solution <assignments/sequence_slice_sequence.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_slice_text.py
    :caption: :download:`Solution <assignments/sequence_slice_text.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_slice_split.py
    :caption: :download:`Solution <assignments/sequence_slice_split.py>`
    :end-before: # Solution
