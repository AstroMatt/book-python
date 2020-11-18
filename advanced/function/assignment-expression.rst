.. _Assignment Expression:

*********************
Assignment Expression
*********************


Rationale
=========
* Since Python 3.8
* :pep:`572` Assignment Expressions (walrus operator)


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

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

    result = []

    for line in DATA:
        X = [float(x) for x in line.split(',')[0:4]]
        result.append(X)

    print(result)
    # [[5.8, 2.7, 5.1, 1.9],
    #  [5.1, 3.5, 1.4, 0.2],
    #  [5.7, 2.8, 4.1, 1.3]]

.. code-block:: python

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

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

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

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

    DATA = [
        {'is_astronaut': True,  'name': 'JaN TwarDOwski'},
        {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
        {'is_astronaut': False, 'name': 'José Maria Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    astronauts = [{'firstname': name[0], 'lastname': name[-1]}
                  for person in DATA
                  if person['is_astronaut']
                  and (name := person['name'].title().split())]

    print(astronauts)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python

    DATA = [
        {'is_astronaut': True,  'name': 'JaN TwarDOwski'},
        {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
        {'is_astronaut': False, 'name': 'José Maria Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    astronauts = [{'firstname': fname, 'lastname': lname}
                  for person in DATA
                  if person['is_astronaut']
                  and (name := person['name'].title().split())
                  and (fname := name[0])
                  and (lname := name[-1])]

    print(astronauts)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    result = [cls(*features)
              for *features, species in DATA[1:]
              if (clsname := species.capitalize())
              and (cls := globals()[clsname])]


Assignments
===========
.. todo:: Create assignments
