****************
Parameter Syntax
****************


Recap
=====
.. code-block:: python

    def echo(a, b, c=3):
         print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Keyword-only parameters
=======================
* All parameters after ``*`` must be keyword-only

.. code-block:: python

    def echo(a, *, b, c=3):
        print(a, b, c)

    echo(1, 2)              # TypeError: echo() takes 1 positional argument but 2 were given
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required keyword-only argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 1 positional argument but 3 were given
    echo(1, 2, c=3)         # TypeError: echo() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Positional-only parameters
==========================
.. versionadded:: Python 3.8
    See :pep:`570` Python Positional-Only Parameters

* All parameters before ``/`` must be positional-only

.. code-block:: python

    def echo(a, /, b, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Positional and Keyword parameters
=================================
.. code-block:: python

    def echo(a, /, b, *, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 2 positional arguments but 3 were given
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Examples
========
.. code-block:: python
    :caption: https://docs.python.org/3/library/functions.html#sorted

    sorted(iterable, *, key=None, reverse=False)

.. code-block:: python
    :caption: https://docs.python.org/3/library/functions.html#sum

    sum(iterable, /, start=0)

.. code-block:: python

    def add(a, b, /):
        return a + b

    def divmod(a, b, /):
        return (a // b, a % b)

    def quantiles(dist, /, *, n=4, method='exclusive')
        ...


Assignments
===========

Function Parameter Syntax Kwargs
--------------------------------
* Assignment name: Function Parameter Syntax Kwargs
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_parameter_syntax_kwargs.py`

:English:
    #. Create function ``set_position``
    #. Function takes two arguments ``x``, ``y`` and always returns ``None``
    #. Arguments must be passed only as keywords
    #. Test function by running with keyword arguments
    #. Test function by running with positional arguments
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz funckję ``set_position``
    #. Funkcja przyjmuje dwa argumenty ``x``, ``y`` i zawsze zwraca ``None``
    #. Argumenty można podawać tylko nazwanie (keyword)
    #. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    #. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isfunction
        >>> assert callable(set_position)
        >>> assert isfunction(set_position)

        >>> set_position(x=1, y=2)

        >>> set_position()
        Traceback (most recent call last):
            ...
        TypeError: set_position() missing 2 required keyword-only arguments: 'x' and 'y'

        >>> set_position(1)
        Traceback (most recent call last):
            ...
        TypeError: set_position() takes 0 positional arguments but 1 was given

        >>> set_position(1, 2)
        Traceback (most recent call last):
            ...
        TypeError: set_position() takes 0 positional arguments but 2 were given

        >>> set_position(1, y=1)
        Traceback (most recent call last):
            ...
        TypeError: set_position() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

        >>> set_position(x=1, 2)
        Traceback (most recent call last):
            ...
        SyntaxError: positional argument follows keyword argument

Function Parameter Syntax Args
------------------------------
* Assignment name: Function Parameter Syntax Args
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_parameter_syntax_args.py`
* Warning: This assignment will work only in Python 3.8+

:English:
    #. Create function ``take_damage``
    #. Function takes one argument ``dmg`` and always returns ``None``
    #. Argument must be passed only as positional
    #. Test function by running with positional arguments
    #. Test function by running with keyword arguments
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz funckję ``take_damage``
    #. Funkcja przyjmuje jeden argument ``dmg`` i zawsze zwraca ``None``
    #. Argument można podawać tylko pozycyjnie
    #. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
    #. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isfunction
        >>> assert callable(take_damage)
        >>> assert isfunction(take_damage)

        >>> take_damage(1)
        >>> take_damage(1, 2)
        Traceback (most recent call last):
            ...
        TypeError: take_damage() takes 1 positional argument but 2 were given
        >>> take_damage()
        Traceback (most recent call last):
            ...
        TypeError: take_damage() missing 1 required positional argument: 'dmg'
        >>> take_damage(dmg=1)
        Traceback (most recent call last):
            ...
        TypeError: take_damage() got some positional-only arguments passed as keyword arguments: 'dmg'
