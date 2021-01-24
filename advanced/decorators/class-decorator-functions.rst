******************************
Class Decorator with Functions
******************************


Syntax
======
* ``decorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:
    .. code-block:: python

        @Decorator
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = Decorator(my_function)


Definition
==========
.. code-block:: python

    class Decorator:
        def __init__(self, function):
            self._function = function

        def __call__(self, *args, **kwargs):
            return self._function(*args, **kwargs)


Usage
=====
.. code-block:: python

    class Decorator:
        def __init__(self, function):
            self._function = function

        def __call__(self, *args, **kwargs):
            return self._function(*args, **kwargs)


    @Decorator
    def echo(name):
        print(name)


    echo('Mark Watney')
    # Mark Watney


Examples
========

Login Check
-----------
.. code-block:: python

    class User:
        def __init__(self):
            self.is_authenticated = False

        def login(self, username, password):
            self.is_authenticated = True


    class LoginCheck:
        def __init__(self, function):
            self._function = function

        def __call__(self, *args, **kwargs):
            if user.is_authenticated:
                return self._function(*args, **kwargs)
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

Dict Cache
----------
.. code-block:: python

    class Cache(dict):
        def __init__(self, function):
            self._function = function

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self._function(*key)
            return self[key]


    @Cache
    def my_function(a, b):
        return a * b


    my_function(2, 4)           # 8         # Computed
    my_function('hi', 3)        # 'hihihi'  # Computed
    my_function('ha', 3)        # 'hahaha'  # Computed

    my_function('ha', 3)        # 'hahaha'  # Fetched from cache
    my_function('hi', 3)        # 'hihihi'  # Fetched from cache
    my_function(2, 4)           # 8         # Fetched from cache
    my_function(4, 2)           # 8         # Computed


    my_function
    # {
    #   (2, 4): 8,
    #   ('hi ', 3): 'hihihi',
    #   ('ha', 3): 'hahaha',
    #   (4, 2): 8,
    # }


Assignments
===========

Simple decorator
----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/decorator_abspath.py`

:English:
    .. todo:: English translation

:Polish:
    #. Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``
    #. Wypisz nazwę pliku lub katalogu
    #. Stwórz dekorator do funkcji, który przed wypisaniem podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

