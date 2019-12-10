*********
``tuple``
*********


* Can store elements of any types
* Immutable - cannot add, modify or remove items


Initializing
============
* ``tuple()`` is more readable
* ``()`` is used more often

Initialize empty
----------------
.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

Initialize with one element
---------------------------
* Single element ``tuple`` require comma at the end (**important!**)
* Brackets are optional

.. code-block:: python

    my_tuple = 1,
    my_tuple = (1,)

Initialize with many elements
-----------------------------
* Comma after last element is optional
* Brackets are optional

.. code-block:: python

    my_tuple = 1, 2
    my_tuple = (1, 2)

.. code-block:: python

    my_tuple = 1, 2.0, None, False, 'José'
    my_tuple = (1, 2.0, None, False, 'José')


Length of a ``tuple``
=====================
.. code-block:: python

    my_tuple = (1, 2, 3)

    len(my_tuple)           # 3


Assignments
===========

Create
------
* Filename: ``sequences_tuple.py``
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

.. csv-table:: Pomiary Iris
    :name: sequences-tuple-iris
    :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"
    "6.3", "2.9", "5.6", "1.8", "virginica"
    "6.4", "3.2", "4.5", "1.5", "versicolor"
    "4.7", "3.2", "1.3", "0.2", "setosa"
    "7.0", "3.2", "4.7", "1.4", "versicolor"
    "7.6", "3.0", "6.6", "2.1", "virginica"
    "4.9", "3.0", "1.4", "0.2", "setosa"
    "4.9", "2.5", "4.5", "1.7", "virginica"
    "7.1", "3.0", "5.9", "2.1", "virginica"

#. Dane są pomiary :numref:`sequences-tuple-iris`
#. Stwórz ``tuple`` z nazwami gatunków
#. Wylicz średnią arytmetyczną dla każdej z kolumn
