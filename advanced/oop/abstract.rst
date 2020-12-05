.. _OOP Abstract Class:

**************
Abstract Class
**************


Rationale
=========
.. versionadded:: 3.0
    :pep:`3119` -- Introducing Abstract Base Classes

* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation

.. glossary::

    abstract class
        Class which can only be inherited, not instantiated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Syntax
======
* New class ``ABC`` has ``ABCMeta`` as its meta class.
* Using ``ABC`` as a base class has essentially the same effect as specifying ``metaclass=abc.ABCMeta``, but is simpler to type and easier to read.
* ``abc.ABC`` basically just an extra layer over ``metaclass=abc.ABCMeta``
* ``abc.ABC`` implicitly defines the metaclass for you

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class MyClass(metaclass=ABCMeta):

        @abstractmethod
        def mymethod(self):
            pass


Abstract Method
===============
.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Astronaut(metaclass=ABCMeta):
        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

.. code-block:: python

    from abc import ABC, abstractmethod


    class Astronaut(ABC):
        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello


Abstract Property
=================
.. code-block:: python

    from abc import ABCMeta, abstractproperty


    class HasGold(metaclass=ABCMeta):
        @abstractproperty
        def GOLD_MIN(self):
            raise NotImplementedError

        @abstractproperty
        def GOLD_MAX(self):
            raise NotImplementedError


    class Hero(HasGold):
        GOLD_MIN: int = 1
        GOLD_MAX: int = 10
        name: str

        def __init__(self, name):
            self.name = name


    my = Hero('Mark Watney')
    print(my.name)
    # Mark Watney

.. code-block:: python

    from abc import ABCMeta, abstractproperty


    class HasGold(metaclass=ABCMeta):
        @abstractproperty
        def GOLD_MIN(self):
            raise NotImplementedError

        @abstractproperty
        def GOLD_MAX(self):
            raise NotImplementedError


    class Hero(HasGold):
        name: str

        def __init__(self, name):
            self.name = name


    my = Hero('Mark Watney')
    print(my.name)
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Hero with abstract methods GOLD_MAX, GOLD_MIN


Errors
======
.. code-block:: python
    :caption: In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating.

    from abc import ABC


    class Astronaut(ABC):
        pass


    astro = Astronaut()
    print('no errors')
    # no errors

.. code-block:: python
    :caption: In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating.

    from abc import ABCMeta


    class Astronaut(metaclass=ABCMeta):
        pass


    astro = Astronaut()
    print('no errors')
    # no errors

.. code-block:: python
    :caption: Must implement all abstract methods

    from abc import ABCMeta, abstractmethod


    class Human(metaclass=ABCMeta):
        @abstractmethod
        def say_hello(self):
            pass


    class Astronaut(Human):
        pass


    astro = Astronaut()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

.. code-block:: python
    :caption: ``abc`` is common name and it is very easy to create file, variable lub module with the same name as the library, hence overwrite it. In case of error. Check all entries in ``sys.path`` or ``sys.modules['abc']`` to find what is overwriting it.

    from pprint import pprint
    import sys


    sys.modules['abc']
    # <module 'abc' from '/usr/local/Cellar/python@3.9/3.9.0/Frameworks/Python.framework/Versions/3.9/lib/python3.9/abc.py'>

    pprint(sys.path)
    # ['/Applications/PyCharm 2020.3 EAP.app/Contents/plugins/python/helpers/pydev',
    #  '/Users/watney/book-python',
    #  '/Applications/PyCharm 2020.3 EAP.app/Contents/plugins/python/helpers/pycharm_display',
    #  '/Applications/PyCharm 2020.3 EAP.app/Contents/plugins/python/helpers/third_party/thriftpy',
    #  '/Applications/PyCharm 2020.3 EAP.app/Contents/plugins/python/helpers/pydev',
    #  '/usr/local/Cellar/python@3.9/3.9.0/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
    #  '/usr/local/Cellar/python@3.9/3.9.0/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
    #  '/usr/local/Cellar/python@3.9/3.9.0/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
    #  '/Users/watney/.virtualenvs/python-3.9/lib/python3.9/site-packages',
    #  '/Applications/PyCharm 2020.3 EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
    #  '/Users/watney/book-python',
    #  '/Users/watney/book-python/_tmp']


Use Cases
=========
.. code-block:: python
    :caption: Abstract Class

    from abc import ABC, abstractmethod


    class Document(ABC):
        def __init__(self, file):
            with open(file, mode='rb') as file:
                self.file = file
                self.content = file.read()

        @abstractmethod
        def display(self):
            pass


    class PDFDocument(Document):
        def display(self):
            # display self.content as PDF Document

    class WordDocument(Document):
        def display(self):
            # display self.content as Word Document


    file1 = PDFDocument('filename.pdf')
    file1.display()

    file2 = Document('filename.txt')
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Document with abstract method display


Assignments
===========

.. literalinclude:: assignments/oop_abstract_syntax.py
    :caption: :download:`Solution <assignments/oop_abstract_syntax.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_interface.py
    :caption: :download:`Solution <assignments/oop_abstract_interface.py>`
    :end-before: # Solution
