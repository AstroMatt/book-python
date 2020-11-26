.. _Builtin Keywords:

****************
Builtin Keywords
****************

* https://www.programiz.com/python-programming/keyword-list

List of keywords
================
.. code-block:: python

    import keyword

    print(keyword.kwlist)
    # ['False', 'None', 'True', 'and',
    #  'as', 'assert', 'async', 'await',
    #  'break', 'class', 'continue', 'def',
    #  'del', 'elif', 'else', 'except',
    #  'finally', 'for', 'from', 'global',
    #  'if', 'import', 'in', 'is', 'lambda',
    #  'nonlocal', 'not', 'or', 'pass',
    #  'raise', 'return', 'try', 'while',
    #  'with', 'yield']


``pass``
========
* Avoid error when you don't specify the body of a block

.. code-block:: python
    :caption: Exceptions has all the content needed inherited from ``Exception`` class. You need something to avoid ``IndentationError``
    :emphasize-lines: 2

    class MyError(Exception):


    print('hello')
    # Traceback (most recent call last):
    # IndentationError: expected an indented block

.. code-block:: python
    :emphasize-lines: 2

    class MyError(Exception):
        pass


    print('hello')
    # hello


``__file__``
============
.. code-block:: python

    print(__file__)
    # /home/twardowski/bin/myfile.py

.. code-block:: python

    from os.path import dirname


    dir = dirname(__file__)

    print(f'Working directory: {dir}')
    # Working directory: /home/twardowski/bin

.. code-block:: python

    from os.path import dirname, join


    dir = dirname(__file__)
    path = join(dir, 'main.py')

    print(f'My file: {path}')
    # My file: /home/twardowski/bin/main.py


``del``
=======
.. code-block:: python

    DATA = {
        'firstname': 'Jan',
        'lastname': 'Twardowski',
    }

    print(DATA)
    # {'firstname': 'Jan', 'lastname': 'Twardowski'}

    del DATA['firstname']

    print(DATA)
    # {'lastname': 'Twardowski'}
