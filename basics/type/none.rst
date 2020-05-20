.. _Type None:

*********
Type None
*********


Type Definition
===============
.. highlights::
    * First letter capitalized, other are lower cased
    * Empty (null) or unknown (unset) value
    * It is not ``False`` value
    * With ``if`` statements behaves like negative values

.. code-block:: python
    :caption: ``NoneType`` Type Definition

    data = None


Comparision
===========
.. highlights::
    * Do not use ``==`` or ``!=`` to check ``None`` values (it works, but you shouldn't)

.. code-block:: python

    age = None

    age == None             # True
    age != None             # False


Identity
========
.. highlights::
    * ``x is None`` - ``x`` is the same object as ``y``
    * ``x is not None`` - ``x`` is not the same object as ``y``

.. code-block:: python

    age = None

    age is None             # True
    age is not None         # False


Assignments
===========

Is ``None`` or ``not``
----------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_none.py`

:English:
    #. Use data from "Input" section (see below)
    #. What you need to put in expressions to get the expected outcome?
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

            a = ... is None                                                                       # True
            b = ... is not None                                                                   # False
            c = bool(bool(...) is not bool(...)) == False                                         # True
            d = (bool(bool(...) is not bool(...)) == False and bool(...))                         # False
            e = (bool(bool(...) is not bool(...)) == False and bool(...)) and (... is not None)   # False

:Output:
    .. code-block:: python

            print(a)    # True
            print(b)    # False
            print(c)    # True
            print(d)    # False
            print(e)    # False

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types


.. todo:: Create more assignments
