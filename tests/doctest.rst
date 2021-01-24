*******
Doctest
*******


* tests are always the most up-to-date code documentation
* tests cannot get out of sync from code
* checks if function is outputs expected result
* useful for regex modifications
* can add text (i.e. explanations) between tests
* Case Study: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/base.py#L409
* PyCharm doctest runner warns about ``DeprecationWarning``, fix in progress -  https://youtrack.jetbrains.com/issue/PY-31751


Running tests
=============

Running tests with your IDE
---------------------------
* View menu -> Run... -> Doctest in ``my_function``

From code
---------
.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

From command line
-----------------
.. code-block:: console
    :caption: Display only errors

    python -m doctest example.py

.. code-block:: console
    :caption: With ``-v`` display progress

    python -m doctest -v example.py


Test for ``bool`` return values
===============================
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


Test numeric return values
==========================

``int`` values
--------------
.. code-block:: python

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

``float`` values
----------------
.. code-block:: python

    def add_numbers(a, b):
        """
        >>> add_numbers(2.5, 1.2)
        3.7
        """
        return a + b


Test for ``str`` return values
==============================

Returning ``str``
-----------------
.. code-block:: python

    def echo(text):
        """
        >>> echo('hello')
        'hello'
        """
        return text

.. code-block:: python

    def echo(text='default text'):
        """
        >>> echo()
        'default text'
        """
        return text

Python forces single quotes
---------------------------
* Those tests will fail, because of quotes

 .. code-block:: python
    :caption: Test will fail, Python will automatically change to single quotes
    :emphasize-lines: 4

     def echo(text):
        """
        >>> echo('hello')
        "hello"
        """
        return text

 .. code-block:: python
    :caption: Test will fail, Python will automatically change to single quotes
    :emphasize-lines: 4

     def echo(text):
        """
        >>> echo("hello")
        "hello"
        """
        return text

Python changes to single quotes to avoid escapes
------------------------------------------------
 .. code-block:: python
    :caption: Python will automatically change quotes to avoid escapes
    :emphasize-lines: 3,4

     def echo(text):
        """
        >>> echo('It\\'s Twardowski\\'s Moon')
        "It's Twardowski's Moon"
        """
        return text

Testing ``print(str)``
----------------------
.. code-block:: python
    :caption: ``print`` function results, don't have quotes
    :emphasize-lines: 4

    def echo(text):
        """
        >>> echo('hello')
        hello
        """
        print(text)

.. code-block:: python
    :caption: ``print`` function results, don't have quotes
    :emphasize-lines: 4

    def echo(text='default text'):
        """
        >>> hello()
        default text
        """
        print(text)

Testing ``print(str)`` with newlines
------------------------------------
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


Testing for exceptions
======================
.. code-block:: python
    :caption: Testing for exceptions
    :emphasize-lines: 3-6

    def add_numbers(a, b):
        """
        >>> add_numbers([1, 2])
        Traceback (most recent call last):
            ...
        TypeError: add_numbers() missing 1 required positional argument: 'b'
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b


Using python statements in ``doctest``
======================================
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

Celsius to Kelvin temperature conversion
----------------------------------------
.. literalinclude:: src/doctest-corner-cases.py
    :language: python
    :caption: Celsius to Kelvin temperature conversion

Email regex
-----------
.. code-block:: python
    :caption: Function check email address against Regular Expression

    import re

    VALID_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'


    def is_valid_email(email: str) -> bool:
        """
        >>> is_valid_email('jose.jimenez@nasa.gov')
        True
        >>> is_valid_email('Jose.Jimenez@nasa.gov')
        True
        >>> is_valid_email('+jose.jimenez@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez+@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez@.gov')
        False
        >>> is_valid_email('@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez@nasa.g')
        False
        """
        if re.match(VALID_EMAIL, email):
            return True
        else:
            return False

URL Regex
---------
.. code-block:: python

    # @diegoperini --  https://mathiasbynens.be/demo/url-regex
    REGEX = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

    def is_valid_url(url):
        if re.match(REGEX, url):
            return True
        else:
            return False

Assignments
===========

Refactoring
-----------
* Complexity level: easy
* Lines of code to write: 5 lines of code
* Estimated time of completion: 15 min
* Filename: :download:`solution/doctest_temp.py`

:English:
    #. Write implementation of a function from input code (see below)
    #. All tests must pass

:Polish:
    #. Napisz implementację funkcji z kodu wejściowego (patrz poniżej)
    #. Wszystkie testy muszą przechodzić

:Input Code:
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

Distance conversion doctest
---------------------------
* Complexity level: easy
* Lines of code to write: 5 lines of code + 16 lines of tests
* Estimated time of completion: 10 min
* Filename: :download:`solution/doctest_distance.py`

:English:
    #. Write functions which convert distance given in kilometers to meters
    #. 1 km = 1000 m
    #. Distance cannot be negative
    #. Returned value must by float
    #. Write doctests

:Polish:
    #. Napisz funkcję, która przeliczy dystans podany w kilometrach na metry
    #. 1 km = 1000 m
    #. Dystans nie może być ujemny
    #. Zwracany dystans musi być float
    #. Napisz doctesty

:Output:
    * Test arguments:

        * -1
        * 0
        * 1
        * ``float``
        * ``int``
        * ``str`` -> expect ``TypeError``
        * any other type -> expect ``TypeError``

Fix URL Regex
-------------
* Complexity level: hard
* Lines of code to write: 0 lines (**discussion only**)
* Estimated time of completion: 5 min

:English:
    #. Copy code input from listing below
    #. Pattern incorrectly classifies ``https://foo_bar.example.com/`` as invalid
    #. Fix pattern without automated tests
    #. Don't break classification of the other cases

:Polish:
    #. Skopiuj kod z listingu poniżej
    #. Wyrażenie niepoprawnie klasyfikuje ``https://foo_bar.example.com/`` jako nieprawidłowy
    #. Popraw wyrażenie bez testów automatycznych
    #. Nie zepsuj klasyfikacji pozostałych przypadków

:Input:
    .. code-block:: python

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
