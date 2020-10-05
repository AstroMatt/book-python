************
Python WAT?!
************


.. code-block:: python

    a = 'ABCDE'
    list(a)
    # ['A', 'B', 'C', 'D', 'E']

    a = 'ABCDE',
    list(a)
    # ['ABCDE']

    a = ('ABCDE',)
    list(a)
    # ['ABCDE']

    list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']

    list('ABCDE',)
    # ['A', 'B', 'C', 'D', 'E']

    list('ABCDE','asd')
    # Traceback (most recent call last):
    #  File "<input>", line 1, in <module>
    # TypeError: list expected at most 1 arguments, got 2

.. code-block:: python
    :caption: CPython 3.7.4

    ('a' * 4096) is ('a' * 4096)
    # True

    ('a' * 4097) is ('a' * 4097)
    # False

* More details at :ref:`OOP String Interning`

.. code-block:: python

    1 + 1 is 2
    # True

    0.1 + 0.1 == 0.2
    # True

    0.1 + 0.2 == 0.3
    # False

    0.1 + 0.2
    # 0.30000000000000004

    2.2 * 3.0 == 3.3 * 2.0
    # False

.. code-block:: python

    for x in ('hello'):
        print(x)
    # h
    # e
    # l
    # l
    # o

    for x in ('hello',):
        print(x)
    # hello

    for x in 'hello':
        print(x)
    # h
    # e
    # l
    # l
    # o

    for x in 'hello',:
        print(x)
    # hello

.. code-block:: python

    a = [1, 2, 3]
    b = a
    c = a.copy()

    print(a)  # [1, 2, 3]
    print(b)  # [1, 2, 3]
    print(c)  # [1, 2, 3]

    a.append(4)

    print(a)  # [1, 2, 3, 4]
    print(b)  # [1, 2, 3, 4]
    print(c)  # [1, 2, 3]


