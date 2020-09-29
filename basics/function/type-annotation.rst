.. _Function Type Annotation:

************************
Function Type Annotation
************************


Rationale
=========
.. highlights::
    * Since Python 3.5
    * Types are not forced
    * Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
    * Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów


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

    def add_numbers(a: Union[int,float],
                    b: Union[int,float]
                    ) -> Union[int,float]:
        return a + b

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
        start_position = text.find(what)

        if start_position > 0:
            return start_position
        else:
            return None


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


    valid_email('jose.jimenez@nasa.gov')
    # 'jose.jimenez@nasa.gov'

    valid_email('jose.jimenez_at_nasa.gov')
    # Traceback (most recent call last):
    #   ...
    # ValueError: Invalid Email


Literal
=======
.. versionadded:: Python 3.8
    See :pep:`586`

.. code-block:: python

    from typing import Literal


    def allow_access(who: Literal['Cosmonaut', 'Astronaut']) -> None:
        pass


    allow_access('Astronaut')   # OK
    allow_access('Pilot')       # Error

.. code-block:: python

    from typing import Literal


    def open(filename: str, mode: Literal['r','w','a']) -> None:
        pass


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
    * Your IDE and ``mypy`` will yield errors

.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b


    add_numbers('Jan', 'Twardowski')
    # 'JanTwardowski'


More Information
================
.. note:: More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
