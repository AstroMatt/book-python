.. _OOP Object Identity:

***************
Object Identity
***************


Rationale
=========
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity

.. code-block:: python

    found = True
    found == True
    found is True


Identity
========
* ``id(obj) -> int``
* ``id()`` will change every time you execute script
* ``id()`` returns an integer which is guaranteed to be unique and constant for object during its lifetime
* Two objects with non-overlapping lifetimes may have the same ``id()`` value
* In CPython it's also the memory address of the corresponding C object

.. code-block:: python

    id('Watney')
    # 4499664048

    hex(id('Watney'))
    # '0x10c336cb0'


Value Comparison
================
* ``==`` checks for object equality

.. code-block:: python

    'Mark Watney' == 'Mark Watney'
    # True

.. code-block:: python

    a = 'Mark Watney'
    b = 'Mark Watney'

    a == b
    # True


Identity Check
==============
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned

.. versionchanged:: Python 3.8
    Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

.. code-block:: python

    'Mark Watney' is 'Mark Watney'
    # <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    # True

.. code-block:: python

    a = 'Mark Watney'
    b = 'Mark Watney'

    a is b

.. code-block:: python

    name = None

    name is None
    name is True
    name is False

.. code-block:: python

    name = None

    type(name) is int
    type(name) is float
    type(name) is complex
    type(name) is bool
    type(name) is None
    type(name) is str
    type(name) is bytes
    type(name) is list
    type(name) is tuple
    type(name) is set
    type(name) is frozenset
    type(name) is dict


Problem
=======
.. code-block:: python

    'Mark Watney' is 'Mark Watney'
    # True

.. code-block:: python

    >>> a = 'Mark Watney'
    ... b = 'Mark Watney'

    >>> a == b
    True

    >>> a is b
    True

.. code-block:: python

    >>> a = 'Mark Watney'
    >>> b = 'Mark Watney'

    >>> a == b
    True

    >>> a is b
    False


Compare Value and Identity
==========================
.. code-block:: python

    name = 'Mark Watney'
    expected = 'Mark Watney'

    name == expected
    # True

    name is expected
    # False

    name == 'Mark Watney'
    # True

    name is 'Mark Watney'
    # False


Assignments
===========
.. todo:: Create assignments
