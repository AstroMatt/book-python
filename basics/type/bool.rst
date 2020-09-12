.. _Type Bool:

*********
Type Bool
*********


Type Definition
===============
.. highlights::
    * ``True`` - Positive value
    * ``False`` - Negative value
    * First letter capitalized, other are lower cased

.. code-block:: python
    :caption: ``bool`` Type Definition

    data = True               # True
    data = False              # False


Type Casting
============
.. code-block:: python
    :caption: ``bool()`` converts argument to ``bool``

    bool(1)                     # True
    bool(1.0)                   # True
    bool('Jan Twardowski')      # True

.. code-block:: python
    :caption: Negative values

    bool(0)                     # False
    bool(0.0)                   # False
    bool(0+0j)                  # False
    bool(0.0+0.0j)              # False
    bool(False)                 # False
    bool(None)                  # False
    bool('')                    # False
    bool(())                    # False
    bool([])                    # False
    bool({})                    # False

    bool(int())                 # False
    bool(float())               # False
    bool(complex())             # False
    bool(bool())                # False
    bool(str())                 # False
    bool(tuple())               # False
    bool(list())                # False
    bool(dict())                # False
    bool(set())                 # False
    bool(frozenset())           # False


Conjunction
===========
.. code-block:: python

    True and True               # True
    True and False              # False
    False and True              # False
    False and False             # False

.. code-block:: python

    1 and 1                     # True
    1 and 0                     # False
    0 and 1                     # False
    0 and 0                     # False

.. code-block:: python

    'Jan' and 'Jan'             # True
    'Jan' and ''                # False
    '' and 'Jan'                # False
    '' and ''                   # False

.. code-block:: python

    'Jan' and 1                 # True
    'Jan' and 0                 # False
    0.0 and 'Jan'               # False
    1 and False                 # False


Disjunction
===========
.. code-block:: python

    True or True                # True
    True or False               # True
    False or True               # True
    False or False              # False

.. code-block:: python

    1 or 1                      # True
    1 or 0                      # True
    0 or 1                      # True
    0 or 0                      # False

.. code-block:: python

    'José' or 'Иван'            # True
    'José' or ''                # True
    '' or 'José'                # True
    '' or ''                    # False

.. code-block:: python

    1 or 'Иван'                 # True
    True or ''                  # True
    0 or True                   # True
    0.0 or False                # False


Boolean Algebra
===============
.. code-block:: python

    True and True or False      # True
    False and False or True     # True

.. code-block:: python

    (True and True) or False    # True
    True and (True or False)    # True

    True and False or False     # False
    True and (False or False)   # False

.. code-block:: python

    (firstname == 'Mark' and lastname == 'Watney') \
        or (firstname == 'Jan' and lastname == 'Twardowski') \
        or (firstname == 'Melissa' and lastname == 'Lewis')


Built-in Functions
==================
* ``type()`` - Checks type of an object
* ``isinstance(a, b)`` - If ``a`` is instance of ``b``
* ``isinstance(a, (b,c))`` - If ``a`` is instance of ``b`` or ``c``

.. code-block:: python

    type(True)                      # <class 'bool'>
    type(False)                     # <class 'bool'>

.. code-block:: python

    isinstance(1, bool)             # False
    isinstance(1, int)              # True
    isinstance(1, float)            # False

    isinstance(1.23, bool)          # False
    isinstance(1.23, int)           # False
    isinstance(1.23, float)         # True

    isinstance(True, bool)          # True
    isinstance(True, int)           # True
    isinstance(True, float)         # False

    isinstance(False, bool)         # True
    isinstance(False, int)          # True
    isinstance(False, float)        # False


Example
=======
.. code-block:: python

    import numpy as np

    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True],
    #        [ True,  True,  True]])

    a < 7
    # array([[ True,  True,  True],
    #        [ True,  True,  True],
    #        [False, False, False]])

    a == 9
    # array([[False, False, False],
    #        [False, False, False],
    #        [False, False,  True]])

    (a>2) & (a<7) | (a==9)
    # array([[False, False,  True],
    #        [ True,  True,  True],
    #        [False, False,  True]])

    a[(a>2) & (a<7) | (a==9)]
    # array([3, 4, 5, 6, 9])


Assignments
===========

Type Bool True or False
-----------------------
* Complexity level: easy
* Lines of code to write: 16 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_bool_true_or_false.py`

:English:
    #. Use data from "Input" section (see below)
    #. Which variables are ``True``?
    #. Which variables are ``False``?

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Które zmienne są ``True``?
    #. Które zmienne są ``False``?

:Input:
    .. code-block:: python

        a = bool(False)
        b = bool(True)

        c = bool(0)
        d = bool(0.0)
        e = bool(-0)
        f = bool(-0.0)

        g = bool('a')
        h = bool('.')
        i = bool('0')
        j = bool('0.0')
        k = bool('')
        l = bool(' ')

        m = bool(int('0'))
        n = bool(float(str(-0)))

        o = bool(-0.0+0.0j)
        p = bool('-0.0+0.0j')
        q = bool(complex('-0.0+0.0j'))

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types

Type Bool Simple
----------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_bool_simple.py`

:English:
    #. Use data from "Input" section (see below)
    #. What you need to put in expressions to get the expected outcome?
    #. Insert only ``True`` or ``False``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    #. Wstawiaj tylko ``True`` lub ``False``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        a = bool(...) == True                   # True
        b = bool(...) == False                  # True
        c = ... == True                         # True
        d = ... != False                        # True
        e = ... or ...                          # True
        f = ... and ...                         # False
        g = bool(bool(...) == False) or False   # True
        h = bool(...) is not bool(...)          # False

:Output:
    .. code-block:: python

        print(bool(a))                          # True
        print(bool(b))                          # True
        print(bool(c))                          # True
        print(bool(d))                          # True
        print(bool(e))                          # True
        print(bool(f))                          # False
        print(bool(g))                          # True
        print(bool(h))                          # False

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types
