********
Closures
********


Nested Function
===============
* Function inside the function
* nested functions can access the variables of the enclosing scope

.. code-block:: python

    def run():
        lastname = 'Watney'

        def hello():
            print(lastname)

        return hello

    hello()
    # NameError: name 'hello' is not defined

    run()
    # <function __main__.run.<locals>.hello()>

    result = run()
    result()
    # Watney


What is closure?
================
* technique by which the data is attached to some code even after end of those other original functions is called as closures
* Closures can avoid use of global variables and provides some form of data hiding
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Method of binding data to a function without actually passing them as parameters is called closure
* It is a function object obj that remembers values in enclosing scopes even if they are not present in memory
* Closures provide some sort of data hiding as they are used as callback functions
* This helps us to reduce the use of global variables
* Useful for replacing hard-coded constants
* Closures prove to be efficient way when we have few functions in our code

.. code-block:: python

    firstname = 'Mark'
    lastname = 'Watney'

    def hello():
        print(firstname)
        print(lastname)

    hello()
    # Mark
    # Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname)
            print(lastname)

        return hello


    result = run()
    result()
    # Mark
    # Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname)
            print(lastname)

        return hello


    result = run()
    del run
    result()
    # Mark
    # Watney

.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g


Assignments
===========

Function Closure Define
-----------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_closure_define.py`

:English:
    #. Define function ``check`` which takes ``func: Callable`` as an argument
    #. Define closure function ``wrapper`` inside ``check``
    #. Function ``wrapper`` takes ``*args`` and ``**kwargs`` as arguments
    #. Function ``wrapper`` returns ``None``
    #. Function ``check`` must return ``wrapper: Callable``

:Polish:
    #. Zdefiniuj funkcję ``check``, która przyjmuje ``func: Callable`` jako argument
    #. Zdefiniuj funkcję closure ``wrapper`` wewnątrz ``check``
    #. Funkcja ``wrapper`` przyjmuje ``*args`` i ``**kwargs`` jako argumenty
    #. Funckja ``wrapper`` zwraca ``None``
    #. Funkcja ``check`` ma zwracać ``wrapper: Callable``

:Output:
    .. code-block:: python

        >>> assert callable(check)
        >>> assert callable(check(lambda x: x))
        >>> result = check(lambda x: x).__call__()
        >>> result is None
        True

Function Closure Call
---------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_closure_call.py`

:English:
    #. Define function ``add(a: int, b: int) -> int``, which returns sum of ``a`` and ``b``
    #. Define function ``check`` which takes ``func: Callable`` as an argument
    #. Define closure function ``wrapper`` inside ``check``
    #. Function ``wrapper`` takes ``*args`` and ``**kwargs`` as arguments
    #. Function ``wrapper`` prints ``hello`` on the screen
    #. Function ``check`` must return ``wrapper: Callable``
    #. Call ``check`` with ``add`` as and argument and capture pointer to ``wrapper``
    #. Delete ``check`` using ``del`` keyword
    #. Call pointer
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``add(a: int, b: int) -> int``, która zwraca sumę ``a`` i ``b``
    #. Zdefiniuj funkcję ``check``, która przyjmuje ``func: Callable`` jako argument
    #. Zdefiniuj funkcję closure ``wrapper`` wewnątrz ``check``
    #. Funkcja ``wrapper`` przyjmuje ``*args`` i ``**kwargs`` jako argumenty
    #. Funckja ``wrapper`` wypisuje ``hello`` na ekranie
    #. Funkcja ``check`` ma zwracać ``wrapper: Callable``
    #. Wywołaj ``check`` z argumentem ``add`` i przechwyć wskaźnik do ``wrapper``
    #. Skasuj ``check`` za pomocą słowa kluczowego ``del``
    #. Wywołaj wskaźnik
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> add(1, 2)
        3

        >>> add(-1.1, 1.1)
        0.0

        >>> result()
        hello

        >>> check()
        Traceback (most recent call last):
            ...
        NameError: name 'check' is not defined
