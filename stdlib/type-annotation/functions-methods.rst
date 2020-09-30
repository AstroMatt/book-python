*********************
Functions and Methods
*********************


Simple
======
.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b


    add(1, 2.5)


The NoReturn type
=================
.. code-block:: python

    from typing import NoReturn


    def stop() -> NoReturn:
        raise RuntimeError


Iterator
========
.. code-block:: python

    from typing import Iterator


    def fib(n: int) -> Iterator[int]:
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b


Callable
========
.. code-block:: python

    from typing import Callable

    def feeder(get_next_item: Callable[[], str]) -> None:
        pass

    def async_query(on_success: Callable[[int], None],
                    on_error: Callable[[int, Exception], None]) -> None:
        pass



Overload
========
.. versionadded:: Python 3.8
    See :pep:`589`

* The ``@overload`` decorator allows describing functions and methods that support multiple different combinations of argument types.
* A series of @overload-decorated definitions must be followed by exactly one non-@overload-decorated definition (for the same function/method)
* The @overload-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-@overload-decorated definition

.. code-block:: python

    @overload
    def process(response: None) -> None:
        ...

    @overload
    def process(response: int) -> tuple[int, str]:
        ...

    @overload
    def process(response: bytes) -> str:
        ...

    def process(response):
        <actual implementation>


Final
=====
.. versionadded:: Python 3.8
    See :pep:`589`

.. code-block:: python

    from typing import final

    class Base:
        @final
        def foo(self) -> None:
            ...

    class Derived(Base):
        def foo(self) -> None:  # Error: Cannot override final attribute "foo"
                                # (previously declared in base class "Base")
            ...
