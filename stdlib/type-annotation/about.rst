.. _Type Annotations:

****************
Type Annotations
****************


Rationale
=========
.. versionadded:: Python 3.5
    See :pep:`484`

* Also known as Type Hinting
* Accessed by ``__annotations__`` attribute
* No type checking happens at runtime
* Use separate off-line type checker which users can run over their source code voluntarily
* Supports unions, generic types, and a special type named
* ``Any`` is consistent with (i.e. assignable to and from) all types
* This latter feature is taken from the idea of gradual typing.
* Gradual typing and the full type system are explained in :pep:`483`
* https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

.. warning:: It should also be emphasized that Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.


Glossary
========
.. glossary::

    Generic
        A type that can be parameterized, typically a container.
        Also known as a parametric type or a generic type.
        For example: ``dict``.

    Parameterized Generic
        A specific instance of a generic with the expected types for container elements provided.
        Also known as a parameterized type.
        For example: ``dict[str, int]``.


Data types
==========
.. code-block:: python

    name: str = 'Jan Twardowski'
    leet: int = 1337
    pi: float = 3.14



Final
=====
.. versionadded:: Python 3.8
    See :pep:`591`

.. code-block:: python

    from typing import final

    @final
    class Base:
        ...

    class Derived(Base):  # Error: Cannot inherit from final class "Base"
        ...

.. code-block:: python

    from typing import Final


    ID: Final = 1
    ID: Final[float] = 1

.. code-block:: python

    from typing import Final

    class Window:
        BORDER_WIDTH: Final = 2.5

    class ListView(Window):
        BORDER_WIDTH = 3  # Error: can't override a final attribute

.. code-block:: python

    from typing import Final

    class ImmutablePoint:
        x: Final[int]
        y: Final[int]  # Error: final attribute without an initializer

        def __init__(self) -> None:
            self.x = 1  # Good

.. code-block:: python

    from typing import Final

    RATE: Final = 3000

    class Base:
        DEFAULT_ID: Final = 0

    RATE = 300  # Error: can't assign to final attribute
    Base.DEFAULT_ID = 1  # Error: can't override a final attribute


New Features
============
.. versionadded:: Python 3.9
    :pep:`585` Builtin Generic Types

* In type annotations you can now use built-in collection types such as list and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing.
* Some other types in the standard library are also now generic, for example ``queue.Queue``.
* Importing those from typing is deprecated.
* Due to :pep`563` and the intention to minimize the runtime impact of typing, this deprecation will not generate ``DeprecationWarnings``.
* Instead, type checkers may warn about such deprecated usage when the target version of the checked program is signalled to be Python 3.9 or newer.
* The deprecated functionality will be removed from the typing module in the first Python version released 5 years after the release of Python 3.9.0.


.. code-block:: python

    def greet_all(names: list[str]) -> None:
        for name in names:
            print("Hello", name)

.. code-block:: python
    :caption: You can try this feature since Python 3.7 with ``from __future__ import annotations``

    from __future__ import annotations

    def find(haystack: dict[str, list[int]]) -> int:
        ...


* ``tuple`` instead of ``typing.Tuple``
* ``list`` instead of ``typing.List``
* ``dict`` instead of ``typing.Dict``
* ``set`` instead of ``typing.Set``
* ``frozenset`` instead of ``typing.FrozenSet``
* ``type`` instead of ``typing.Type``
* ``collections.deque``
* ``collections.defaultdict``
* ``collections.OrderedDict``
* ``collections.Counter``
* ``collections.ChainMap``
* ``collections.abc.Awaitable``
* ``collections.abc.Coroutine``
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``
* ``collections.abc.Iterable``
* ``collections.abc.Iterator``
* ``collections.abc.Generator``
* ``collections.abc.Reversible``
* ``collections.abc.Container``
* ``collections.abc.Collection``
* ``collections.abc.Callable``
* ``collections.abc.Set`` instead of ``typing.AbstractSet``
* ``collections.abc.MutableSet``
* ``collections.abc.Mapping``
* ``collections.abc.MutableMapping``
* ``collections.abc.Sequence``
* ``collections.abc.MutableSequence``
* ``collections.abc.ByteString``
* ``collections.abc.MappingView``
* ``collections.abc.KeysView``
* ``collections.abc.ItemsView``
* ``collections.abc.ValuesView``
* ``contextlib.AbstractContextManager``  instead of ``typing.ContextManager``
* ``contextlib.AbstractAsyncContextManager``  instead of ``typing.AsyncContextManager``
* ``re.Pattern``  instead of ``typing.Pattern``, ``typing.re.Pattern``
* ``re.Match``  instead of ``typing.Match``, ``typing.re.Match``

.. code-block:: python

    l = list[str]()
    # []

    list is list[str]
    # False

    list == list[str]
    # False

    list[str] == list[str]
    # True

    list[str] == list[int]
    # False

    isinstance([1, 2, 3], list[str])
    # Traceback (most recent call last):
    #     ...
    # TypeError: isinstance() arg 2 cannot be a parameterized generic

    issubclass(list, list[str])
    # Traceback (most recent call last):
    #     ...
    # TypeError: issubclass() arg 2 cannot be a parameterized generic

    isinstance(list[str], types.GenericAlias)
    # True
