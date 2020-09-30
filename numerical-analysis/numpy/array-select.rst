************
Array Select
************


Unique
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3, 1],
                  [1, 4, 5, 6]])

    np.unique(a)
    # array([1, 2, 3, 4, 5, 6])

    np.unique(a, axis=0)
    # array([[1, 2, 3, 1],
    #        [1, 4, 5, 6]])

    np.unique(a, axis=1)
    # array([[1, 1, 2, 3],
    #        [1, 6, 4, 5]])


Diagonal
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2],
                  [3, 4]])

    a.diagonal()
    # array([1, 4])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.diagonal()
    # array([1, 5])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.diagonal()
    # array([1, 5, 9])


Nonzero
=======
* Each element of the tuple contains one of the indices for each nonzero value.
* Therefore, the length of each tuple element is the number of nonzeros in the array.
* The first element of the tuple is the first index for each of the nonzero values: (``[0, 0, 1, 1]``).
* The second element of the tuple is the second index for each of the nonzero values: (``[0, 2, 0, 2]``).
* Pairs are zipped (first and second tuple):

    * ``0, 0``
    * ``0, 2``
    * ``1, 0``
    * ``1, 2``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 0, 2],
                  [3, 0, 4]])

    a.nonzero()
    # (array([0, 0, 1, 1]),
    #  array([0, 2, 0, 2]))

    a[a.nonzero()]
    # array([1, 2, 3, 4])


Where
=====

Single argument
---------------
* ``where(boolarray)``
* indexes of elements

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])

    np.where(a != 2)
    # (array([0, 2, 3, 4, 5]),)

    np.where(a % 2 == 0)
    # (array([1, 3, 5]),)

    np.where( (a>2) & (a<5) )
    # (array([2, 3]),)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.where(a % 2 == 0)
    # (array([0, 0, 1]),
    #  array([0, 2, 1]))

    np.where( (a>2) & (a<5) )
    # (array([0, 1]),
    #  array([2, 0]))

Multiple argument
-----------------
* ``where(boolarray, truearray, falsearray)``:

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.where(a < 5, 'small', 'large')
    # array([['small', 'small', 'small'],
    #        ['small', 'large', 'large'],
    #        ['large', 'large', 'large']], dtype='<U5')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.where(a % 2 == 0, 'even', 'odd')
    # array([['odd', 'even', 'odd'],
    #        ['even', 'odd', 'even'],
    #        ['odd', 'even', 'odd']], dtype='<U4')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.where(a % 2 == 0, np.nan, a)
    # array([[ 1., nan,  3.],
    #        [nan,  5., nan],
    #        [ 7., nan,  9.]])


Take
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    at_index = np.array([0, 0, 1, 2, 2, 1])

    a.take(at_index)
    # array([1, 1, 2, 3, 3, 2])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    at_index = np.array([0, 0, 1])

    a.take(at_index, axis=0)
    # array([[1, 2, 3],
    #        [1, 2, 3],
    #        [4, 5, 6]])

    a.take(at_index, axis=1)
    # array([[1, 1, 2],
    #        [4, 4, 5],
    #        [7, 7, 8]])


Advanced indexing
=================
* two types of indexes: int, bool
* Also known as Fancy indexing

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True]])

    a[a > 2]
    # array([3, 4, 5, 6])

    a[a > a.mean()]
    # array([4, 5, 6])

    a[a >= a.mean()+1]
    # array([5, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[a % 2 == 0]
    # array([2, 4, 6])

    even = (a % 2 == 0)
    a[even]
    # array([2, 4, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[ (a>2) & (a<=5) & (a%2==1) ]
    # array([3, 5])

    query1 = (a > 2)
    query2 = (a <= 5)
    query3 = (a % 2 == 1)
    a[query1 & query2 & query3]
    # array([3, 5])

    large = (a > 2)
    small = (a <= 5)
    odd = (a % 2 == 1)
    a[large & small & odd]
    # array([3, 5])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    at_index = np.array([0, 1, 0])
    a[at_index]
    # array([1, 2, 1])

    at_index = np.array([0, 2])
    a[at_index]
    # array([1, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[[0,2]]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    a[[0,2], [1,2]]
    # array([2, 9])

    a[:2, [1,2]]
    # array([[2, 3],
    #        [5, 6]])

.. code-block:: python
    :caption: ``rows,cols`` creates coordinate system for selecting values (like ``zip()``). For example: ``(0,0); (0,1); (1,0); (1,1); (0,1)``, as in this example.

    import numpy as np


    a = np.array([[1, 4], [9, 16]], float)

    rows = np.array([0, 0, 1, 1, 0], int)
    cols = np.array([0, 1, 0, 1, 1], int)

    a[rows]
    # array([[ 1.,  4.],
    #        [ 1.,  4.],
    #        [ 9., 16.],
    #        [ 9., 16.],
    #        [ 1.,  4.]])

    a[rows,cols]
    # array([ 1.,  4.,  9., 16.,  4.])

.. code-block:: python

    import numpy as np

    # '2000-01-01' -> [1, 2, 3]
    # '2000-01-02' -> [4, 5, 6]
    # '2000-01-03' -> [7, 8, 9]

    date = np.array([
        '2000-01-01',
        '2000-01-02',
        '2000-01-03'])

    values = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])


    date == '2000-01-02'
    # array([False,  True, False])

    values[date == '2000-01-02']
    # array([[4, 5, 6]])

    values[date != '2000-01-02']
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    values[ (date=='2000-01-01') | (date=='2000-01-03') ]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

.. code-block:: python

    import numpy as np


    index = np.array([
        '2000-01-01',
        '2000-01-02',
        '2000-01-03'])

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    jan01 = (index == '2000-01-01')
    jan03 = (index == '2000-01-03')

    data[jan01|jan03]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    data[jan01|jan03, 0]
    # array([1, 7])s

    data[jan01|jan03, :2]
    # array([[1, 2],
    #        [7, 8]])

    data[jan01|jan03, :2] = 0
    data
    # array([[0, 0, 3],
    #        [4, 5, 6],
    #        [0, 0, 9]])


.. code-block:: python

    import numpy as np

    #                Morning         Noon      Evening
    # 1999-12-30  1.76405235,  0.40015721,  0.97873798,
    # 1999-12-31  2.2408932 ,  1.86755799, -0.97727788,
    # 2000-01-01  0.95008842, -0.15135721, -0.10321885,
    # 2000-01-02  0.4105985 ,  0.14404357,  1.45427351,

    index = np.array([
        '1999-12-30',
        '1999-12-31',
        '2000-01-01',
        '2000-01-02'])

    columns = np.array(['Morning', 'Noon', 'Evening'])

    data = np.array([[ 1.76405235,  0.40015721,  0.97873798],
                     [ 2.2408932 ,  1.86755799, -0.97727788],
                     [ 0.95008842, -0.15135721, -0.10321885],
                     [ 0.4105985 ,  0.14404357,  1.45427351]])

    dec31 = (index == '1999-12-31')   # array([False,  True, False, False])
    jan01 = (index == '2000-01-01')   # array([False, False,  True, False])
    days = (dec31 | jan01)            # array([False,  True,  True, False])
    morning = (columns == 'Morning')  # array([ True, False, False])

    data[dec31|jan01]
    # array([[ 2.2408932 ,  1.86755799, -0.97727788],
    #        [ 0.95008842, -0.15135721, -0.10321885]])

    data[dec31|jan01, (columns == 'Morning')]
    # array([2.2408932 , 0.95008842])

    data[dec31|jan01, morning]
    # array([2.2408932 , 0.95008842])

    data[days]
    # array([[ 2.2408932 ,  1.86755799, -0.97727788],
    #        [ 0.95008842, -0.15135721, -0.10321885]])

    data[days, morning]
    # array([2.2408932 , 0.95008842])

Diagonal problem
----------------
.. warning:: Without the ``np.ix_`` call, only the diagonal elements would be selected. This difference is the most important thing to remember about indexing with multiple advanced indexes.

.. code-block:: python

    import numpy as np

    #                Morning         Noon      Evening
    # 1999-12-30  1.76405235,  0.40015721,  0.97873798,
    # 1999-12-31  2.2408932 ,  1.86755799, -0.97727788,
    # 2000-01-01  0.95008842, -0.15135721, -0.10321885,
    # 2000-01-02  0.4105985 ,  0.14404357,  1.45427351,

    index = np.array([
        '1999-12-30',
        '1999-12-31',
        '2000-01-01',
        '2000-01-02'])

    columns = np.array(['Morning', 'Noon', 'Evening'])

    data = np.array([[ 1.76405235,  0.40015721,  0.97873798],
                     [ 2.2408932 ,  1.86755799, -0.97727788],
                     [ 0.95008842, -0.15135721, -0.10321885],
                     [ 0.4105985 ,  0.14404357,  1.45427351]])

    dec31 = (index == '1999-12-31')     # array([False,  True, False, False])
    jan01 = (index == '2000-01-01')     # array([False, False,  True, False])
    morning = (columns == 'Morning')    # array([ True, False, False])
    evening = (columns == 'Evening')    # array([False, False,  True])

    data[dec31|jan01]
    # array([[ 2.2408932 ,  1.86755799, -0.97727788],
    #        [ 0.95008842, -0.15135721, -0.10321885]])

    data[(dec31|jan01), (morning|evening)]
    # array([ 2.2408932 , -0.10321885])

    data[np.ix_((dec31|jan01), (morning|evening))]
    # array([[ 2.2408932 , -0.97727788],
    #        [ 0.95008842, -0.10321885]])


Assignments
===========

Numpy Select Isin
-----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_select_isin.py`
* Last update: 2020-10-01

:English:
    #. Set random seed to 0
    #. Generate ``a: np.ndarray`` of size 50x50
    #. ``a`` must contains random integers from 0 to 1024 inclusive
    #. Create ``result: np.ndarray`` with elements selected from ``a`` which are power of two
    #. Sort ``result`` in descending order
    #. Print ``result``

:Polish:
    #. Ustaw ziarno losowości na 0
    #. Wygeneruj ``a: np.ndarray`` rozmiaru 50x50
    #. ``a`` musi zawierać losowe liczby całkowite z zakresu od 0 do 1024 włącznie
    #. Stwórz ``result: np.ndarray`` z elementami wybranymi z ``a``, które są potęgami dwójki
    #. Posortuj ``result`` w kolejności malejącej
    #. Wypisz ``result``

:Hints:
    * ``np.isin(a, b)``
    * ``np.flip(a)``
