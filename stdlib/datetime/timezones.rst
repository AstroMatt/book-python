******************
Datetime Timezones
******************


Standard Library
================
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to local time only when displaying to user
* Computerphile Time & Time Zones :cite:`VideoComputerphileTimeZones`
* Refer to :ref:`Timezone Conversion` for automated solution

Timezone Naive
--------------
* ``datetime.utcnow()`` - produces timezone naive date!

.. code-block:: python
    :caption: Timezone naive datetimes.

    from datetime import datetime


    datetime(1957, 10, 4, 19, 28, 34)
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    datetime.now()
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    datetime.utcnow()
    # datetime.datetime(1957, 10, 4, 17, 28, 34)

Timezone Aware
--------------
.. code-block:: python
    :caption: Timezone aware datetime

    from datetime import datetime, timezone


    datetime.now(tz=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    dt = datetime(1957, 10, 4, 19, 28, 34)
    dt.replace(tzinfo=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    datetime.utcnow(tz=timezone.utc)
    # TypeError: utcnow() takes no keyword arguments

    datetime.utcnow(timezone.utc)
    # TypeError: utcnow() takes no arguments (1 given)

``pytz``
========

List of Timezones
-----------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones

.. code-block:: python
    :caption: ``pytz`` brings the Olson tz database into Python.

    from pytz import timezone


    timezone('UTC')
    timezone('US/Eastern')
    timezone('Europe/Warsaw')
    timezone('Asia/Almaty')

From Naive to UTC
-----------------
.. code-block:: python
    :caption: From naive to local time

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1969, 7, 21, 2, 56, 15)

    timezone('UTC').localize(my_date)
    # datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=<UTC>)

From Naive to Local
-------------------
.. code-block:: python
    :caption: From naive to local time

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1961, 4, 12, 6, 7)

    timezone('Asia/Almaty').localize(my_date)
    # datetime.datetime(1961, 4, 12, 6, 7, tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)

From UTC to local time
----------------------
.. code-block:: python
    :caption: From UTC to local time

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1969, 7, 21, 2, 56, 15, tzinfo=timezone('UTC'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1969, 7, 21, 3, 56, 15, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

Between timezones
-----------------
* Problem with precision

.. code-block:: python
    :caption: Between timezones

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1961, 4, 12, 6, 7, tzinfo=timezone('Asia/Almaty'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1961, 4, 12, 1, 59, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)


Assignments
===========

Datetime Timezone Convert
-------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/datetime_timezone_convert.py`

:English:
    #. Use data from "Input" section (see below)
    #. Convert given date to ``datetime`` objects
    #. What was the time in:

        * London, United Kingdom
        * Moscow, Russian Federation
        * Warsaw, Poland
        * Tokyo, Japan
        * Sydney, Australia
        * Auckland, New Zealand

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj podaną datę do obiektu ``datetime``
    #. Wyświetl datę jaka była w:

        * London, Wielka Brytania
        * Moscow, Rosja
        * Warsaw, Polska
        * Tokyo, Japan
        * Sydney, Australia
        * Auckland, Nowa Zelandia

:Input:
    .. code-block:: python

        DATA = '1969-07-21 02:56:15 UTC'

:Extra Task:
    #. Kosmodrom Bajkonur, Kazachstan
    #. Cape Canaveral, FL, USA
    #. Houston, TX, USA
    #. New York, USA
    #. South Pole
    #. North Pole
