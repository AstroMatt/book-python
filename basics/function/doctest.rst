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
    * View menu -> Run... -> Doctest in ``my_function``

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

.. code-block:: python

    >>> DATA = [
    ...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    ...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    ...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ... ]

    >>> DATA
    ... # doctest: +NORMALIZE_WHITESPACE
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

Function Doctest Temperature
----------------------------
* Assignment name: Function Doctest Temperature
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_doctest_temperature.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write implementation of a function ``celsius_to_kelvin``
    #. All tests must pass

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Napisz implementację funkcji ``celsius_to_kelvin``
    #. Wszystkie testy muszą przechodzić

:Input:
    .. code-block:: python

        def celsius_to_kelvin(degrees):
            """
            >>> celsius_to_kelvin(0)
            273.15
            >>> celsius_to_kelvin(1)
            274.15
            >>> celsius_to_kelvin(-1)
            272.15
            >>> celsius_to_kelvin('a')
            Traceback (most recent call last):
                ...
            TypeError: Invalid argument
            >>> celsius_to_kelvin([0, 1])
            [273.15, 274.15]
            >>> celsius_to_kelvin((0, 1))
            (273.15, 274.15)
            >>> celsius_to_kelvin({0, 1})
            {273.15, 274.15}
            """
            return ...

Function Doctest Distance
-------------------------
* Assignment name: Function Doctest Distance
* Complexity level: easy
* Lines of code to write: 21 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/function_doctest_distance.py`
* Last update: 2020-10-01

:English:
    #. Write functions which convert distance given in kilometers to meters
    #. 1 km = 1000 m
    #. Distance cannot be negative
    #. Returned value must by float
    #. Write doctests
    #. All tests must pass

:Polish:
    #. Napisz funkcję, która przeliczy dystans podany w kilometrach na metry
    #. 1 km = 1000 m
    #. Dystans nie może być ujemny
    #. Zwracany dystans musi być float
    #. Napisz doctesty
    #. Wszystkie testy muszą przechodzić

:Output:
    * Test arguments:

        * -1
        * 0
        * 1
        * ``float``
        * ``int``
        * ``str`` -> expect ``TypeError``
        * any other type -> expect ``TypeError``
        * True

Function Doctest Regexp
-----------------------
* Assignment name: Function Doctest Regexp
* Complexity level: hard
* Lines of code to write: 0 lines (**discussion only**)
* Estimated time of completion: 5 min
* Solution: TODO
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Pattern incorrectly classifies ``https://foo_bar.example.com/`` as invalid
    #. Fix pattern without automated tests
    #. Don't break classification of the other cases

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wyrażenie niepoprawnie klasyfikuje ``https://foo_bar.example.com/`` jako nieprawidłowy
    #. Popraw wyrażenie bez testów automatycznych
    #. Nie zepsuj klasyfikacji pozostałych przypadków

:Input:
    .. code-block:: python
        :caption: @diegoperini --  https://mathiasbynens.be/demo/url-regex

        PATTERN = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

        VALID = [
            'http://foo.com/blah_blah',
            'http://foo.com/blah_blah/',
            'http://foo.com/blah_blah_(wikipedia)',
            'http://foo.com/blah_blah_(wikipedia)_(again)',
            'http://www.example.com/wpstyle/?p=364',
            'https://www.example.com/foo/?bar=baz&inga=42&quux',
            'http://✪df.ws/123',
            'http://userid:password@example.com:8080',
            'http://userid:password@example.com:8080/',
            'http://userid@example.com',
            'http://userid@example.com/',
            'http://userid@example.com:8080',
            'http://userid@example.com:8080/',
            'http://userid:password@example.com',
            'http://userid:password@example.com/',
            'http://142.42.1.1/',
            'http://142.42.1.1:8080/',
            'http://➡.ws/䨹',
            'http://⌘.ws',
            'http://⌘.ws/',
            'http://foo.com/blah_(wikipedia)#cite-1',
            'http://foo.com/blah_(wikipedia)_blah#cite-1',
            'http://foo.com/unicode_(✪)_in_parens',
            'http://foo.com/(something)?after=parens',
            'http://☺.damowmow.com/',
            'http://code.google.com/events/#&product=browser',
            'http://j.mp',
            'ftp://foo.bar/baz',
            'http://foo.bar/?q=Test%20URL-encoded%20stuff',
            'http://مثال.إختبار',
            'http://例子.测试',
            'http://उदाहरण.परीक्षा',
            'http://-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com',
            'http://1337.net',
            'http://a.b-c.de',
            'http://223.255.255.254',
            'https://foo_bar.example.com/',
        ]

        INVALID = [
            'http://',
            'http://.',
            'http://..',
            'http://../',
            'http://?',
            'http://??',
            'http://??/',
            'http://#',
            'http://##',
            'http://##/',
            'http://foo.bar?q=Spaces',
            '//',
            '//a',
            '///a',
            '///',
            'http:///a',
            'foo.com',
            'rdar://1234',
            'h://test',
            'http:// shouldfail.com',
            ':// should fail',
            'http://foo.bar/foo(bar)baz quux',
            'ftps://foo.bar/',
            'http://-error-.invalid/',
            'http://a.b--c.de/',
            'http://-a.b.co',
            'http://a.b-.co',
            'http://0.0.0.0',
            'http://10.1.1.0',
            'http://10.1.1.255',
            'http://224.1.1.1',
            'http://1.1.1.1.1',
            'http://123.123.123',
            'http://3628126748',
            'http://.www.foo.bar/',
            'http://www.foo.bar./',
            'http://.www.foo.bar./',
            'http://10.1.1.1',
            'http://10.1.1.254',
        ]
