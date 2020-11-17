.. _Sequence Unpack:

***************
Sequence Unpack
***************


Rationale
=========
.. code-block:: python

    a = 1
    a, b = 1, 2
    a, b, c = 1, 2, 3

    a, b, c = (1, 2, 3)
    a, b, c = [1, 2, 3]
    a, b, c = {1, 2, 3}

.. code-block:: python

    (a, b, c) = (1, 2, 3)
    (a, b, c) = [1, 2, 3]

    [a, b, c] = [1, 2, 3]
    [a, b, c] = (1, 2, 3)

.. figure:: img/function-unpacking,args,kwargs.png
    :scale: 40%
    :align: center

    Unpacking and Arbitrary Number of Parameters and Arguments


Errors
======
.. code-block:: python

    {a, b, c} = {1, 2, 3}
    # Traceback (most recent call last):
    #     ...
    # SyntaxError: can't assign to literal

.. code-block:: python

    a, b, c = [1, 2, 3, 4]
    # Traceback (most recent call last):
    #     ...
    # ValueError: too many values to unpack (expected 3)

.. code-block:: python

    a, b, c, d = [1, 2, 3]
    # Traceback (most recent call last):
    #     ...
    # ValueError: not enough values to unpack (expected 4, got 3)


Arbitrary Number of Arguments
=============================
.. code-block:: python
    :caption: Unpacking values at the right side

    a, b, *c = [1, 2, 3, 4]

    a               # 1
    b               # 2
    c               # [3, 4]

.. code-block:: python
    :caption: Unpacking values at the left side

    *a, b, c = [1, 2, 3, 4]

    a               # [1, 2]
    b               # 3
    c               # 4

.. code-block:: python
    :caption: Unpacking values from both sides at once

    a, *b, c = [1, 2, 3, 4]

    a               # 1
    b               # [2, 3]
    c               # 4

.. code-block:: python
    :caption: Unpacking from variable length

    a, *b, c = [1, 2]

    a               # 1
    b               # []
    c               # 2

.. code-block:: python
    :caption: Cannot unpack from both sides at once

    *a, b, *c = [1, 2, 3, 4]
    # Traceback (most recent call last):
    #     ...
    # SyntaxError: two starred expressions in assignment

.. code-block:: python
    :caption: Unpacking requires values for required arguments

    a, *b, c = [1]
    # Traceback (most recent call last):
    #     ...
    # ValueError: not enough values to unpack (expected at least 2, got 1)


Nested
======
.. code-block:: python

    a, (b, c) = [1, (2, 3)]

    a               # 1
    b               # 2
    c               # 3


Convention
==========
.. code-block:: python

    first, *middle, last = [1, 2, 3, 4]

    first           # 1
    middle          # [2, 3]
    last            # 4

.. code-block:: python

    first, second, *others = [1, 2, 3, 4]

    first               # 1
    second              # 2
    others              # [3, 4]


Skipping Values
===============
.. highlights::
    * ``_`` is regular variable name, not a special Python syntax
    * ``_`` by convention is used for data we don't want to access in future

.. code-block:: python

    _ = 'Jan Twardowski'

    print(_)
    # Jan Twardowski

.. code-block:: python

    line = 'Jan,Twardowski,44'

    firstname, lastname, _ = line.split(',')

    print(firstname)        # Jan
    print(lastname)         # Twardowski

.. code-block:: python

    a, _, c = 1, 2, 3

    print(a)                # 1
    print(c)                # 3

.. code-block:: python

    _, b, _ = 1, 2, 3

    print(b)                # 2

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *_, label = line.split(',')

    label                   # setosa

.. code-block:: python

    line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'

    username, _, _, _, fullname, *_ = line.split(':')

    username                # twardowski
    fullname               # Jan Twardowski

.. code-block:: python

    line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'

    username, *_, home, _ = line.split(':')

    username                # twardowski
    home                    # /home/twardowski

.. code-block:: python

    _, (interesting, _) = [1, (2, 3)]

    interesting             # 2


Examples
========
.. code-block:: python

    import sys

    sys.version_info
    # sys.version_info(major=3, minor=9, micro=0, releaselevel='final', serial=0)

    major, minor, *_ = sys.version_info
    print(major, minor, sep='.')
    # 3.9

.. code-block:: python

    *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')

    features                # [5.8, 2.7, 5.1, 1.9]
    label                   # 'virginica'

.. code-block:: python

    *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
    avg = sum(features) / len(features)

    print(label, avg)
    # virginica 3.875

.. code-block:: python

    line = 'ares3,watney,lewis,vogel,johanssen'
    mission, *crew = line.split(',')

    mission                 # ares3
    crew                    # ['watney', 'lewis', 'vogel', 'johanssen']

.. code-block:: python

    def parse(line):
        mission, *crew = line.split(',')
        crew = ' and '.join(name.title() for name in crew)
        print(mission.upper(), crew, sep=': ')


    parse('ares3,watney,lewis,vogel,johanssen')
    # ARES3: Watney and Lewis and Vogel and Johanssen

    parse('apollo18,twardowski,ivanovic')
    # APOLLO18: Twardowski and Ivanovic

.. code-block:: python

    first, second, *others = range(10)

    first                   # 0
    second                  # 1
    others                  # [2, 3, 4, 5, 6, 7, 8, 9]


Using in a Loop
===============
.. code-block:: python

    *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')

    features                # [5.8, 2.7, 5.1, 1.9]
    label                   # 'virginica'

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *features, label in DATA:
        avg = sum(features) / len(features)
        print(label, avg)

    # virginica 3.875
    # setosa 2.55
    # versicolor 3.475

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *_, label in DATA:
        print(label)

    # virginica
    # setosa
    # versicolor


Assignments
===========

Function Unpack Flat
--------------------
* Assignment name: Function Unpack Flat
* Last update: 2020-10-12
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_unpack_flat.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``str.split()`` split input data by white space
    #. Separate ip address and host names
    #. Use asterisk ``*`` notation
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając ``str.split()`` podziel dane wejściowe po białych znakach
    #. Odseparuj adres ip i nazw hostów
    #. Skorzystaj z notacji z gwiazdką ``*``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

:Output:
    .. code-block:: text

        >>> assert type(ip) is str
        >>> assert type(hosts) is list
        >>> assert all(type(host) is str for host in hosts)

        >>> ip
        '10.13.37.1'
        >>> hosts
        ['nasa.gov', 'esa.int', 'roscosmos.ru']

:Hints:
    * ``help(str.split)``

Function Unpack Nested
----------------------
* Assignment name: Function Unpack Nested
* Last update: 2020-10-12
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_unpack_nested.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header and records
    #. Use asterisk ``*`` notation
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Skorzystaj z konstrukcji z gwiazdką ``*``
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
        ]

:Output:
    .. code-block:: text

        >>> assert type(header) is tuple
        >>> assert all(type(x) is str for x in header)
        >>> assert type(data) is list
        >>> assert all(type(row) is tuple for row in data)

        >>> header
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

        >>> data  # doctest: +NORMALIZE_WHITESPACE
        [(5.8, 2.7, 5.1, 1.9, 'virginica'),
         (5.1, 3.5, 1.4, 0.2, 'setosa'),
         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
         (6.3, 2.9, 5.6, 1.8, 'virginica'),
         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
         (4.7, 3.2, 1.3, 0.2, 'setosa')]

