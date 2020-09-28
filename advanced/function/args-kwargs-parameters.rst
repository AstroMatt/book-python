******************************
Arbitrary Number of Parameters
******************************


Recap information about function parameters
===========================================
* positional arguments
* keyword arguments
* required parameters
* optional parameters (with default value)
* keyword arguments must be on the right side
* order of keyword arguments doesn't matter

.. code-block:: python

    def echo(a, b):
        print(a)
        print(b)


    echo(1, 2)       # positional arguments
    echo(2, 1)       # positional arguments
    echo(a=1, b=2)   # keyword arguments
    echo(b=2, a=1)   # keyword arguments, order doesn't matter
    echo(1, b=2)     # positional and keyword arguments
    echo(a=1, 2)     # SyntaxError: positional argument follows keyword argument


Positional Parameters
=====================
* ``*`` is used for positional arguments
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``

.. code-block:: python

    def echo(*args):
        print(args)


    echo()                     # ()
    echo(1)                    # (1,)
    echo(2, 3)                 # (2, 3)
    echo('a', 'b')             # ('a', 'b')
    echo('a', 2, 3.3)          # ('a', 2, 3.3)

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)


    echo(1, 2, 3, 4, 5, 6)


Keyword Parameters
==================
* ``**`` is used for keyword arguments
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``

.. code-block:: python

    def echo(**kwargs):
        print(kwargs)


    echo(a=1)                                       # {'a': 1}
    echo(color='red')                               # {'color': 'red'}
    echo(firstname='Jan', lastname='Twardowski')    # {'firstname': 'Jan', 'lastname': Twardowski}

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(kwargs)  # {}


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, d=7, e=8)


Positional and Keyword Parameters
=================================
.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {}


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {}


    echo(1, 2, 3, 4, 5, 6)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # ()
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, d=7, e=8)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d': 7, 'e': 8}


    echo(1, 2, 3, 4, 5, 6, d=7, e=8)


Examples
========
.. code-block:: python
    :caption: Sum

    def sum(*values):
        total = 0

        for value in values:
            total += value

        return total


    sum()            # 0
    sum(1)           # 1
    sum(1, 4)        # 5
    sum(3, 1)        # 4
    sum(1, 2, 3, 4)  # 10

.. code-block:: python
    :caption: Kelvin to Celsius

    def kelvin_to_celsius(*degrees):
        return [x+273.15 for x in degrees]


    kelvin_to_celsius(1)
    # [274.15]

    kelvin_to_celsius(1, 2, 3, 4, 5)
    # [274.15, 275.15, 276.15, 277.15, 278.15]

.. code-block:: python
    :caption: Generate HTML list from function arguments

    def html_list(*fruits):
        print('<ul>')

        for fruit in fruits:
            print(f'<li>{fruit}</li>')

        print('</ul>')


    html_list('apple', 'banana', 'orange')
    # <ul>
    # <li>apple</li>
    # <li>banana</li>
    # <li>orange</li>
    # </ul>

.. code-block:: python
    :caption: Intuitive definition of ``print`` function

    def print(*values, sep=' ', end='\n', ...):
        return sep.join(values) + end


Assignments
===========

Function Args/Kwargs Parameters Define
--------------------------------------
* Complexity level: easy
* Lines of code to write: 4 lines + doctests
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_argskwargs_parameters_define.py`

:English:
    #. Create function ``mean()``, which calculates arithmetic mean
    #. Function can have arbitrary number of positional arguments
    #. Do not import any libraries and modules
    #. Compare result with "Output" section (see below)

:Polish:
    #. Napisz funkcję ``mean()``, wyliczającą średnią arytmetyczną
    #. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów
    #. Nie importuj żadnych biliotek i modułów
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> mean(1)
        1.0
        >>> mean(1, 3)
        2.0
        >>> mean()
        Traceback (most recent call last):
            ...
        ValueError: At least one argument is required

:Hint:
    * ``sum(...) / len(...)``

Function Args/Kwargs Parameters Args
------------------------------------
* Complexity level: easy
* Lines of code to write: 7 lines + doctests
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_argskwargs_parameters_args.py`

:English:
    #. Create function ``isnumeric``
    #. Function can have arbitrary number of positional arguments
    #. Arguments can be of any type
    #. Return ``True`` if all arguments are ``int`` or ``float`` only
    #. Return ``False`` if any argument is different type
    #. Do not use ``all()`` and ``any()``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz funkcję ``isnumeric``
    #. Funkcja może przyjmować dowolną liczbę argumentów pozycyjnych
    #. Podawane argumenty mogą być dowolnego typu
    #. Zwróć ``True`` jeżeli wszystkie argumenty są tylko typów ``int`` lub ``float``
    #. Zwróć ``False`` jeżeli którykolwiek jest innego typu
    #. Nie używaj ``all()`` oraz ``any()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> isnumeric()
        False
        >>> isnumeric(0)
        True
        >>> isnumeric(1)
        True
        >>> isnumeric(-1)
        True
        >>> isnumeric(1.1)
        True
        >>> isnumeric('one')
        False
        >>> isnumeric([1, 1.1])
        False
        >>> isnumeric(1, 1.1)
        True
        >>> isnumeric(1, 'one')
        False
        >>> isnumeric(1, 'one', 'two')
        False
        >>> isnumeric(True)
        False

:The whys and wherefores:
    * Defining and calling functions
    * Arbitrary number of positional arguments
    * Corner case checking
    * Function arguments checking
    * Type casting

:Hint:
    * ``isinstance(obj, (type1, type2))``
    * ``type(obj)``

Function Args/Kwargs Parameters Kwargs
--------------------------------------
* Complexity level: medium
* Lines of code to write: 8 lines + doctests
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_argskwargs_parameters_kwargs.py`

:English:
    #. Create function ``isnumeric``
    #. Function can have arbitrary number of positional **and keyword arguments**
    #. Arguments can be of any type
    #. Return ``True`` if all arguments are ``int`` or ``float`` only
    #. Return ``False`` if any argument is different type
    #. Do not use ``all()`` and ``any()``
    #. Compare using ``type()`` and ``isinstance()`` passing ``True`` as an argument
    #. Run the function without any arguments
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz funkcję ``isnumeric``
    #. Funkcja może przyjmować dowolną liczbę argumentów pozycyjnych **i nazwanych**
    #. Podawane argumenty mogą być dowolnego typu
    #. Zwróć ``True`` jeżeli wszystkie argumenty są tylko typów ``int`` lub ``float``
    #. Zwróć ``False`` jeżeli którykolwiek jest innego typu
    #. Nie używaj ``all()`` oraz ``any()``
    #. Porównaj użycie ``type()`` i ``isinstance()`` podając argument do funkcji ``True``
    #. Uruchom funkcję bez podawania argumentów
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> isnumeric()
        False
        >>> isnumeric(0)
        True
        >>> isnumeric(1)
        True
        >>> isnumeric(-1)
        True
        >>> isnumeric(1.1)
        True
        >>> isnumeric('one')
        False
        >>> isnumeric([1, 1.1])
        False
        >>> isnumeric(1, 1.1)
        True
        >>> isnumeric(1, 'one')
        False
        >>> isnumeric(1, 'one', 'two')
        False
        >>> isnumeric(True)
        False
        >>> isnumeric(a=1)
        True
        >>> isnumeric(a=1.1)
        True
        >>> isnumeric(a='one')
        False

:The whys and wherefores:
    * Defining and calling functions
    * Arbitrary number of positional arguments
    * Corner case checking
    * Function arguments checking
    * Type casting

:Hint:
    * ``isinstance(obj, (type1, type2))``
    * ``type(obj)``
