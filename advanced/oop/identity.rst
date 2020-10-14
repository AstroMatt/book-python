.. _OOP Object Identity:

***************
Object Identity
***************


Identity
========
.. highlights::
    * ``id()`` will change every time you execute script
    * An integer which is guaranteed to be unique and constant for this object during its lifetime
    * Two objects with non-overlapping lifetimes may have the same ``id()`` value.
    * In CPython it's also the memory address of the corresponding C object

.. code-block:: python
    :caption: Note, that ``id()`` will change every time you execute script

    id('Watney')
    # 4499664048

    hex(id('Watney'))
    # '0x10c336cb0'

.. code-block:: python

    >>> a = 'Jan Twardowski'
    >>> b = 'Jan Twardowski'

    >>> a == b
    True
    >>> a is b
    False

    >>> id(a) == id(b)
    False
    >>> hex(id(a)) == hex(id(b))
    False
    >>> hash(a) == hash(b)
    True

.. code-block:: python

    >>> a = 'Jan Twardowski'
    ... b = 'Jan Twardowski'

    >>> a == b
    True
    >>> a is b
    True

    >>> id(a) == id(b)
    True
    >>> hex(id(a)) == hex(id(b))
    True
    >>> hash(a) == hash(b)
    True


Identity Check
==============
.. highlights::
    * ``is`` checks for object identity
    * ``is`` tests for identity, not equality
    * Compares ``id()`` output for both objects
    * CPython: compares the memory address a object resides in
    * Is used for checking if ``None``
    * Testing strings with ``is`` only works when the strings are interned

.. code-block:: python
    :caption: Test if empty

    if name is None:
        print('Your name is empty')
    else:
        print(f'Hello {name}')


Value Comparison
================
.. versionchanged:: Python 3.8
    Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

.. code-block:: python

    'Mark Watney' is 'Mark Watney'
    # <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    # True

.. code-block:: python

    'Mark Watney' == 'Mark Watney'
    # True



Assignments
===========
.. todo:: Create assignments
