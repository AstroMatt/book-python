************
Type Aliases
************


Type Aliases
============
.. code-block:: python

    from typing import List, Tuple


    GeographicCoordinate = Tuple[float, float]

    locations: List[GeographicCoordinate] = [
        (25.91375, -60.15503),
        (-11.01983, -166.48477),
        (-11.01983, -166.48477)
    ]

.. code-block:: python

    from typing import Union


    AllowedTypes = Union[list, set, tuple]

    def my_print(args: AllowedTypes) -> None:
        if not isinstance(args, AllowedTypes.__args__):
            raise TypeError(f'Collection must be instance of {AllowedTypes.__args__}')

        for element in collection:
            print(element)


Type Vars
=========
.. code-block:: python

    from typing import TypeVar, Iterable, Tuple

    T = TypeVar('T', int, float, complex)
    Vector = Iterable[Tuple[T, T]]

    def inproduct(v: Vector[T]) -> T:
        return sum(x*y for x, y in v)

    def dilate(v: Vector[T], scale: T) -> Vector[T]:
        return ((x * scale, y * scale) for x, y in v)

    vec = []  # type: Vector[float]
