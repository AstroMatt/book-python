.. _Assignment Expression:

*********************
Assignment Expression
*********************


Recap
=====
.. code-block:: python

    result = [x for x in range(0,10)]
    result = [x for x in range(0,10) if x%2 == 0]


Rationale
=========
* Since Python 3.8
* :pep:`572` Assignment Expressions (walrus operator)


.. code-block:: python

    DATA = ['Jan Twardowski',
            'Melissa Lewis',
            'Mark Watney']


    result = [(name.split()[0], name.split()[1])
              for name in DATA]
    # [('Jan', 'Twardowski'),
    #  ('Melissa', 'Lewis'),
    #  ('Mark', 'Watney')]

    result = [{'firstname': name.split()[0],
               'lastname': name.split()[1]}
              for name in DATA]
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'}]

    result = [{'firstname': astro[0],
               'lastname': astro[1]}
              for name in DATA
              if (astro := name.split())]
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'}]


Syntax
======
.. code-block:: text

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)]

.. code-block:: text

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)]

.. code-block:: text

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)
              or (<VARIABLE4> := <EXPR>)]

Example
=======
.. code-block:: python

    DATA = ['5.8,2.7,5.1,1.9,virginica',
            '5.1,3.5,1.4,0.2,setosa',
            '5.7,2.8,4.1,1.3,versicolor']

    result = []

    for line in DATA:
        X = [float(x) for x in line.split(',')[0:4]]
        result.append(X)

    print(result)
    # [[5.8, 2.7, 5.1, 1.9],
    #  [5.1, 3.5, 1.4, 0.2],
    #  [5.7, 2.8, 4.1, 1.3]]

.. code-block:: python

    DATA = ['5.8,2.7,5.1,1.9,virginica',
            '5.1,3.5,1.4,0.2,setosa',
            '5.7,2.8,4.1,1.3,versicolor']

    result = [[float(x) for x in X]
              for line in DATA
              if (X := line.split(',')[0:4])]

    print(result)
    # [[5.8, 2.7, 5.1, 1.9],
    #  [5.1, 3.5, 1.4, 0.2],
    #  [5.7, 2.8, 4.1, 1.3]]


Use Case
========
.. code-block:: python

    DATA = ['5.8,2.7,5.1,1.9,virginica',
            '5.1,3.5,1.4,0.2,setosa',
            '5.7,2.8,4.1,1.3,versicolor']

    result = [[float(x) for x in X] + [y]
              for line in DATA
              if (row := line.split(','))
              and (X := row[0:4])
              and (y := row[4])]

    print(result)
    # [[5.8, 2.7, 5.1, 1.9, 'virginica'],
    #  [5.1, 3.5, 1.4, 0.2, 'setosa'],
    #  [5.7, 2.8, 4.1, 1.3, 'versicolor']]

.. code-block:: python

    DATA = [{'is_astronaut': True,  'name': 'JaN TwarDOwski'},
            {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
            {'is_astronaut': False, 'name': 'José Maria Jiménez'},
            {'is_astronaut': True,  'name': 'Melissa Lewis'},
            {'is_astronaut': False, 'name': 'Alex Vogel'}]

    result = [{'firstname': person['name'].title().split()[0],
               'lastname': person['name'].title().split()[-1]}
              for person in DATA
              if person['is_astronaut']]

    result = [{'firstname': name[0],
               'lastname': name[-1]}
              for person in DATA
              if person['is_astronaut']
              and (name := person['name'].title().split())]

    result = [{'firstname': fname,
               'lastname': lname}
              for person in DATA
              if person['is_astronaut']
              and (name := person['name'].title().split())
              and (fname := name[0])
              and (lname := name[-1])]

    print(result)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python

    from dataclasses import dataclass
    from pprint import pprint


    @dataclass
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float


    class Versicolor(Iris):
        pass

    class Virginica(Iris):
        pass

    class Setosa(Iris):
        pass


    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor')]

    result = [cls(*features)
              for *features, species in DATA[1:]
              if (clsname := species.capitalize())
              and (cls := globals()[clsname])]


    pprint(result)
    # [Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
    #  Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
    #  Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
    #  Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
    #  Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
    #  Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2),
    #  Versicolor(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4)]


Assignments
===========
.. todo:: Create assignments
