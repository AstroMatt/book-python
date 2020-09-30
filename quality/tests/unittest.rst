************
Unit Testing
************

.. figure:: img/geek-and-poke-development-driven-tests.jpg
    :align: center
    :width: 75%

    Development driven tests

* https://martinfowler.com/articles/microservice-testing/#testing-component-out-of-process-diagram
* https://docs.python.org/3/library/unittest.mock.html


Glossary
========
.. glossary::

    Stub
        A method stub or simply stub in software development is a piece of code used to stand in for some other programming functionality. A stub may simulate the behavior of existing code (such as a procedure on a remote machine) or be a temporary substitute for yet-to-be-developed code. Stubs are therefore most useful in porting, distributed computing as well as general software development and testing.

    Mock
        In object-oriented programming, mock objects are simulated objects that mimic the behavior of real objects in controlled ways. In a unit test, mock objects can simulate the behavior of complex, real objects and are therefore useful when a real object is impractical or impossible to incorporate into a unit test.

    Unittest
        In computer programming, unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use.


Running tests
=============

Running tests with your IDE
---------------------------
* View menu -> Run... -> Unittest in ``my_function``

From code
---------
.. code-block:: python

    if __name__ == "__main__":
        import unittest
        unittest.main()

From command line
-----------------
.. code-block:: console
    :caption: Display only errors. With ``-v`` display progress

    $ python -m unittest example.py
    $ python -m unittest -v example.py


Examples
========

Example 1
---------
.. literalinclude:: src/unittest-example-1.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 2
---------
.. literalinclude:: src/unittest-example-2.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 3
---------
.. literalinclude:: src/unittest-example-3.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 4
---------
.. literalinclude:: src/unittest-example-4.py
    :language: python
    :caption: Example ``unittest`` code coverage

Example 5
---------
.. literalinclude:: src/unittest-example-5.py
    :language: python
    :caption: Example ``unittest`` code coverage

Mock
====
* Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used.

.. code-block:: python

    from unittest.mock import MagicMock

    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)

    thing.method(3, 4, 5, key='value')
    # 3

    thing.method.assert_called_with(3, 4, 5, key='value')

Side effect
-----------
* Raising an exception when a mock is called

.. code-block:: python

    from unittest.mock import Mock

    mock = Mock(side_effect=KeyError('foo'))

    mock()
    # Traceback (most recent call last):
    #  ...
    # KeyError: 'foo'

patch
-----
* The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends

.. code-block:: python

    from unittest.mock import patch

    @patch('module.ClassName2')
    @patch('module.ClassName1')
    def test(MockClass1, MockClass2):
        module.ClassName1()
        module.ClassName2()
        assert MockClass1 is module.ClassName1
        assert MockClass2 is module.ClassName2
        assert MockClass1.called
        assert MockClass2.called


    test()

.. code-block:: python

    from unittest.mock import patch

    class MyClass:
        def method(self)
            pass

    with patch.object(MyClass, 'method', return_value=None) as mock_method:
        thing = MyClass()
        thing.method(1, 2, 3)

    mock_method.assert_called_once_with(1, 2, 3)

Stub
====
* writing classes or functions but not yet implementing them
* After you have planned a module or class, for example by drawing it's UML diagram, you begin implementing it.
* As you may have to implement a lot of methods and classes, you begin with stubs.
* This simply means that you only write the definition of a function down and leave the actual code for later.

.. code-block:: python

    class Foo:
         def bar(self):
             raise NotImplementedError

         def tank(self):
             raise NotImplementedError

Assignments
===========

Dragon
------
* Complexity level: medium
* Lines of code to write: 100 lines
* Estimated time of completion: 21 min
* Solution: TODO

:English:
    #. Write unittest for the dragon from :ref:`Dragon Alpha`

:Polish:
    #. Napisz testy jednostkowe dla Smoka z :ref:`Dragon Alpha`
