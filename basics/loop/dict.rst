.. _Loop Dict:

**************
Loop over Dict
**************


Rationale
=========
* Since Python 3.7: ``dict`` keeps order
* Before Python 3.7: ``dict`` order is not ensured!!


Iterate
=======
.. highlights::
    * By default ``dict`` iterates over keys
    * Suggested variable name: ``key``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    for obj in DATA:
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Keys
============
.. highlights::
    * Suggested variable name: ``key``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.keys())
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    for obj in DATA.keys():
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Values
==============
.. highlights::
    * Suggested variable name: ``value``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.values())
    # [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in DATA.values():
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Iterate Key-Value Pairs
=======================
.. highlights::
    * Suggested variable name: ``key``, ``value``

.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.items())
    # [('Sepal length', 5.1),
    #  ('Sepal width', 3.5),
    #  ('Petal length', 1.4),
    #  ('Petal width', 0.2),
    #  ('Species', 'setosa')]

    for key, value in DATA.items():
        print(key, '->', value)

    # Sepal length -> 5.1
    # Sepal width -> 3.5
    # Petal length -> 1.4
    # Petal width -> 0.2
    # Species -> setosa


List of Dicts
=============
.. code-block:: python
    :caption: Unpacking ``list`` of ``dict``

    DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'}]

    for row in DATA:
        sepal_length = row['Sepal length']
        species = row['Species']
        print(f'{species} -> {sepal_length}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3


Generate with Range
===================
.. highlights::
    * ``range()``
    * Pythonic way is to use ``zip()``
    * Don't use ``len(range(...))`` - it evaluates generator

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i in range(len(header)):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}

Generate with Enumerate
=======================
.. highlights::
    * ``enumerate()``
    * ``_`` regular variable name (not a special syntax)
    * ``_`` by convention is used when variable will not be referenced

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i, key in enumerate(header):
        result[key] = data[i]

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}


Generate with Zip
=================
.. highlights::
    * ``zip()``
    * The most Pythonic way

.. code-block:: python

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for key, value in zip(header, data):
        result[key] = value

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}

.. code-block:: python

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']

    result = dict(zip(header, data))

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}


Assignments
===========

.. literalinclude:: assignments/loop_dict_to_dict.py
    :caption: :download:`Solution <assignments/loop_dict_to_dict.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_dict_to_list.py
    :caption: :download:`Solution <assignments/loop_dict_to_list.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_dict_label_encoder.py
    :caption: :download:`Solution <assignments/loop_dict_label_encoder.py>`
    :end-before: # Solution
