*******
Special
*******


Optional
========
.. code-block:: python

    from typing import Optional


    def non_zero(number: int) -> Optional[int]:
        if not number:
            return None
        else:
            return number


Union
=====
.. code-block:: python

    from typing import Union


    def round(number: Union[int, float]) -> int:
        return int(number)

.. code-block:: python

    from typing import Union, Sequence


    def fire_employees(e: Union[Employee, Sequence[Employee]]) -> None:
        print(employee)


Any
===
.. code-block:: python

    from typing import Any


    def echo(value: Any) -> None:
        print(value)


Literal
=======
.. versionadded:: Python 3.8
    :pep:`586` -- Literal Types

.. code-block:: python

    from typing import Literal

    def accepts_only_four(x: Literal[4]) -> None:
        pass

    accepts_only_four(4)   # OK
    accepts_only_four(19)  # Rejected


.. code-block:: python

    from typing import Literal, overload


    @overload
    def open(path: str,
             mode: Literal["r", "w", "a", "x", "r+", "w+", "a+", "x+"],
             ) -> IO[str]: ...

    @overload
    def open(path: str,
             mode: Literal["rb", "wb", "ab", "xb", "r+b", "w+b", "a+b", "x+b"],
             ) -> IO[bytes]: ...

