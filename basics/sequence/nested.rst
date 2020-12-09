Sequence Nested
===============


List of Lists
-------------
* Multidimensional lists
* Readability differs depending on whitespaces

    >>> data = [[1, 2, 3],
    ...         [4, 5, 6],
    ...         [7, 8, 9]]

    >>> a = [[1,2,3],[4,5,6],[7,8,9]]
    >>>
    >>> b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>>
    >>> c = [[1,2,3], [4,5,6], [7,8,9]]
    >>>
    >>> d = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ... ]
    >>>
    >>> e = [[1, 2, 3],
    ...      [4, 5, 6],
    ...      [7, 8, 9]]

    >>> data = [[1, 2, 3],
    ...         [4, 5, 6],
    ...         [7, 8, 9]]
    >>>
    >>> len(data)
    3
    >>> len(data[0])
    3


List of Tuples
--------------
* Readability differs depending on whitespaces

    >>> data = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    ...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ...         (7.6, 3.0, 6.6, 2.1, 'virginica')]

Append elements using ``list.append()``:

    >>> data = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    ...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ...         (7.6, 3.0, 6.6, 2.1, 'virginica')]
    >>>
    >>> row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    >>> data.append(row)
    >>> data  # doctest: +NORMALIZE_WHITESPACE
    [(4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 2.5, 4.5, 1.7, 'virginica')]

Append elements using ``list.extend()``:

    >>> data = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    ...        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ...        (7.6, 3.0, 6.6, 2.1, 'virginica')]
    >>>
    >>> row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    >>> data.extend(row)
    >>> data  # doctest: +NORMALIZE_WHITESPACE
    [(4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     4.9,
     2.5,
     4.5,
     1.7,
     'virginica']

    >>> data = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    ...         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ...         (7.6, 3.0, 6.6, 2.1, 'virginica')]
    >>>
    >>> len(data)
    3
    >>> len(data[0])
    5


Many Types
----------
    >>> data = [[1, 2],
    ...         (3, 4, 5, 6),
    ...         {7, 8, 9, 10, 11}]
    >>>
    >>> len(data)
    3
    >>> len(data[0])
    2
    >>> len(data[1])
    4
    >>> len(data[2])
    5


Assignments
-----------
.. literalinclude:: assignments/sequence_nested_create.py
    :caption: :download:`Solution <assignments/sequence_nested_create.py>`
    :end-before: # Solution
