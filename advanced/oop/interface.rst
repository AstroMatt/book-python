**********
Interfaces
**********



What it is?
===========
* Python don't have interfaces
* Cannot instantiate
* Inheriting class must implement all methods
* Only method declaration
* :pep:`544` Protocols: Structural subtyping (static duck typing)

.. glossary::
    interface
    implement

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


When use it?
============


Examples
========
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

OOP Interface Iris
------------------
* Assignment name: OOP Interface Iris
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 21 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/oop_interface_iris.py`

:English:
    #. Use code from "Input" section (see below)
    #. Define interface ``IrisInterface``
    #. Constuctor parameters: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Define methods ``sum()``, ``mean()``, ``len()`` in ``IrisInterface``
    #. Methods must raise exception ``NotImplementedError``
    #. Create class ``Setosa`` inheriting from ``IrisInterface``
    #. Create instance of a class ``Setosa`` and call ``mean()`` method
    #. Create instance of a class ``IrisInterface`` and call ``mean()`` method
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj interfejs ``IrisInterface``
    #. Parametry konstuktora: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Zdefiniuj metody ``sum()``, ``mean()``, ``len()`` w ``IrisInterface``
    #. Metody muszą podnosić wyjątek ``NotImplementedError``
    #. Stwórz klasę ``Setosa`` dziedziczące po ``IrisInterface``
    #. Stwórz instancje klasy ``Setosa`` i wywołaj metodę ``mean()``
    #. Stwórz instancje klasy ``IrisInterface`` i wywołaj metodę ``mean()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> setosa = Setosa(5.1, 3.5, 1.4, 0.2)
        >>> print(setosa.mean())
        2.55

        >>> iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
        Traceback (most recent call last):
            ...
        NotImplementedError

:Hints:
    * ``self.__dict__``
