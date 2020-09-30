********
Callable
********


Rationale
=========
.. code-block:: python

    def hello():
        print('Hello')

    type(hello)
    # <class 'function'>

    callable(hello)
    # True


First-class Function
====================
* If a function can be assigned to a variable or passed as object/variable to other function.
* Can be used as parameters
* Can be used as a return value
* Can be assigned to variables
* Can be stored in data structures such as hash tables, lists, ...

.. code-block:: python

    def lower():
        return 'My name... José Jiménez'

    def higher():
        return lower


    result = higher()     # <function __main__.lower()>
    result()              # 'My name... José Jiménez'


Aliases
=======
.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now()

    print(now)            # 1969-07-21 02:56:15
    time.sleep(10)
    print(now)            # 1969-07-21 02:56:15

.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now

    print(now())          # 1969-07-21 02:56:15
    time.sleep(10)
    print(now())          # 1969-07-21 02:56:25


.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now

    print(now())
    # 1969-07-21 02:56:25

    print(now)
    # <built-in method now of type object at 0x107695638>

    now()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

    now.__call__()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)


Callable
========
* ``__call__()`` method makes object callable

.. code-block:: python

    def hello():
        print('Hello')

    type(hello)
    # <class 'function'>

    callable(hello)
    # True

    hello()
    # Hello

    hello.__call__()
    # Hello

.. code-block:: python

    def hello():
        return 'My name... José Jiménez'


    type(hello())         # <class 'str'>
    hello()               # My name... José Jiménez

    type(hello)           # <class 'function'>
    hello                 # <function hello at 0x0C55D420>

.. code-block:: python

    astro = str('Mark Watney')

    type(astro)
    # <class 'str'>

    astro()
    # TypeError: 'str' object is not callable

.. code-block:: python

    class str(str):
        def __call__(self):
            print('hello')


    astro = str('Mark Watney')

    type(astro)
    # <class '__main__.str'>

    astro()
    # hello


Callbacks
=========
.. code-block:: python
    :caption: Callback Design Pattern

    from http import HTTPStatus
    import requests


    def noop(*arg, **kwargs):
        pass


    def http_request(url, on_success=noop, on_error=noop:
        result = requests.get(url)
        if result.status_code == HTTPStatus.OK:
            return on_success(result)
        else:
            return on_error(result)


    def success(result):
        print('Success')


    def error(result):
        print('Error')


    http_request(
        url='http://python.astrotech.io',
        on_success=success,
        on_error=error)


Type Annotation
===============
.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b

    total: Callable = add
    total: Callable[[int, int], int] = add

.. code-block:: python

    from typing import Callable, Iterator, Iterable


    def map(func: Callable, data: Iterable) -> Iterator:
        ...

    def filter(func: Callable, data: Iterable) -> Iterator:
        ...

    def zip(a: Iterable, b: Iterable) -> Iterator:
        ...

    def enumerate(data: Iterable) -> Iterator[int, Any]:
        ...

.. code-block:: python

    from typing import Callable

    def http_request(url: str,
                     on_success: Callable = noop,
                     on_error: Callable = noop) -> None:
        pass

.. code-block:: python

    from typing import Callable


    def lower() -> str:
        return 'My name... José Jiménez'

    def higher() -> Callable:
        return lower


    result = higher()     # <function __main__.lower()>
    result()              # 'My name... José Jiménez'


Assignments
===========

Function First Class Define
---------------------------
* Assignment name: Function First Class Define
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_firstclass_define.py`
* Last update: 2020-10-01

:English:
    #. Define function ``wrapper``
    #. ``wrapper`` takes ``*args`` and ``**kwargs`` as arguments
    #. ``wrapper`` returns ``None``
    #. Define function ``check`` which takes ``func: Callable`` as an argument
    #. Function ``check`` must return ``wrapper: Callable``

:Polish:
    #. Zdefiniuj funkcję ``wrapper``
    #. ``wrapper`` przyjmuje ``*args`` i ``**kwargs`` jako argumenty
    #. ``wrapper`` zwraca ``None``
    #. Zdefiniuj funkcję ``check``, która przyjmuje ``func: Callable`` jako argument
    #. Funkcja ``check`` ma zwracać ``wrapper: Callable``

.. code-block:: text

    >>> assert callable(check)
    >>> assert callable(check(lambda x: x))
    >>> result = check(lambda x: x).__call__()
    >>> result is None
    True
