********
Closures
********


Rationale
=========
.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g



Nested Function
===============
* Function inside the function
* Nested functions can access the variables of the enclosing scope

.. code-block:: python

    def run():
        def hello():
            print('hello')
        return hello


    hello()
    # Traceback (most recent call last):
    #   ...
    # NameError: name 'hello' is not defined

    run()
    # <function run.<locals>.hello at 0x104e13700>

    run()()
    # hello

    result = run()
    result()
    # hello


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
        print(firstname, lastname)


    hello()
    # Mark Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        return hello


    result = run()
    result()
    # Mark Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        return hello


    result = run()
    del run
    result()
    # Mark Watney


Assignments
===========

Function Closure Define
-----------------------
* Assignment name: Function Closure Define
* Last update: 2020-10-13
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
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
    .. code-block:: text

        >>> assert callable(check)
        >>> assert callable(check(lambda x: x))
        >>> result = check(lambda x: x).__call__()
        >>> result is None
        True

Function Closure Call
---------------------
* Assignment name: Function Closure Call
* Last update: 2020-10-13
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_closure_call.py`

:English:
    #. Define function ``check`` with parameter ``func: Callable``
    #. Define closure function ``wrapper`` inside ``check``
    #. Function ``wrapper`` takes arbitrary number of positional and keyword arguments
    #. Function ``wrapper`` prints ``hello from wrapper`` on the screen
    #. Function ``check`` must return ``wrapper: Callable``
    #. Define function ``hello()`` which prints ``hello from function``
    #. Define ``result`` with result of calling ``check(hello)``
    #. Delete ``check`` using ``del`` keyword
    #. Call ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``check`` z parametrem ``func: Callable``
    #. Zdefiniuj funkcję closure ``wrapper`` wewnątrz ``check``
    #. Funkcja ``wrapper`` przyjmuje dowolną ilość argumentów pozycyjnych i nazwanych
    #. Funkcja ``wrapper`` wypisuje ``hello from wrapper``
    #. Funkcja ``check`` ma zwracać ``wrapper: Callable``
    #. Zdefiniuj funkcję ``hello()``, która wypisuje ``hello from function``
    #. Zdefiniuj zmienną ``result``, która jest wynikiem wywołania ``check(hello)``
    #. Skasuj ``check`` za pomocą słowa kluczowego ``del``
    #. Wywołaj ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isfunction
        >>> assert isfunction(hello)
        >>> assert isfunction(result)
        >>> assert not hasattr(__name__, 'check')

        >>> hello()
        hello from function

        >>> result()
        hello from wrapper

        >>> check()
        Traceback (most recent call last):
            ...
        NameError: name 'check' is not defined
