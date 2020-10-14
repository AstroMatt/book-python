.. _OOP Access Modifiers:

****************
Access Modifiers
****************


Rationale
=========
.. highlights::
    * Attributes and methods are always public
    * No protected and private keywords

    Attributes:

        * ``__name__`` - system attribute or method
        * ``__name`` - private attribute
        * ``_name`` - protected attribute (by convention)
        * ``name_`` - used while name collision

    Methods:

        * ``__name__(self)`` - system method
        * ``__name(self)`` - private method
        * ``_name(self)`` - protected method (by convention)
        * ``name_(self)`` - used while name collision


Protected Attribute
===================
* ``_name`` - protected attribute (by convention)

.. code-block:: python
    :caption: Access modifiers

    class Temperature:
        pass


    temp = Temperature()
    temp._value = 10

    print(temp._value)  # IDE should warn, that you access protected member
    # 10

.. code-block:: python
    :caption: Access modifiers

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(mark._firstname)  # IDE should warn: "Access to a protected member _firstname of a class "
    # Mark

    print(mark._lastname)  # IDE should warn: "Access to a protected member _lastname of a class "
    # Watney

    print(mark.publicname)
    # Mark W.

    print(mark.firstname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute 'firstname'

    print(mark.lastname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute 'lastname'


Private Attribute
=================
* ``__name`` - private attribute

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.__firstname = firstname
            self.__lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(astro.publicname)
    # Mark W.

    print(astro.__firstname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(astro.__lastname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(astro.__dict__)
    # {'_Astronaut__firstname': 'Mark',
    #  '_Astronaut__lastname': 'Watney',
    #  'publicname': 'Mark W.'}


System Attributes
=================
* ``__name__`` - system attribute

.. code-block:: python
    :caption: ``obj.__dict__`` - Getting dynamic fields and values

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.__dict__)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney'}

.. code-block:: python
    :caption: ``obj.__dict__`` - Getting dynamic fields and values

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(astro.__dict__)
    # {'_firstname': 'Mark',
    #  '_lastname': 'Watney',
    #  'publicname': 'Mark W.'}

    public_attributes = {attribute: value
                         for attribute, value in astro.__dict__.items()
                         if not attribute.startswith('_')}

    print(public_attributes)
    # {'publicname': 'Mark W.'}



Protected Method
================
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def _get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    astro = Astronaut('Mark', 'Watney')

    print(dir(astro))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_firstname',
    # '_get_fullname', '_lastname', 'get_publicname']

    public_methods = [method
                      for method in dir(astro)
                      if not method.startswith('_')]

    print(public_methods)
    # ['get_publicname']


Private Method
==============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(dir(mark))
    # ['_Astronaut__get_fullname', '__class__', '__delattr__', '__dict__',
    #  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    #  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    #  '__weakref__', '_firstname', '_lastname', 'get_publicname']

    public_methods = [method
                      for method in dir(astro)
                      if not method.startswith('_')]

    print(public_methods)
    # ['get_publicname']

    mark.__get_fullname()
    # Traceback (most recent call last):
    #   ...
    # AttributeError: 'Astronaut' object has no attribute '__get_fullname'


System Method
=============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __str__(self):
            return 'stringification'

        def __repr__(self):
            return 'representation'


    mark = Astronaut('Mark', 'Watney')

    print(str(mark))
    # stringification

    print(repr(mark))
    # representation


Assignments
===========

OOP Attribute Access Modifiers
------------------------------
* Assignment name: OOP Attribute Access Modifiers
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 11 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/oop_attribute_access_modifiers.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list[dict]``
    #. Define class ``Iris`` with attributes
    #. Protected attributes: ``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``
    #. Public attribute: ``species``
    #. Iterate over ``DATA`` and add all public attributes to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: list[dict]``
    #. Define klasę ``Iris``
    #. Chronione atrybuty: ``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``
    #. Publiczne atrybuty: ``species``
    #. Iteruj po ``DATA`` i dodaj wszystkie publiczne atrybuty do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
            Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
            Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        ]

:Output:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'species': 'virginica'},
         {'species': 'setosa'},
         {'species': 'versicolor'}]

OOP Attribute Access Dict
-------------------------
* Assignment name: OOP Attribute Access Dict
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 35 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/oop_attribute_access_dict.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: list[Iris]``
    #. Iterate over ``DATA`` skipping header
    #. Separate ``features`` from ``species`` in each row
    #. Append to ``result``:

        * if ``species`` is "setosa" append instance of a class ``Setosa``
        * if ``species`` is "versicolor" append instance of a class ``Versicolor``
        * if ``spceies`` is "virginica" append instance of a class ``Virginica``

    #. Initialize instances with ``features`` using ``*args`` notation
    #. Print instance class name and then both sum and mean
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: list[Iris]``
    #. Iterując po ``DATA`` pomijając header
    #. Odseparuj ``features`` od ``species`` w każdym wierszu
    #. Dodaj do ``result``:

        * jeżeli ``species`` jest "setosa" to dodaj instancję klasy ``Setosa``
        * jeżeli ``species`` jest "versicolor" to dodaj instancję klasy ``Versicolor``
        * jeżeli ``species`` jest "virginica" to dodaj instancję klasy ``Virginica``

    #. Instancje inicjalizuj danymi z ``features`` używając notacji ``*args``
    #. Wypisz nazwę stworzonej klasy oraz średnią z pomiarów
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
        ]

        class Iris:
            def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
                self._sepal_length = sepal_length
                self._sepal_width = sepal_width
                self._petal_length = petal_length
                self._petal_width = petal_width

            def __repr__(self):
                raise NotImplementedError

            def values(self):
                raise NotImplementedError

            def mean(self):
                return sum(self.values()) / len(self.values())


        class Setosa(Iris):
            pass

        class Versicolor(Iris):
            pass

        class Virginica(Iris):
            pass

:Output:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'name': 'Virginica',  'mean': 3.88},
         {'name': 'Setosa',     'mean': 2.55},
         {'name': 'Versicolor', 'mean': 3.48},
         {'name': 'Virginica',  'mean': 4.15},
         {'name': 'Versicolor', 'mean': 3.9},
         {'name': 'Setosa',     'mean': 2.35}]

:Hints:
    * ``self.__class__.__name__``
    * ``self.__dict__.values()``
    * ``globals()[classname]``
