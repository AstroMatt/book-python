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

Type Int Distance
-----------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_int_distance.py`

:English:
    #. Calculate altitude in meters:

        * Armstrong Line: 18 km
        * Stratosphere: 20 km
        * USAF Space Line: 80 km

    #. Calculate altitude in kilometers:

        * Kármán Line Earth: 100000 m
        * Kármán Line Mars: 80000 m
        * Kármán Line Venus: 250000 m

    #. In Calculations use truediv (``//``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Calculate altitude in meters:

        * Linia Armstronga: 18 km
        * Stratosfera: 20 km
        * Granica kosmosu wg. USAF: 80 km

    #. Calculate altitude in kilometers:

        * Linia Kármána Ziemia: 100000 m
        * Linia Kármána Mars: 80000 m
        * Linia Kármána Wenus: 250000 m

    #. W obliczeniach użyj truediv (``//``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        Armstrong Line: 18000 m
        Stratosphere: 20000 m
        USAF Space: 80000 m
        Kármán Line Earth: 100 km
        Kármán Line Mars: 80 km
        Kármán Line Venus: 250 km

:Hint:
    * 1 km = 1000 m

Type Int Time
-------------
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
    .. code-block:: text

        Day: 86400 sec
        Day: 1440 min
        Work day: 28800 sec
        Work week: 2400 min
        Work month: 176 h

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 h = 60 min
    * 1 min = 60 s

Type Int Bits
-------------
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bits.py`

:English:
    #. File size is 1 megabit
    #. Calculate size in bits
    #. Calculate size in kilobits
    #. W obliczeniach użyj truediv (``//``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Wielkość pliku to 1 megabit
    #. Oblicz wielkość w bitach
    #. Oblicz wielkość w kilobitach
    #. In Calculations use truediv (``//``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        Size: 1048576 b
        Size: 1024 kb

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb

Type Int Bytes
--------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bytes.py`

:English:
    #. File size is 1 megabyte
    #. Calculate size in megabits
    #. Print result in megabytes and megabits
    #. Compare result with "Output" section (see below)

:Polish:
    #. Wielkość pliku to 1 megabajt
    #. Oblicz wielkość w megabitach
    #. Wypisz wielkość w megabajtach oraz megabitach
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        Size: 1 MB
        Size: 8 Mb

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Type Int Bandwidth
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bandwidth.py`

:English:
    #. Having internet connection with speed up to 100 Mb/s
    #. How long will take to download 100 MB?
    #. W obliczeniach użyj truediv (``//``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Mając łącze internetowe "do 100 Mb/s"
    #. Ile zajmie ściągnięcie pliku 100 MB?
    #. In Calculations use truediv (``//``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        File size: 100 MB
        Download speed: 12 sec
        Download time: 8 sec

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Type Int Temperature
--------------------
* Complexity level: medium
* Lines of code to write: 18 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/type_int_temperature.py`

:English:
    #. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    #. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    #. For calculation use round number -273 (0K = -273°C)
    #. How many Kelvins and Celsius degrees has average temperatures at surface :cite:`MSL_REMS`:

        * Lunar day: 453 K
        * Lunar night: 93 K
        * Mars highest: 20 °C
        * Mars lowest: -153 °C
        * Mars average: −63 °C

    #. Compare result with "Output" section (see below)

:Polish:
    #. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    #. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    #. W zadaniu przyjmij równe -273°C (0K = -273°C)
    #. Ile Kelwinów, a ile stopni Celsiusza wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

        * Księżyca w dzień: 453 K
        * Księżyca w nocy: 93 K
        * Mars najwyższa: 20 °C
        * Mars najniższa: -153 °C
        * Mars średnia: −63 °C

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        Moon day: 453K, 726°C
        Moon night: 93K, 93°C
        Mars high: -253K, 20°C
        Mars low: -393K, -153°C
        Mars avg: -336K, -63°C

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations

