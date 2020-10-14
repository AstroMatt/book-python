.. _OOP String Interning:

****************
String Interning
****************


Rationale
=========
.. highlights::
    * https://en.wikipedia.org/wiki/String_interning
    * Method of storing only one copy of each distinct string value, which must be immutable
    * many high level languages use it
    * string literals and values are internally kept in a hashed list called 'string intern pool' and those which are identical are rendered as references to the same object
    * possible because ``str`` are immutable
    * implementation dependent
    * Jython, IronPython, PyPy and others may intern more aggressively
    * Calling the ``intern()`` function on strings will "force" a string to have the same object identity as any equivalent and previously interned string

Example
=======
.. code-block:: python
    :caption: CPython 3.7, 3.8, 3.9

    ('a' * 4096) is ('a' * 4096)
    # True

    ('a' * 4097) is ('a' * 4097)
    # False

.. figure:: img/identity-str-1.png
    :align: center
    :scale: 50%

    Define str

.. figure:: img/identity-str-2.png
    :align: center
    :scale: 50%

    Define another str with the same value

.. figure:: img/identity-str-3.png
    :align: center
    :scale: 50%

    Define another str with different value
