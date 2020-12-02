******************
Datetime Timestamp
******************


What is timestamp?
==================
* Seconds since midnight of January 1st, 1970 (1970-01-01 00:00:00 UTC)
* Unix era, also known as "epoch"
* In most systems represented as 32-bit integer
* Max value is 2,147,483,647 (2038-01-19 03:14:07 UTC)
* Min value is -2,147,483,647 (1902-12-13 20:45:53 UTC)
* If you add 1 to max value, you will get overflow to min value


Get current timestamp
=====================
.. code-block:: python
    :caption: Get current timestamp using ``datetime`` module

    from datetime import datetime

    datetime.now().timestamp()
    # 1567298992.679585

.. code-block:: python
    :caption: Get current timestamp using ``time`` module

    import time

    time.time()
    # 1567298992.679617


Convert timestamp to ``datetime``
=================================
.. code-block:: python
    :caption: Convert timestamp to ``datetime``

    from datetime import datetime

    datetime.fromtimestamp(267809220)
    # datetime.datetime(1978, 6, 27, 15, 27)

* JavaScript has timestamp in milliseconds
* To convert from milliseconds we have to divide by 1000

.. code-block:: python
    :caption: Convert JavaScript timestamp to ``datetime``

    from datetime import datetime

    MILLISECONDS = 1000

    datetime.fromtimestamp(267809220000 / MILLISECONDS)
    # datetime.datetime(1978, 6, 27, 17, 27)


Assignments
===========

Datetime Timestamp Limits
-------------------------
* Assignment: Datetime Timestamp Limits
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 1 lines
* Estimated time: 5 min
* Filename: :download:`solution/datetime_timestamp_limits.py`

English:
    #. Use data from "Given" section (see below)
    #. Convert given dates to ``datetime`` objects
    #. Print timestamp for each date
    #. What is special about those dates?

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Przekonwertuj podane daty do obiektów ``datetime``
    #. Wypisz timestamp każdej daty
    #. Co to za daty?

Given:
    .. code-block:: python

        a = '1902-12-13 20:45:53 UTC'
        b = '1970-01-01 00:00:00 UTC'
        c = '2038-01-19 03:14:07 UTC'
