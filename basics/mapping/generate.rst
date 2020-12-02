****************
Mapping Generate
****************


Pair
====
.. code-block:: python

    pair = [
        ('commander', 'Melissa Lewis'),
    ]

    dict(pair)
    # {'commander': 'Melissa Lewis'}


List of Pairs
=============
.. code-block:: python

    pairs = [
        ('commander', 'Melissa Lewis'),
        ('botanist', 'Mark Watney'),
        ('chemist', 'Alex Vogel'),
    ]

    dict(pairs)
    # {'commander': 'Melissa Lewis',
    #   'botanist': 'Mark Watney',
    #   'chemist': 'Alex Vogel'}


Enumerate
=========
.. code-block:: python

    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    astronaut = enumerate(crew)

    next(astronaut)
    # (0, 'Melissa Lewis')

    next(astronaut)
    # (1, 'Mark Watney')

    next(astronaut)
    # (2, 'Alex Vogel')

    next(astronaut)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(enumerate(crew))
    # [(0, 'Melissa Lewis'),
    #  (1, 'Mark Watney'),
    #  (2, 'Alex Vogel')]

    dict(enumerate(crew))
    # {0: 'Melissa Lewis',
    #  1: 'Mark Watney',
    #  2: 'Alex Vogel'}


Zip
===
.. highlights::
    * ``zip`` is a generator
    * ``zip`` will create a list of pairs (like ``dict.items()``)

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    astronaut = zip(roles, crew)

    next(astronaut)
    # ('commander', 'Melissa Lewis')

    next(astronaut)
    # ('botanist', 'Mark Watney')

    next(astronaut)
    # ('chemist', 'Alex Vogel')

    next(astronaut)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(zip(roles, crew))
    # [('commander', 'Melissa Lewis'),
    #  ('botanist', 'Mark Watney'),
    #  ('chemist', 'Alex Vogel')]

    dict(zip(roles, crew))
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel'}

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]

    astronauts = zip(roles, crew)
    astronauts
    # <zip object at 0x120c487c0>

    next(astronauts)
    # ('commander', ('Melissa', 'Lewis'))

    next(astronauts)
    # ('botanist', ('Mark', 'Watney'))

    next(astronauts)
    # ('chemist', ('Alex', 'Vogel'))

    next(astronauts)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]

    list(zip(roles, crew))
    # [('commander', ('Melissa', 'Lewis')),
    #  ('botanist', ('Mark', 'Watney')),
    #  ('chemist', ('Alex', 'Vogel'))]

    dict(zip(roles, crew))
    # {'commander': ('Melissa', 'Lewis'),
    #  'botanist': ('Mark', 'Watney'),
    #  'chemist': ('Alex', 'Vogel')}


Assignments
===========

.. literalinclude:: assignments/mapping_generate_pairs.py
    :caption: :download:`Solution <assignments/mapping_generate_pairs.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_enumerate.py
    :caption: :download:`Solution <assignments/mapping_generate_enumerate.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_zip.py
    :caption: :download:`Solution <assignments/mapping_generate_zip.py>`
    :end-before: # Solution
