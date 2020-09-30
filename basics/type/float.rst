.. _Type Float:

**********
Type Float
**********


Type Definition
===============
.. highlights::
    * Notation without leading or trailing zero is used by ``numpy``

.. code-block:: python
    :caption: ``float`` Type Definition

    data = 13.37             # 13.37
    data = -13.37            # -13.37

.. code-block:: python
    :caption: Notation without leading or trailing zero

    data = 10.               # 10.0
    data = .44               # 0.44

.. code-block:: python
    :caption: Engineering notation

    million = 1e6           # 1000000.0
    million = 1E6           # 1000000.0

    +1e6                    # 1000000.0
    -1e6                    # -1000000.0

    1e-3                    # 0.001
    1e-4                    # 0.0001
    1e-5                    # 1e-05
    1e-6                    # 1e-06

    1.337 * 1e3             # 1337.0
    1.337 * 1e-3            # 0.001337


Type Casting
============
.. highlights::
    * ``float()`` converts argument to ``float``

.. code-block:: python
    :caption: ``float()`` converts argument to ``float``

    float(13)               # 13.0
    float(+13)              # 13.0
    float(-13)              # -13.0

    float(13.37)            # 13.37
    float(+13.37)           # 13.37
    float(-13.37)           # -13.37

    float('13.37')          # 13.37
    float('+13.37')         # 13.37
    float('-13.37')         # -13.37

    float('13,37')          # ValueError: could not convert string to float: '13,37'
    float('+13,37')         # ValueError: could not convert string to float: '+13,37'
    float('-13,37')         # ValueError: could not convert string to float: '-13,37'


Round Number
============
.. highlights::
    * ``round()`` - Rounds a number

.. code-block:: python
    :caption: ``round()`` - Rounds a number

    pi = 3.14159265359

    round(pi, 4)            # 3.1416
    round(pi, 2)            # 3.14
    round(pi)               # 3

.. code-block:: python
    :caption: Rounds a number in print formatting

    pi = 3.14159265359

    print(f'Pi number is {pi}')         # Pi number is 3.14159265359
    print(f'Pi number is {pi:f}')       # Pi number is 3.141593
    print(f'Pi number is {pi:.4f}')     # Pi number is 3.1416
    print(f'Pi number is {pi:.2f}')     # Pi number is 3.14

.. code-block:: python

    round(10.5)             # 10
    round(10.51)            # 11


Built-in Functions
==================
.. highlights::
    * ``abs()`` - Absolute value
    * ``pow()`` - Number to the ``n-th`` power
    * Note, that arithmetic operator ``**`` also raises number to the power

.. code-block:: python
    :caption: ``pow()`` - Number to the ``n-th`` power

    pow(10, 2)          # 100
    pow(2, -1)          # 0.5

    pow(1.337, 3)       # 2.389979753
    pow(4, 0.5)         # 2.0
    pow(2, 0.5)         # 1.4142135623730951

    pow(4, 1/2)         # 2.0
    pow(2, 1/2)         # 1.4142135623730951
    pow(27, 1/3)        # 3.0

.. code-block:: python
    :caption: ``abs()`` - Absolute value

    abs(1)                      # 1
    abs(13.37)                  # 13.37

    abs(-1)                     # 1
    abs(-13.37)                 # 13.37


Assignments
===========

Type Float Tax
--------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_float_tax.py`

:English:
    #. Cost of the service is 100 PLN net
    #. Service has value added tax (VAT) rate of 23%
    #. Calculate tax and gross values
    #. To calculate tax, multiply net times VAT
    #. To calculate gross multiply net times VAT plus 1
    #. Mind the operator precedence
    #. Compare result with "Output" section (see below)

:Polish:
    #. Cena usługi wynosi 100 PLN netto
    #. Usługa objęta jest 23% stawką VAT
    #. Oblicz wartości podatku oraz cenę brutto
    #. Aby obliczyć podatek, pomnóż cenę netto razy stawkę VAT
    #. Aby obliczyć cenę brutto pomnóż cenę netto razy stawka VAT plus 1
    #. Zwróć uwagę na kolejność wykonywania działań
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        net=100 PLN
        tax=23.0 PLN
        gross=123.0 PLN

Type Float Altitude
-------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_float_altitude.py`

:English:
    #. Plane altitude is 10.000 ft
    #. Data uses imperial (US) system
    #. Convert to metric (SI) system
    #. Result round to one decimal place
    #. Compare result with "Output" section (see below)

:Polish:
    #. Wysokość lotu samolotem wynosi 10 000 ft
    #. Dane używają systemu imperialnego (US)
    #. Przelicz je na system metryczny (układ SI)
    #. Wynik zaokrąglij do jednego miejsca po przecinku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        altitude=3048.0 m

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 ft = 0.3048 m

Type Float Volume
------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_float_volume.py`

:English:
    #. Bottle volume is 20 Fl Oz
    #. Data uses imperial (US) system
    #. Convert to metric (SI) system
    #. Compare result with "Output" section (see below)

:Polish:
    #. Objętość butelki wynosi 20 Fl Oz
    #. Dane używają systemu imperialnego (US)
    #. Przelicz je na system metryczny (układ SI)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        volume=0.5914688 l

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 Fl Oz = 0.02957344 l

Type Float Distance
-------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_float_distance.py`

:English:
    #. Use code from "Input" section (see below)
    #. Convert units
    #. Instead ``...`` substitute calculated and converted values
    #. Note the number of decimal places
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj jednostki
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości
    #. Zwróć uwagę na ilość miejsc po przecinku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        m = 1337

        print(f'Meters: {...}')
        print(f'Kilometers: {...}')
        print(f'Miles: {...}')
        print(f'Nautical Miles: {...}')
        print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')

:Output:
    .. code-block:: text

        Meters: 1337
        Kilometers: 1.337
        Miles: 0.83
        Nautical Miles: 0.722
        m: 1337, km: 1, mi: 0.8, nm: 0.72

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * 1 km = 1000 m
    * 1 mile = 1609.344 m
    * 1 nautical mile = 1852 m

Type Float Velocity
-------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_float_velocity.py`

:English:
    #. Speed limit is 75 MPH
    #. Data uses imperial (US) system
    #. Convert to metric (SI) system
    #. Speed limit print in KPH (km/h)
    #. Result round to one decimal place

:Polish:
    #. Ograniczenie prędkości wynosi 75 MPH
    #. Dane używają systemu imperialnego (US)
    #. Przelicz je na system metryczny (układ SI)
    #. Ograniczenie prędkości wypisz w KPH (km/h)
    #. Wynik zaokrąglij do jednego miejsca po przecinku

:Output:
    .. code-block:: text

        speed_limit=120.7 km/h

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

Type Float Pressure
-------------------
* Complexity level: medium
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_float_pressure.py`

:English:
    #. Operational pressure of EMU spacesuit: 4.3 PSI
    #. Operational pressure of ORLAN spacesuit: 400 hPa
    #. Calculate operational pressure in kPa for EMU
    #. Calculate operational pressure in PSI for Orlan
    #. Print all results in kPa and PSI rounding to two decimal places
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU (NASA): 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN (Roscosmos): 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Wypisz wszystkie wyniki w kPa oraz PSI zaokrąglając do dwóch miejsc po przecinku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        EMU: 29.65 kPa, 4.30 psi
        Orlan: 40.00 kPa, 5.80 psi

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

.. figure:: img/spacesuits.png
    :width: 50%
    :align: center

    EMU and Orlan

:Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 psi = 6894.757 Pa

Type Float Percent
------------------
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_float_percent.py`

:English:
    #. International Standard Atmosphere (ISA) at sea level is 1013.25 hPa
    #. Calculate partial pressure of Oxygen at sea level
    #. Print ISA and partial O2 pressure in kPa rounding to two decimal places
    #. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    #. Compare result with "Output" section (see below)

:Polish:
    #. International Standard Atmosphere (ISA) na poziomie morza wynosi 1013.25 hPa
    #. Oblicz ciśnienie parcjalne tlenu na poziomie morza
    #. Wypisz ISA oraz ciśnienie parcjalne O2 wyniki w kPa zaokrąglając do dwóch miejsc po przecinku
    #. Aby policzyć ciśnienie parcialne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        International Standard Atmosphere: 101.33 kPa
        O2 partial pressure at sea level: 21.22 kPa

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Type Float Gradient
-------------------
* Complexity level: hard
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/type_float_gradient.py`

:English:
    #. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    #. Print result in meters rounding to two decimal places
    #. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    #. Calculated altitude is pressure at sea level minis oxygen partial pressure divided by gradient
    #. Mind the operator precedence
    #. Compare result with "Output" section (see below)

:Polish:
    #. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wypisz rezultat w metrach zaokrąglając do dwóch miejsc po przecinku
    #. Aby policzyć ciśnienie parcialne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    #. Wyliczona wysokość to ciśnienie atmosferyczne na poziomie morza minus ciśnienie parcialne tlenu podzielone przez gradient
    #. Zwróć uwagę na kolejność wykonywania działań
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        Oxygen starvation altitude: 7088.63 m

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * pressure gradient (decrease) = 11.3 Pa / 1 m
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%
