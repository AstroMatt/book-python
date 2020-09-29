******************************
Class Decorator with Functions
******************************


Rationale
======
* ``MyDecorator`` is a decorator name
* ``myfunction`` is a function name

Syntax:
    .. code-block:: python

        @MyDecorator
        def myfunction(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        myfunction = MyDecorator(myfunction)


Definition
==========
* ``cls`` is a pointer to class which is being decorated (``MyClass`` in this case)
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` can inherit from ``MyClass``
* Decorator must return pointer to ``Wrapper``

.. code-block:: python

    class Decorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)

.. code-block:: python

    @Decorator
    def echo(name):
        print(name)


    echo('Mark Watney')
    # Mark Watney


Examples
========
.. code-block:: python
    :caption: Login Check

    class User:
        def __init__(self):
            self.is_authenticated = False

        def login(self, username, password):
            self.is_authenticated = True


    class LoginCheck:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            if user.is_authenticated:
                return self._func(*args, **kwargs)
            else:
                print('Permission Denied')


    @LoginCheck
    def edit_profile():
        print('Editing profile...')


    user = User()

    edit_profile()
    # Permission Denied

    user.login('admin', 'MyVoiceIsMyPassword')

    edit_profile()
    # Editing profile...

.. code-block:: python
    :caption: Dict Cache

    class Cache(dict):
        def __init__(self, func):
            self._func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self._func(*key)
            return self[key]


    @Cache
    def myfunction(a, b):
        return a * b


    myfunction(2, 4)           # 8         # Computed
    myfunction('hi', 3)        # 'hihihi'  # Computed
    myfunction('ha', 3)        # 'hahaha'  # Computed

    myfunction('ha', 3)        # 'hahaha'  # Fetched from cache
    myfunction('hi', 3)        # 'hihihi'  # Fetched from cache
    myfunction(2, 4)           # 8         # Fetched from cache
    myfunction(4, 2)           # 8         # Computed


    myfunction
    # {
    #   (2, 4): 8,
    #   ('hi ', 3): 'hihihi',
    #   ('ha', 3): 'hahaha',
    #   (4, 2): 8,
    # }


Assignments
===========

Decorator Class Abspath
-----------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_cls_abspath.py`

:English:
    #. Create function ``print_file(filename: str) -> str`` which prints file content (filename given as an argument)
    #. Create decorator ``ToAbsolutePath``
    #. Decorator converts to absolute path (``path`` + ``filename``), if filename given as an argument is a relative path

:Polish:
    #. Stwórz funkcję ``print_file(filename: str) -> str`` która wyświetla zawartość pliku (nazwa pliku podana jako argument)
    #. Stwórz dekorator ``ToAbsolutePath``
    #. Dekorator zamienia ścieżkę na bezwzględną (``path`` + ``filename``), jeżeli nazwa pliku podana jako argument jest względna

:Hint:
    * ``from pathlib import Path``
    * ``current_directory = Path.cwd()``
    * ``path = Path(current_directory, filename)``

Decorator Class Type Check
--------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/decorator_cls_typecheck.py`

:English:
    .. todo:: English translation

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator - klasę ``CheckTypes``
    #. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
    #. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
    #. Wyjątek ma wypisywać:

        * nazwę parametru
        * typ, który parametr ma (nieprawidłowy)
        * typ, który był oczekiwany

:Input:
    .. code-block:: python

        @CheckTypes
        def isworking(a: str, b: int, c: float = 0) -> bool:
            return True

:Tests:
    .. doctest::

        >>> isworking('hello', 1)
        True

        >>> isworking('hello', b=1)
        True

        >>> isworking(a='hello', b=1)
        True

        >>> isworking(b=1, a='hello')
        True

        >>> isworking(1, 'hello')
        Traceback (most recent call last):
            ...
        TypeError: Argument 1 is <class 'int'>, but <class 'str'> was expected

        >>> isworking(1, b='hello')
        Traceback (most recent call last):
            ...
        TypeError: Argument 1 is <class 'int'>, but <class 'str'> was expected

        >>> isworking(a=1, b='hello')
        Traceback (most recent call last):
            ...
        TypeError: Argument a is <class 'str'>, but <class 'str'> was expected

        >>> isworking(b='hello', a=1)
        Traceback (most recent call last):
            ...
        TypeError: Argument b is <class 'str'>, but <class 'int'> was expected

:Hint:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'b': <class 'int'>, 'c':  <class 'float'>, 'return': <class 'bool'>}
