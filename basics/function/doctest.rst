.. _Function Doctest:

****************
Function Doctest
****************


Rationale
=========
.. highlights::
    * Tests are always the most up-to-date code documentation
    * Tests cannot get out of sync from code
    * Checks if function output is exactly as expected
    * Useful for regex modifications
    * Can add text (i.e. explanations) between tests
    * Case Study: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_base.py#L409


Syntax
======
.. highlights::
    * Docstring is a first multiline comment in: File/Module, Class, Method/Function
    * Used for generating ``help()`` documentation
    * It is accessible in ``__doc__`` property of an object
    * Used for ``doctest``
    * :pep:`257` Docstring convention - For multiline always use three double quote (``"""``) characters
    * More information in :ref:`Function Doctest`

.. code-block:: python
    :caption: Docstring used for doctest

    def apollo_dsky(noun, verb):
        """
        This is the Apollo Display Keyboard
        It takes noun and verb

        >>> apollo_dsky(6, 61)
        Program selected. Noun: 06, verb: 61

        >>> apollo_dsky(16, 68)
        Program selected. Noun: 16, verb: 68
        """
        print(f'Program selected. Noun: {noun:02}, verb: {verb:02}')


Running Tests
=============
#. Note, that doctests are not discovered in scratch files in PyCharm
#. Running tests in Pycharm IDE (either option):

    * Right click on source code with doctests -> Run 'Doctest for ...'
    * View menu -> Run... -> Doctest in ``myfunction``

#. Running Tests from Python Code:

    .. code-block:: python

        if __name__ == "__main__":
            import doctest
            doctest.testmod()

#. Running tests from command line:

    .. code-block:: console
        :caption: Display only errors. With ``-v`` display progress

        $ python -m doctest myfile.py
        $ python -m doctest -v myfile.py


Test Int, Float
===============
.. code-block:: python
    :caption: ``int`` values

    def add_numbers(a, b):
        """
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(-1, 1)
        0
        >>> add_numbers(0, 0)
        0
        """
        return a + b

.. code-block:: python
    :caption: ``float`` values

    def add_numbers(a, b):
        """
        >>> add_numbers(2.5, 1.2)
        3.7

        >>> add_numbers(0.1, 0.2)
        0.30000000000000004

        >>> add_numbers(0.1, 0.2)  # doctest: +ELLIPSIS
        0.3000...
        """
        return a + b


Test Bool
=========
.. code-block:: python

    AGE_ADULT = 18

    def is_adult(age):
        """
        Function checks if person is adult.
        Adult person is over 18 years old.

        >>> is_adult(18)
        True

        >>> is_adult(17.9)
        False
        """
        if age >= AGE_ADULT:
            return True
        else:
            return False


Test Str
========
.. highlights::
    * Python will change to single quotes in most cases
    * Python will change to double quotes to avoid escapes
    * ``print()`` function output, don't have quotes

.. code-block:: python
    :caption: Returning ``str``. Python will change to single quotes in most cases
    :emphasize-lines: 3-4,7-8,11-12,15-16

    def echo(text):
        """
        >>> echo('hello')
        'hello'

        # Python will change to single quotes in most cases
        >>> echo("hello")
        'hello'

        Following test will fail
        >>> echo('hello')
        "hello"

        Python will change to double quotes to avoid escapes
        >>> echo('It\\'s Twardowski\\'s Moon')
        "It's Twardowski's Moon"
        """
        return text

.. code-block:: python
    :caption: There are no quotes in ``print()`` function output
    :emphasize-lines: 4

    def echo(text):
        """
        >>> echo('hello')
        hello
        """
        print(text)

.. code-block:: python
    :caption: Testing ``print(str)`` with newlines
    :emphasize-lines: 7

    def echo(text):
        """
        >>> echo('hello')
        hello
        hello
        hello
        <BLANKLINE>
        """
        print(f'{text}\n' * 3)

.. code-block:: text

    >>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    ...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    ...         (4.7, 3.2, 1.3, 0.2, 'setosa')]

    >>> DATA  # doctest: +NORMALIZE_WHITESPACE
    [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
    """


Test Sequences
==============
.. code-block:: python
    :caption: Test Sequences

    def celsius_to_kelvin(sequence):
        """
        >>> celsius_to_kelvin([1,2,3])
        [274.15, 275.15, 276.15]

        >>> celsius_to_kelvin((1,2,3))
        [274.15, 275.15, 276.15]

        >>> celsius_to_kelvin({1,2,3})
        [274.15, 275.15, 276.15]

        >>> celsius_to_kelvin(frozenset({1,2,3}))
        [274.15, 275.15, 276.15]
        """
        return [x + 273.15 for x in sequence]

.. code-block:: python
    :caption: Test Sequences

    def celsius_to_kelvin(sequence):
        """
        >>> celsius_to_kelvin([1,2,3])
        [274.15, 275.15, 276.15]

        >>> celsius_to_kelvin((1,2,3))
        (274.15, 275.15, 276.15)

        >>> celsius_to_kelvin({1,2,3})
        {274.15, 275.15, 276.15}

        >>> celsius_to_kelvin(frozenset({1,2,3}))
        frozenset({274.15, 275.15, 276.15})
        """
        cls = type(sequence)
        return cls(x + 273.15 for x in sequence)


Test Exceptions
===============
.. code-block:: python
    :caption: Testing for exceptions
    :emphasize-lines: 3-6

    def add_numbers(a, b):
        """
        >>> add_numbers('one', 'two')
        Traceback (most recent call last):
            ...
        TypeError: Argument must be int or float
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b

.. code-block:: python
    :caption: This test will fail. Expected exception, got 2.0

    def add_numbers(a, b):
        """
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if not isinstance(a, (int, float)):
            raise ValueError('not a number')

        if not isinstance(b, (int, float)):
            raise ValueError('not a number')

        return a + b

    # Expected:
    #     Traceback (most recent call last):
    #         ...
    #     ValueError: not a number
    # Got:
    #     2.0

.. code-block:: python
    :caption: This test will pass.

    def add_numbers(a, b):
        """
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if type(a) not in (int, float):
            raise ValueError('not a number')

        if type(b) not in (int, float):
            raise ValueError('not a number')

        return a + b


Test Python Expressions
=======================
.. code-block:: python
    :caption: Using python statements in ``doctest``
    :emphasize-lines: 3-5

    def when(date):
        """
        >>> from datetime import datetime, timezone
        >>> moon = datetime(1969, 7, 21, 17, 54, tzinfo=timezone.utc)
        >>> when(moon)
        1969-07-21 17:54 UTC
        """
        print(f'{date:%Y-%m-%d %H:%M %Z}')

Flags
=====
* ``DONT_ACCEPT_TRUE_FOR_1``
* ``DONT_ACCEPT_BLANKLINE``
* ``NORMALIZE_WHITESPACE``
* ``ELLIPSIS``
* ``IGNORE_EXCEPTION_DETAIL``
* ``SKIP``
* ``COMPARISON_FLAGS``
* ``REPORT_UDIFF``
* ``REPORT_CDIFF``
* ``REPORT_NDIFF``
* ``REPORT_ONLY_FIRST_FAILURE``
* ``FAIL_FAST``
* ``REPORTING_FLAGS``


Examples
========
.. code-block:: python
    :caption: Adding two numbers

    def add_numbers(a, b):
        """
        >>> add_numbers(1, 2)
        3.0
        >>> add_numbers(-1, 1)
        0.0
        >>> add_numbers(0.1, 0.2)  # doctest: +ELLIPSIS
        0.3000...
        >>> add_numbers(1.5, 2.5)
        4.0
        >>> add_numbers(1, 1.5)
        2.5
        >>> add_numbers([1, 2], 3)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers(0, [1, 2])
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers('one', 'two')
        Traceback (most recent call last):
            ...
        ValueError: not a number
        >>> add_numbers(True, 1)
        Traceback (most recent call last):
            ...
        ValueError: not a number
        """
        if type(a) not in (int, float):
            raise ValueError('not a number')

        if type(b) not in (int, float):
            raise ValueError('not a number')

        return float(a + b)

.. code-block:: python
    :caption: Celsius to Kelvin temperature conversion

    def celsius_to_kelvin(celsius):
        """
        >>> celsius_to_kelvin(0)
        273.15

        >>> celsius_to_kelvin(1)
        274.15

        >>> celsius_to_kelvin(-1)
        272.15

        >>> celsius_to_kelvin(-273.15)
        0.0

        >>> celsius_to_kelvin(-273.16)
        Traceback (most recent call last):
            ...
        ValueError: Negative Kelvin

        >>> celsius_to_kelvin(-300)
        Traceback (most recent call last):
            ...
        ValueError: Negative Kelvin

        >>> celsius_to_kelvin(True)
        Traceback (most recent call last):
            ...
        TypeError: Argument must be: int, float or Sequence[int, float]

        >>> celsius_to_kelvin([0, 1, 2, 3])
        [273.15, 274.15, 275.15, 276.15]

        >>> celsius_to_kelvin({0, 1, 2, 3})
        {273.15, 274.15, 275.15, 276.15}

        >>> celsius_to_kelvin([0, 1, 2, -300])
        Traceback (most recent call last):
            ...
        ValueError: Negative Kelvin

        >>> celsius_to_kelvin([0, 1, [2, 3], 3])
        [273.15, 274.15, [275.15, 276.15], 276.15]
        """
        datatype = type(celsius)

        if type(celsius) in {list, tuple, set, frozenset}:
            return datatype(celsius_to_kelvin(x) for x in celsius)

        if datatype not in {int, float}:
            raise TypeError('Argument must be: int, float or Sequence[int, float]')

        kelvin = celsius + 273.15

        if kelvin < 0.0:
            raise ValueError('Negative Kelvin')

        return float(kelvin)


Assignments
===========

.. literalinclude:: solution/function_doctest_temperature.py
    :caption: :download:`Solution <solution/function_doctest_temperature.py>`
    :end-before: # Solution

.. literalinclude:: solution/function_doctest_distance.py
    :caption: :download:`Solution <solution/function_doctest_distance.py>`
    :end-before: # Solution

.. literalinclude:: solution/function_doctest_regexp.py
    :caption: :download:`Solution <solution/function_doctest_regexp.py>`
    :end-before: # Solution
