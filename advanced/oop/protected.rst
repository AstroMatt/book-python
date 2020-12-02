.. _OOP Protected:

*********
Protected
*********


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
    # AttributeError: 'Astronaut' object has no attribute 'firstname'

    print(mark.lastname)
    # Traceback (most recent call last):
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
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(astro.__lastname)
    # Traceback (most recent call last):
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

.. literalinclude:: solution/oop_protected_modifiers.py
    :caption: :download:`Solution <solution/oop_protected_modifiers.py>`
    :end-before: # Solution

.. literalinclude:: solution/oop_protected_dict.py
    :caption: :download:`Solution <solution/oop_protected_dict.py>`
    :end-before: # Solution
