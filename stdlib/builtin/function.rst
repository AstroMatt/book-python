.. _Builtin Functions:

*****************
Builtin Functions
*****************


``range()``
===========
* Tworzy **iterator**, który zwraca liczby w sekwencji.

.. code-block:: python

    for liczba in range(0, 5):
        print(liczba)
    # 0
    # 1
    # 2
    # 3
    # 4

    for liczba in range(0, 5, 2):
        print(liczba)
    # 0
    # 2
    # 4

.. code-block:: python

    numbers_generator = range(0, 5)

    print(numbers_generator)
    # range(0, 5)

.. code-block:: python

    numbers_generator = range(0, 5)
    numbers = list(numbers_generator)

    print(numbers)
    # [0, 1, 2, 3, 4]


Sprawdzanie typów
=================

``type()``
----------
.. code-block:: python

    type(1)                 # <class 'int'>
    type(1.2)               # <class 'float'>
    type('hello')           # <class 'str'>

    type(True)              # <class 'bool'>
    type(False)             # <class 'bool'>
    type(None)              # <class 'NoneType'>

    type([1, 2])            # <class 'list'>
    type((1, 2))            # <class 'tuple'>
    type({1, 2})            # <class 'set'>
    type({1: 2})            # <class 'dict'>

.. code-block:: python

    type(1) == int          # True
    type(1.2) == float      # True

    type(True) == bool      # True
    type(False) == bool     # True

    type(True) == int       # False
    type(False) == int      # False

    type(None) == int       # False
    type(None) == bool      # False
    type(None) == None      # False

``isinstance()``
----------------
* Sprawdza czy dany obiekt jest instancją danej klasy
* Jeżeli jest więcej niż jeden typ to musi być ``tuple`` a nie ``list`` lub ``set``

.. code-block:: python

    isinstance(10, int)             # True
    isinstance(10, float)           # False
    isinstance(10, (int, float))    # True

.. code-block:: python

    isinstance(True, float)         # False
    isinstance(True, int)           # True
    isinstance(True, bool)          # True

    isinstance(False, float)        # False
    isinstance(False, int)          # True
    isinstance(False, bool)         # True

    isinstance(None, int)           # False
    isinstance(None, bool)          # False
    isinstance(None, float)         # False

``issubclass()``
----------------


Działania na kolekcjach
=======================

``any()``
---------
.. code-block:: python

    DATA = [1, 2, 'three', 4]

    if any(isinstance(x, str) for x in DATA):
        print(True)
    else:
        print(False)

    # True

``all()``
---------
.. code-block:: python

    DATA = [1, 2, 'three', 4]

    if all(isinstance(x, int) for x in DATA):
        print(True)
    else:
        print(False)

    # False

``sum()``
---------
.. code-block:: python

    sum(x for x in range(0, 100))
    # 4950

``len()``
---------
.. code-block:: python

    DATA = [1, 2, 3]

    len(DATA)
    # 3

``slice()``
-----------
.. highlights::
    * ``slice()`` arguments must be ``int`` (positive, negative or zero)
    * start (inclusive), default: 0
    * stop (exclusive), default: len(...)
    * step, default: 1

.. code-block:: python

    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    get = slice(1)

    data[get]
    # ['a']

.. code-block:: python

    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    get = slice(2, 7)

    data[get]
    # ['c', 'd', 'e', 'f', 'g']

.. code-block:: python

    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    get = slice(2, 7, 2)

    data[get]
    # ['c', 'e', 'g']

.. code-block:: python

    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    get = slice(1)
    data[get]
    # [0]

    get = slice(2, 7)
    data[get]
    # [2, 3, 4, 5, 6]

    get = slice(2, 7, 2)
    data[get]
    # [2, 4, 6]

.. code-block:: python

    text = 'We choose to go to the Moon!'
    get = slice(23, 28)

    text[get]
    # 'Moon!'


Konwersje typów
===============

``bin()``
---------
* Konwertuje liczbę na binarną
* Nie stosuje kodu uzupełnień do dwóch

.. code-block:: python

    0b101111    # 47

.. code-block:: python

    bin(3)      # '0b11'
    bin(-3)     # '-0b11'

``hex()``
---------
* Konwertuje liczbę na heksadecymalną
* Konwersja kolorów w HTML
* Shellcode

.. code-block:: python

    hex(99)  # '0x63'

``oct()``
---------
* Konwertuje liczbę na oktalną
* Przydatne do uprawnień w systemie operacyjnym

.. code-block:: python

    oct(33261)  # '0o100755'

``ord()``
---------
Zwraca kod ASCII jedno-znakowego stringa.

.. code-block:: python

    ord('a')  # 97

``chr()``
---------
Z pozycji w tablicy ASCII konwertuje kod na znak Unicode.

.. code-block:: python

    chr(97)  # 'a'

``eval()``
----------
.. code-block:: python

    eval('name="José Jiménez"; print(name)')
    # José Jiménez


Other builtin functions
=======================
.. csv-table:: Most used Built-in functions
    :widths: 20, 80
    :header: "Name", "Description"

    "``abs()``", "Return the absolute value of the argument."
    "``all()``", "Return True if bool(x) is True for all values x in the iterable."
    "``any()``", "Return True if bool(x) is True for any x in the iterable."
    "``ascii()``", "Return an ASCII-only representation of an object."
    "``bin()``", "Return the binary representation of an integer."
    "``bool()``", "bool(x) -> bool"
    "``bytearray()``", "bytearray(iterable_of_ints) -> bytearray"
    "``bytes()``", "bytes(iterable_of_ints) -> bytes"
    "``callable()``", "Return whether the object is callable (i.e., some kind of function)."
    "``chr()``", "Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff."
    "``classmethod()``", "classmethod(function) -> method"
    "``compile()``", "Compile source into a code object that can be executed by exec() or eval()."
    "``complex()``", "Create a complex number from a real part and an optional imaginary part."
    "``delattr()``", "Deletes the named attribute from the given object."
    "``dict()``", "dict() -> new empty dictionary"
    "``dir()``", "dir([object]) -> list of strings"
    "``divmod()``", "Return the tuple (x//y, x%y).  Invariant: div*y + mod == x."
    "``enumerate()``", "Return an enumerate object."
    "``eval()``", "Evaluate the given source in the context of globals and locals."
    "``exec()``", "Execute the given source in the context of globals and locals."
    "``filter()``", "filter(function or None, iterable) --> filter object"
    "``float()``", "Convert a string or number to a floating point number, if possible."
    "``format()``", "Return value.__format__(format_spec)"
    "``frozenset()``", "frozenset() -> empty frozenset object"
    "``getattr()``", "getattr(object, name[, default]) -> value"
    "``globals()``", "Return the dictionary containing the current scope's global variables."
    "``hasattr()``", "Return whether the object has an attribute with the given name."
    "``hash()``", "Return the hash value for the given object."
    "``help()``", "Define the builtin 'help'."
    "``hex()``", "Return the hexadecimal representation of an integer."
    "``id()``", "Return the identity of an object."
    "``input()``", "Read a string from standard input.  The trailing newline is stripped."
    "``int()``", "int([x]) -> integer"
    "``isinstance()``", "Return whether an object is an instance of a class or of a subclass thereof."
    "``issubclass()``", "Return whether 'cls' is a derived from another class or is the same class."
    "``iter()``", "iter(iterable) -> iterator"
    "``len()``", "Return the number of items in a container."
    "``list()``", "Built-in mutable sequence."
    "``locals()``", "Return a dictionary containing the current scope's local variables."
    "``map()``", "map(func, \*iterables) --> map object"
    "``max()``", "max(iterable, \*[, default=obj, key=func]) -> value"
    "``memoryview()``", "Create a new memoryview object which references the given object."
    "``min()``", "min(iterable, \*[, default=obj, key=func]) -> value"
    "``next()``", "next(iterator[, default])"
    "``object()``", "The most base type"
    "``oct()``", "Return the octal representation of an integer."
    "``open()``", "Open file and return a stream.  Raise OSError upon failure."
    "``ord()``", "Return the Unicode code point for a one-character string."
    "``pow()``", "Equivalent to x\*\*y (with two arguments) or x\*\*y % z (with three arguments)"
    "``print()``", "print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)"
    "``property()``", "Property attribute."
    "``range()``", "range(stop) -> range object"
    "``repr()``", "Return the canonical string representation of the object."
    "``reversed()``", "Return a reverse iterator over the values of the given sequence."
    "``round()``", "Round a number to a given precision in decimal digits."
    "``set()``", "set() -> new empty set object"
    "``setattr()``", "Sets the named attribute on the given object to the specified value."
    "``slice()``", "slice(stop)"
    "``sorted()``", "Return a new list containing all items from the iterable in ascending order."
    "``staticmethod()``", "staticmethod(function) -> method"
    "``str()``", "str(object='') -> str"
    "``sum()``", "Return the sum of a 'start' value (default: 0) plus an iterable of numbers"
    "``super()``", "super() -> same as super(__class__, <first argument>)"
    "``tuple()``", "Built-in immutable sequence."
    "``type()``", "type(object_or_name, bases, dict)"
    "``vars()``", "vars([object]) -> dictionary"
    "``zip()``", "zip(iter1 [,iter2 [...]]) --> zip object"



Assignments
===========

Average
-------
* Assignment: Average
* Filename: :download:`assignments/builtin_average.py`
* Complexity: easy
* Lines of code: 12 lines
* Time: 13 min

English:
    #. Use data from "Given" section (see below)
    #. Separate header and data
    #. Define dict ``result: dict[str, list]``, keys are column names from header
    #. For each row in data, add values to proper lists in ``result``
    #. Define function ``mean()``, calculating mean for arbitrary number of arguments
    #. Return ``None`` if any argument to the function is not ``float`` or ``int``
    #. To calculate mean use built-in functions
    #. Iterating over ``result`` print column name and calculated average
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Zdefiniuj słownik ``result: dict[str, list]``, klucze to nazwy kolumn z nagłówka
    #. Dla każdego wiersza w danych, dodawaj wartości do odpowiednich list w ``result``
    #. Zdefiniuj funkcję ``mean()``, liczącą średnią dla dowolnej ilości argumentów
    #. Zwróć ``None`` jeżeli którykolwiek z argumentów do funkcji nie jest ``float`` lub ``int``
    #. Do wyliczenia średniej wykorzystaj wbudowane funkcje
    #. Iterując po ``result`` wypisz nazwę kolumny oraz wyliczoną średnią
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa'),
                (7.0, 3.2, 4.7, 1.4, 'versicolor'),
                (7.6, 3.0, 6.6, 2.1, 'virginica'),
                (4.9, 3.0, 1.4, 0.2, 'setosa'),
                (4.9, 2.5, 4.5, 1.7, 'virginica'),
                (7.1, 3.0, 5.9, 2.1, 'virginica'),
                (4.6, 3.4, 1.4, 0.3, 'setosa'),
                (5.4, 3.9, 1.7, 0.4, 'setosa'),
                (5.7, 2.8, 4.5, 1.3, 'versicolor'),
                (5.0, 3.6, 1.4, 0.3, 'setosa'),
                (5.5, 2.3, 4.0, 1.3, 'versicolor'),
                (6.5, 3.0, 5.8, 2.2, 'virginica'),
                (6.5, 2.8, 4.6, 1.5, 'versicolor'),
                (6.3, 3.3, 6.0, 2.5, 'virginica'),
                (6.9, 3.1, 4.9, 1.5, 'versicolor'),
                (4.6, 3.1, 1.5, 0.2, 'setosa')]

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': [5.8, 5.1, ...],
     'Sepal width': [2.7, 3.5, ...],
     'Petal length': [5.1, 1.4, ...],
     'Petal width': [1.9, 0.2, ...],
     'Species': ['virginica', 'setosa',
     ...],}

