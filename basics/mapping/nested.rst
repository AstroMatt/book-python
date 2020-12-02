**************
Mapping Nested
**************


Dict Keys
=========
.. code-block:: python

    data = {
        (1,): 'setosa',
        (2,): 'virginica',
        (3,): 'versicolor',
    }

.. code-block:: python

    data = {
        (5.8, 2.7, 5.1, 1.9): 'virginica',
        (5.1, 3.5, 1.4, 0.2): 'setosa',
        (5.7, 2.8, 4.1, 1.3): 'versicolor',
    }

.. code-block:: python

    data = {
        {1}: 'setosa',
        {1,2,3}: 'virginica',
    }
    # Traceback (most recent call last):
    # TypeError: unhashable type: 'set'

.. code-block:: python

    data = {
        [1]: 'setosa',
        [1,2,3]: 'virginica',
    }
    # Traceback (most recent call last):
    # TypeError: unhashable type: 'list'


Dict Values
===========
.. highlights::
    * Value can be any object

.. code-block:: python

    data = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }

.. code-block:: python

    data = {
        'virginica': (5.8, 2.7, 5.1, 1.9),
        'setosa': (5.1, 3.5, 1.4, 0.2),
        'versicolor': (5.7, 2.8, 4.1, 1.3),
    }

.. code-block:: python

    data = {
        'virginica': [5.8, 2.7, 5.1, 1.9],
        'setosa': (5.1, 3.5, 1.4, 0.2),
        'versicolor': {5.7, 2.8, 4.1, 1.3},
    }

.. code-block:: python

    data = {
        'commander': {'firstname': 'Jan', 'lastname': 'Twardowski'},
        'medical_officer': {'firstname': 'José', 'lastname': 'Jiménez'},
        'flight_engineer': {'firstname': 'Иван', 'lastname': 'Иванович'},
    }

.. code-block:: python

    data = {
        'date': '1969-07-21',
        'age': 42,
        'astronaut': {'name': 'Jan Twardowski', 'medals': {'Medal of Honor', 'Purple Heart'}},
        'agency': ['POLSA', 'Roscosmos', 'ESA'],
        'location': ('Baikonur', 'Johnson Space Center'),
    }

.. code-block:: python

    data = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]

.. code-block:: python

    data = [{'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
            {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
            {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'}]

.. code-block:: python

    data = [{'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
            {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
            {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'}]


List of Dicts
=============
.. code-block:: python
    :caption: GetItem

    data = [{'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
            {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
            {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'}]

    data[0]
    # {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa')

    data[0]['measurements']
    # [4.7, 3.2, 1.3, 0.2]

    data[0]['measurements'][2]
    # 1.3

    data[0]['species']
    # 'setosa'

    data[0].get('kind')
    # None

    data[0].get('kind', 'n/a')
    # 'n/a'

    data[2].get('measurements')
    # [7.6, 3.0, 6.6, 2.1]

    data[2].get('measurements')[1]
    # 3.0

.. code-block:: python
    :caption: Length

    data = [{'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
            {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
            {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'}]

    len(data)
    # 3

    len(data[0])
    # 2

    len(data[1])
    # 2

    len(data[1]['species'])
    # 10

    len(data[1]['measurements'])
    # 4


Assignments
===========
.. todo:: Create assignments
