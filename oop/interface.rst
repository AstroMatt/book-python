.. _OOP Interface:

*********
Interface
*********


Rationale
=========
* Python don't have interfaces
* Cannot instantiate
* Inheriting class must implement all methods
* Only method declaration
* :pep:`544` Protocols: Structural subtyping (static duck typing)

.. glossary::

    interface
        Software entity with public methods and attribute declaration

    implement
        Class implements interface if has all public fields and methods from interface


Example
=======
.. code-block:: python
    :caption: Interfaces

    from datetime import timedelta


    class CacheInterface:
        timeout: timedelta

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


Use Cases
=========
.. code-block:: python
    :caption: Interfaces

    from datetime import timedelta


    class Cache:
        timeout: timedelta

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    class CacheDatabase(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheRAM(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheFilesystem(Cache):
        timeout: timedelta

        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    fs: Cache = CacheFilesystem()
    fs.set('name', 'Jan Twardowski')
    fs.is_valid('name')
    fs.get('name')

    ram: Cache = CacheRAM()
    ram.set('name', 'Jan Twardowski')
    ram.is_valid('name')
    ram.get('name')

    db: Cache = CacheDatabase()
    db.set('name', 'Jan Twardowski')
    db.is_valid('name')
    db.get('name')


Assignments
===========

OOP Interface Define
--------------------
* Assignment: OOP Interface Define
* Last update: 2020-10-14
* Complexity: easy
* Lines of code: 13 lines
* Estimated time: 13 min
* Filename: :download:`assignments/oop_interface_define.py`

English:
    #. Define interface ``IrisInterface``
    #. Attributes: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Methods: ``sum()``, ``len()``, ``mean()`` in ``IrisInterface``
    #. All methods and constructor must raise exception ``NotImplementedError``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Zdefiniuj interfejs ``IrisInterface``
    #. Attributes: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Metody: ``sum()``, ``len()``, ``mean()`` w ``IrisInterface``
    #. Wszystkie metody oraz konstruktor muszą podnosić wyjątek ``NotImplementedError``

Tests:
    >>> assert hasattr(IrisInterface, 'mean')
    >>> assert hasattr(IrisInterface, 'sum')
    >>> assert hasattr(IrisInterface, 'len')

    >>> IrisInterface.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
    Traceback (most recent call last):
    NotImplementedError

OOP Interface Implement
-----------------------
* Assignment: OOP Interface Implement
* Last update: 2020-10-14
* Complexity: easy
* Lines of code: 12 lines
* Estimated time: 13 min
* Filename: :download:`assignments/oop_interface_implement.py`

English:
    #. Use data from "Given" section (see below)
    #. Define class ``Setosa`` implementing ``IrisInterface``
    #. Implement interface
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz klasę ``Setosa`` implementującą ``IrisInterface``
    #. Zaimplementuj interfejs
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        class IrisInterface:
            sepal_length: float
            sepal_width: float
            petal_length: float
            petal_width: float

            def __init__(self,
                         sepal_length: float,
                         sepal_width: float,
                         petal_length: float,
                         petal_width: float) -> None:

                raise NotImplementedError

            def mean(self) -> float:
                raise NotImplementedError

            def sum(self) -> float:
                raise NotImplementedError

            def len(self) -> int:
                raise NotImplementedError


Tests:
    .. code-block:: text

        >>> assert issubclass(Setosa, IrisInterface)
        >>> assert hasattr(Setosa, 'mean')
        >>> assert hasattr(Setosa, 'sum')
        >>> assert hasattr(Setosa, 'len')

        >>> Setosa.__annotations__  # doctest: +NORMALIZE_WHITESPACE
        {'sepal_length': <class 'float'>,
         'sepal_width': <class 'float'>,
         'petal_length': <class 'float'>,
         'petal_width': <class 'float'>}

        >>> setosa = Setosa(5.1, 3.5, 1.4, 0.2)
        >>> setosa.len()
        4
        >>> setosa.sum()
        10.2
        >>> setosa.mean()
        2.55

Hints:
    * ``self.__dict__.values()``
    * ``mean = sum() / len()``
