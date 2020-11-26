.. _Advanced Annotation Function:

*******************
Annotation Function
*******************


Rationale
=========
.. highlights::
    * Python 3.9 introduced :pep:`585` -- Type Hinting Generics In Standard Collections
    * Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``


Return
======
.. code-block:: python

    def say_hello() -> str:
        return 'My name... José Jiménez'


Parameters
==========
.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers(1, 2)
    # 3


Union
=====
.. code-block:: python

    from typing import Union


    def add_numbers(a: Union[int, float], b: Union[int, float]) -> int:
        return int(a + b)


    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'

.. code-block:: python

    from typing import Union

    Number = Union[int, float]

    def add_numbers(a: Number, b: Number) -> Number:
        return a + b

    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'


Optional
========
.. code-block:: python

    def find(text: str, what: str) -> Optional[int]:
        position = text.find(what)

        if position == -1:
            return None
        else:
            return position


    find('Python', 'o')      # 4
    find('Python', 'x')      # None


NoReturn
========
.. code-block:: python

    from typing import NoReturn


    def stop() -> NoReturn:
        raise RuntimeError

.. code-block:: python

    from typing import Union, NoReturn


    def valid_email(email: str) -> Union[NoReturn, str]:
        if '@' in email:
            return email
        else:
            raise ValueError('Invalid Email')


    valid_email('mark.watney@nasa.gov')
    # 'mark.watney@nasa.gov'

    valid_email('mark.watney_at_nasa.gov')
    # Traceback (most recent call last):
    # ValueError: Invalid Email


Literal
=======
.. versionadded:: Python 3.8
    See :pep:`586`

.. code-block:: python

    from typing import Literal


    def open(filename: str, mode: Literal['r','w','a']) -> None:
        pass

    open('data.csv', mode='w')  # Ok
    open('data.csv', mode='r')  # Ok
    open('data.csv', mode='a')  # Ok
    open('data.csv', mode='x')  # Error


Annotations
===========
.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers.__annotations__
    # {'a': <class 'int'>,
    #  'b': <class 'int'>,
    #  'return': <class 'int'>}


Errors
======
.. highlights::
    * Python will execute without even warning
    * Your IDE and ``mypy`` et. al. will yield errors

.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b


    add_numbers('Jan', 'Twardowski')
    # 'JanTwardowski'


Good Engineering Practices
==========================
.. code-block:: python

    from typing import Union

    def add_numbers(a: Union[int,float],
                    b: Union[int,float]
                    ) -> Union[int,float]:
        return a + b

    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'


More Information
================
* Example: https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py#L458

.. note:: More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
