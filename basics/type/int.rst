.. _Type Int:

********
Type Int
********


Type Definition
===============
.. highlights::
    * In Python 3 there is not maximal ``int`` value
    * Python 3 dynamically extends ``int``, when it's too big
    * You can use ``_`` for easier read especially with big numbers

.. code-block:: python
    :caption: ``int`` Type Definition

    data = 1337                 # 1337
    data = -1337                # -1337

.. code-block:: python

    million = 1000000           # 1000000
    million = 1_000_000         # 1000000


Type Casting
============
.. highlights::
    * ``int()`` - converts argument to ``int``
    * ``int()`` - does not round numbers

.. code-block:: python
    :caption: ``int()`` converts argument to ``int``

    int(13)                     # 13
    int(13.0)                   # 13
    int(13.3)                   # 13
    int(13.37)                  # 13

    int(-13.37)                 # -13

    int('1')                    # 1
    int('+1')                   # 1
    int('-1')                   # -1
    int('1_000_000')            # 1000000

    int('13.37')                # ValueError: invalid literal for int() with base 10: '13.37'
    int('13,37')                # ValueError: invalid literal for int() with base 10: '13,37'
    int('-13.37')               # ValueError: invalid literal for int() with base 10: '-13.37'
    int('-13,37')               # ValueError: invalid literal for int() with base 10: '-13,37'

.. code-block:: python

    int('0x69', base=16)        # 105
    int('0x3C', base=16)        # 60
    int('0o754', base=8)        # 492


Type Checking
=============
.. highlights::
    * ``type()`` - Returns type of an argument

.. code-block:: python

    type(1)                     # <class 'int'>
    type(-1)                    # <class 'int'>
    type(0)                     # <class 'int'>
    type(-0)                    # <class 'int'>


Assignments
===========

Type Int Add
------------
* Assignment name: Type Int Add
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_add.py`

:English:
    #. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    #. Zero Celsius degrees is equal to 273.15 Kelvins
    #. For calculation use round number 273 (0°K = -273K)
    #. How many Kelvins has average temperatures at surface :cite:`MSL_REMS`:

        * Mars highest: 20 °C
        * Mars lowest: -153 °C
        * Mars average: −63 °C

    #. Compare result with "Output" section (see below)

:Polish:
    #. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    #. Zero stopni Celsiusza to 273.15 Kelwiny
    #. W zadaniu przyjmij równe 273°C (0°K = -273K)
    #. Ile Kelwinów wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

        * Mars najwyższa: 20 °C
        * Mars najniższa: -153 °C
        * Mars średnia: −63 °C

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> mars_max
        293
        >>> mars_min
        153
        >>> mars_avg
        210

:The whys and wherefores:
    * Defining constants and variables
    * Mathematical operations

Type Int Sub
------------
* Assignment name: Type Int Sub
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_sub.py`

:English:
    #. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    #. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    #. For calculation use round number -273 (0K = -273°C)
    #. How many Celsius degrees has average temperatures at surface :cite:`MSL_REMS`:

        * Lunar day: 453 K
        * Lunar night: 93 K

    #. Compare result with "Output" section (see below)

:Polish:
    #. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    #. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    #. W zadaniu przyjmij równe -273°C (0K = -273°C)
    #. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

        * Księżyca w dzień: 453 K
        * Księżyca w nocy: 93 K

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> moon_day
        180
        >>> moon_night
        -180

:The whys and wherefores:
    * Defining constants and variables
    * Mathematical operations

Type Int Mul
------------
* Assignment name: Type Int Mul
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_mul.py`

:English:
    #. Calculate altitude in meters:

        * Armstrong Line: 18 km
        * Stratosphere: 20 km
        * USAF Space Line: 80 km

    #. Compare result with "Output" section (see below)

:Polish:
    #. Oblicz wysokości w metrach:

        * Linia Armstronga: 18 km
        * Stratosfera: 20 km
        * Granica kosmosu wg. USAF: 80 km

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> armstrong_line // m
        18000
        >>> stratosphere // m
        20000
        >>> usaf_space // m
        80000

:Hints:
    * 1 km = 1000 m

Type Int Truediv
----------------
* Assignment name: Type Int Truediv
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_truediv.py`

:English:
    #. Calculate altitude in kilometers:

        * Kármán Line Earth: 100000 m
        * Kármán Line Mars: 80000 m
        * Kármán Line Venus: 250000 m

    #. In Calculations use truediv (``//``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Oblicz wysokości w kilometrach:

        * Linia Kármána Ziemia: 100000 m
        * Linia Kármána Mars: 80000 m
        * Linia Kármána Wenus: 250000 m

    #. W obliczeniach użyj truediv (``//``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> karman_line_earth // km
        100
        >>> karman_line_mars // km
        80
        >>> karman_line_venus // km
        250

:Hints:
    * 1 km = 1000 m

Type Int Time
-------------
* Assignment name: Type Int Time
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/type_int_time.py`

:English:
    #. Calculate how many seconds is one day
    #. Calculate how many minutes is one day
    #. Calculate how many seconds is work day (8 hours)
    #. Calculate how many minutes is work week (5 work days)
    #. Calculate how many hours is work month (22 work days)
    #. In Calculations use truediv (``//``)

:Polish:
    #. Oblicz ile sekund to jedna doba
    #. Oblicz ile minut to je jedna doba
    #. Oblicz ile sekund to dzień pracy (8 godzin)
    #. Oblicz ile minut to tydzień pracy (5 dni pracy)
    #. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    #. W obliczeniach użyj truediv (``//``)

:Output:
    .. code-block:: python

    >>> DAY // SECOND
    86400
    >>> DAY // MINUTE
    1440
    >>> workday // SECOND
    28800
    >>> workweek // MINUTE
    2400
    >>> workmonth // HOUR
    176

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 h = 60 min
    * 1 min = 60 s

Type Int Bits
-------------
* Assignment name: Type Int Bits
* Last update: 2020-11-16
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bits.py`

:English:
    #. File size is 1 megabit
    #. Calculate size in bits
    #. Calculate size in kilobits
    #. Compare result with "Output" section (see below)

:Polish:
    #. Wielkość pliku to 1 megabit
    #. Oblicz wielkość w bitach
    #. Oblicz wielkość w kilobitach
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> size // b
        1048576
        >>> size // kb
        1024

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb

Type Int Bytes
--------------
* Assignment name: Type Int Bytes
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bytes.py`

:English:
    #. File size is 100 megabytes
    #. Calculate size in megabits
    #. Compare result with "Output" section (see below)

:Polish:
    #. Wielkość pliku to 100 megabajtów
    #. Oblicz wielkość w megabitach
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> size // MB
        100
        >>> size // Mb
        800

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Type Int Bandwidth
------------------
* Assignment name: Type Int Bandwidth
* Last update: 2020-11-16
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bandwidth.py`

:English:
    #. Having internet connection with speed 100 Mb/s
    #. How long will take to download 100 MB?
    #. In Calculations use truediv (``//``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Mając łącze internetowe 100 Mb/s
    #. Ile zajmie ściągnięcie pliku 100 MB?
    #. W obliczeniach użyj truediv (``//``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        >>> duration // SECOND
        8

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB
