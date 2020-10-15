.. _Advanced Annotation Mapping:

******************
Annotation Mapping
******************


Rationale
=========
* Python 3.9 introduced :pep:`585` -- Type Hinting Generics In Standard Collections
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``


Dict
====
.. code-block:: python

    data: dict = {}
    data: dict = dict()

    a: dict[int, str] = {
        0: 'setosa',
        1: 'virginica',
        2: 'versicolor'}

    b: dict[float, str] = {
        5.8: 'Sepal length',
        2.7: 'Sepal width',
        5.1: 'Petal length',
        1.9: 'Petal width'}

    c: dict[str, float] = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9}


List of Dicts
=============
.. code-block:: python

    from typing import Union

    data: list[dict] = [
        {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
        {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
        {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ]

    data: list[dict[str, Union[list[float], str]]] = [
        {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
        {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
        {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ]

    row = list[float]
    data: list[dict[str, Union[row, str]]] = [
        {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
        {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
        {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ]

    features = list[float]
    label = str
    row = dict[str, Union[features, label]]
    data: list[row] = [
        {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
        {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
        {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ]


Typed Dict
==========
.. versionadded:: Python 3.8
    See :pep:`589`

.. code-block:: python

    from typing import TypedDict


    class Point(TypedDict):
        x: int
        y: int


    pt1: Point = {'x':1, 'y':2}         # Ok
    pt2: Point = {'x':1, 'y':2, 'z':0}  # Error
    pt3: Point = Point(x=1, y=2)       # Ok
    pt4: Point = Point(x=1, y=2, z=0)  # Error


More Information
================
.. note:: More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
