******************************
Class Decorator with Functions
******************************


Rationale
=========
* ``MyDecorator`` is a decorator name
* ``myfunction`` is a function name

Syntax:
    .. code-block:: python

        @MyDecorator
        def myfunction(*args, **kwargs):
            ...

Is equivalent to:
    .. code-block:: python

        myfunction = MyDecorator(myfunction)


Syntax
======
* ``cls`` is a pointer to class which is being decorated (``MyClass`` in this case)
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` can inherit from ``MyClass``
* Decorator must return pointer to ``Wrapper``

.. code-block:: python
    :caption: Definition

    class MyDecorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)

.. code-block:: python
    :caption: Decoration

    @MyDecorator
    def myfunction():
        ...

.. code-block:: python
    :caption: Usage

    myfunction()


Example
=======
.. code-block:: python

    class Run:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)


    @Run
    def hello(name):
        return f'My name... {name}'


    hello('José Jiménez')
    # 'My name... José Jiménez'


Use Cases
=========
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
* Assignment name: Decorator Class Abspath
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_cls_abspath.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Absolute path is when ``path`` starts with ``current_directory``
    #. Create class decorator ``Abspath``
    #. If ``path`` is relative, then ``Abspath`` will convert it to absolute
    #. If ``path`` is absolute, then ``Abspath`` will not modify it
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Ścieżka bezwzględna jest gdy ``path`` zaczyna się od ``current_directory``
    #. Stwórz klasę dekorator ``Abspath``
    #. Jeżeli ``path`` jest względne, to ``Abspath`` zamieni ją na bezwzględną
    #. Jeżeli ``path`` jest bezwzględna, to ``Abspath`` nie będzie jej modyfikował
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @Abspath
        def display(path):
            return str(path)

:Output:
    .. code-block:: text

        >>> from pathlib import Path
        >>> cwd = str(Path().cwd())
        >>> display('iris.csv').startswith(cwd)
        True
        >>> display('iris.csv').endswith('iris.csv')
        True
        >>> display('/home/python/iris.csv')
        '/home/python/iris.csv'

:Hints:
    * ``from pathlib import Path``
    * ``current_directory = Path.cwd()``
    * ``path = Path(current_directory, filename)``

Decorator Class Type Check
--------------------------
* Assignment name: Decorator Class Type Check
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/decorator_cls_typecheck.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator class ``TypeCheck``
    #. Decorator checks types of all arguments (``*args`` oraz ``**kwargs``)
    #. Decorator checks return type
    #. In case when received type is not expected throw an exception ``TypeError`` with:

        * argument name
        * actual type
        * expected type

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator klasę ``TypeCheck``
    #. Dekorator sprawdza typy wszystkich argumentów (``*args`` oraz ``**kwargs``)
    #. Dekorator sprawdza typ zwracany
    #. W przypadku gdy otrzymany typ nie jest równy oczekiwanemu wyrzuć wyjątek ``TypeError`` z:

        * nazwa argumentu
        * aktualny typ
        * oczekiwany typ

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @TypeCheck
        def echo(a: str, b: int, c: float = 0.0) -> bool:
            return bool(a * b)

:Output:
    .. code-block:: text

        >>> echo('one', 1)
        True
        >>> echo('one', 1, 1.1)
        True
        >>> echo('one', b=1)
        True
        >>> echo('one', 1, c=1.1)
        True
        >>> echo('one', b=1, c=1.1)
        True
        >>> echo(a='one', b=1, c=1.1)
        True
        >>> echo(c=1.1, b=1, a='one')
        True
        >>> echo(b=1, c=1.1, a='one')
        True
        >>> echo('one', c=1.1, b=1)
        True

        >>> echo(1, 1)
        Traceback (most recent call last):
        ...
        TypeError: "a" is <class 'int'>, but <class 'str'> was expected

        >>> echo('one', 'two')
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'str'>, but <class 'int'> was expected

        >>> echo('one', 1, 'two')
        Traceback (most recent call last):
        ...
        TypeError: "c" is <class 'str'>, but <class 'float'> was expected

        >>> echo(b='one', a='two')
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'str'>, but <class 'int'> was expected

        >>> echo('one', c=1.1, b=1.1)
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'float'>, but <class 'int'> was expected

:Hints:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'b': <class 'int'>, 'c': <class 'float'>, 'return': <class 'bool'>}
