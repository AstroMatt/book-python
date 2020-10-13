.. _Intermediate Comprehensions Nesting:


**********************
Comprehensions Nesting
**********************


Nested Comprehensions
=====================
.. code-block:: python

   DATA = [
        {'lastname': 'Jiménez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Иван'},
        {'firstname': 'Jan', 'lastname': 'Twardowski', 'born': 1961},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
    ]

    fieldnames = set(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}

.. code-block:: python

   DATA = [
        {'lastname': 'Jiménez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Иван'},
        {'firstname': 'Jan', 'lastname': 'Twardowski', 'born': 1961},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
    ]

    fieldnames = set()
    fieldnames.update(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}

.. code-block:: python

   DATA = [
        {'lastname': 'Jiménez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Иван'},
        {'firstname': 'Jan', 'lastname': 'Twardowski', 'born': 1961},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
    ]

    fieldnames = set()
    fieldnames.update(key for row in DATA for key in row.keys())

    print(fieldnames)
    # {'born', 'lastname', 'firstname'}


Generator comprehensions
========================
.. code-block:: python

   DATA = [
        {'lastname': 'Jiménez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Иван'},
        {'firstname': 'Jan', 'lastname': 'Twardowski', 'born': 1961},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
    ]

    fieldnames = set()

    fieldnames.add(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {<generator object <genexpr> at 0x1179a0a50>}


Assignments
===========
.. todo:: Create assignments
