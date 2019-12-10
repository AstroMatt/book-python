********
``bool``
********


Defining ``bool``
=================
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased

.. code-block:: python

    my_var = True               # True
    my_var = False              # False

    my_var: bool = True               # True
    my_var: bool = False              # False


Converting to ``bool``
======================
* Also known as "type casting"
* ``bool()`` converts argument to ``bool``

.. code-block:: python

    bool(1)                     # True
    bool(0)                     # False

.. code-block:: python

    bool(1.0)                   # True
    bool(0.0)                   # False

.. code-block:: python

    bool('Jan Twardowski')      # True
    bool('')                    # False


Negative values
===============
* ``False``
* ``None``
* ``0``
* ``0.0``
* ``0+0j``
* ``0.0+0.0j``
* empty ``str()`` or ``''``
* empty ``tuple()`` or ``()``
* empty ``dict()`` or ``{}``
* empty ``list()`` or ``[]``
* empty ``set()``


Boolean logic
=============

Using ``and``
-------------
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

Using ``or``
------------
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

Using both: ``or`` and ``and``
------------------------------
.. code-block:: python

    True and True or False      # True
    True and False or False     # False
    False and False or True     # True


Logic operators
===============
.. csv-table:: Logic operators
    :header-rows: 1
    :widths: 15, 25, 60

    "Operand", "Example", "Description"
    "``x < y``", "``x < 18``", "value of ``x`` is less than ``y``"
    "``x <= y``", "``x <= 18``", "value of ``x`` is less or equal ``y``"
    "``x > y``", "``x > 18``", "value of ``x`` is greater than ``y``"
    "``x >= y``", "``x >= 18``", "value of ``x`` is greater or equal than ``y``"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/bool_simple.py`

:English:
    #. Which variables are ``True``?
    #. Which variables are ``False``?

:Polish:
    #. Które zmienne są ``True``?
    #. Które zmienne są ``False``?

:Input:
    .. code-block:: python

        a = bool(False)
        b = bool(True)

        c = bool('a')
        d = bool('.')
        e = bool('0')
        f = bool('0.0')
        g = bool('')
        h = bool(' ')

        i = bool(0)
        j = bool(0.0)
        k = bool(-0)
        l = bool(-0.0)

        m = bool(int('0'))
        n = bool(float('-0'))

        o = bool(-0.0+0.0j)
        p = bool('-0.0+0.0j')

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types

``True`` of ``False``
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/bool_true_or_false.py`

:English:
    #. What you need to put in expressions to get the expected outcome?

:Polish:
    #. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?

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

        print(a)                                # True
        print(b)                                # True
        print(c)                                # True
        print(d)                                # True
        print(e)                                # True
        print(f)                                # False
        print(g)                                # True
        print(h)                                # False

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types
