********
Callable
********


Rationale
=========
.. code-block:: python

    def hello():
        return 'My name... José Jiménez'


    callable(hello)
    # True

    type(hello)           # <class 'function'>
    hello                 # <function hello at 0x0C55D420>

    type(hello())         # <class 'str'>
    hello()               # My name... José Jiménez


Function Attributes
===================
.. code-block:: python

    def hello():
        print('My name... José Jiménez')


    hello.myvar = 10
    print(hello.myvar)
    # 10

.. code-block:: python

    def hello():
        if not hello.disabled:
            print('My name... José Jiménez')
        else:
            raise PermissionError


    hello.disabled = False
    hello()
    # My name... José Jiménez

    hello.disabled = True
    hello()
    # Traceback (most recent call last):
    # PermissionError

.. code-block:: python

    def add(a, b):
        return a + b


    add.__code__.co_varnames
    # ('a', 'b')

    dir(add.__code__)
    # [...,
    #  'co_argcount',
    #  'co_cellvars',
    #  'co_code',
    #  'co_consts',
    #  'co_filename',
    #  'co_firstlineno',
    #  'co_flags',
    #  'co_freevars',
    #  'co_kwonlyargcount',
    #  'co_lnotab',
    #  'co_name',
    #  'co_names',
    #  'co_nlocals',
    #  'co_posonlyargcount',
    #  'co_stacksize',
    #  'co_varnames',
    #  'replace']

.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b


    add.__annotations__
    # {'a': int, 'b': int, 'return': int}


Calling Call Method
===================
* ``__call__()`` method makes object callable

.. code-block:: python

    def hello():
        print('My name... José Jiménez')


    type(hello)
    # <class 'function'>

    callable(hello)
    # True

    hello()
    # My name... José Jiménez

    hello.__call__()
    # My name... José Jiménez


Overloading Call Method
=======================
.. code-block:: python

    astro = str('Mark Watney')

    astro()
    # Traceback (most recent call last):
    # TypeError: 'str' object is not callable

    callable(astro)
    # False

    type(astro)
    # <class 'str'>

.. code-block:: python

    class str(str):
        def __call__(self):
            print('hello')


    astro = str('Mark Watney')

    astro()
    # hello

    callable(astro)
    # True

    type(astro)
    # <class '__main__.str'>


Callbacks
=========
.. code-block:: python
    :caption: Callback Design Pattern

    from http import HTTPStatus
    import requests


    def http_request(url, on_success=lambda *args: None, on_error=lambda *args: None):
        result = requests.get(url)
        if result.status_code == HTTPStatus.OK:
            return on_success(result)
        else:
            return on_error(result)


    http_request(
        url='http://python.astrotech.io/',
        on_success=lambda result: print(result),
        on_error=lambda error: print(error))

    # <Response [200]>


Type Annotation
===============
.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b


    total: Callable = add
    total: Callable[[int, int], int] = add

.. code-block:: python

    from typing import Callable


    def lower() -> str:
        return 'hello'


    def higher() -> Callable:
        return lower

.. code-block:: python

    from typing import Callable


    def http_request(url: str,
                     on_success: Callable = lambda *args: None,
                     on_error: Callable = lambda *args: None) -> None:
        ...

.. code-block:: python

    from typing import Callable, Iterator, Iterable


    def zip(a: Iterable, b: Iterable) -> Iterator:
        ...

    def enumerate(data: Iterable) -> Iterator[int, Any]:
        ...

    def map(func: Callable, data: Iterable) -> Iterator:
        ...

    def filter(func: Callable, data: Iterable) -> Iterator:
        ...


Case Studies
============
.. code-block:: python

    import datetime


    now = datetime.datetime.now

    print(now)
    # <built-in method now of type object at 0x107695638>

    print(now())
    # 1969-07-21 02:56:25

    now()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

    now.__call__()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

.. code-block:: python

    import datetime
    from time import sleep


    now = datetime.datetime.now

    print(now())          # 1969-07-21 02:56:15
    sleep(10)
    print(now())          # 1969-07-21 02:56:25


Assignments
===========

.. literalinclude:: solution/function_callable_define.py
    :caption: :download:`Solution <solution/function_callable_define.py>`
    :end-before: # Solution
