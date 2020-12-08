Type None
=========


Definition
----------
* First letter capitalized, other are lower cased
* Empty (null) or unknown (unset) value
* It is not ``False`` value
* With ``if`` statements behaves like negative values

    >>> data = None


Comparison
----------
* Do not use ``==`` or ``!=`` to check ``None`` values (it works, but you shouldn't)
* ``x is None`` - ``x`` is the same object as ``y``
* ``x is not None`` - ``x`` is not the same object as ``y``

    >>> age = None
    >>>
    >>> age == None
    True
    >>> age != None
    False

    >>> age = None
    >>>
    >>> age is None
    True
    >>> age is not None
    False


Assignments
-----------
.. literalinclude:: assignments/type_none.py
    :caption: :download:`Solution <assignments/type_none.py>`
    :end-before: # Solution
