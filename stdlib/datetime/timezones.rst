.. _Stdlib Datetime Timezone:

******************
Datetime Timezone
******************


Rationale
=========
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to local time only when displaying to user
* Computerphile Time & Time Zones :cite:`VideoComputerphileTimeZones`
* Refer to :ref:`Descriptor Timezone Converter` for automated solution
* ``datetime.utcnow()`` - produces timezone naive date!

.. figure:: img/datetime-compare.png

    Comparing datetime works only when all has the same timezone (UTC)

Timezone naive datetimes:

.. code-block:: python

    from datetime import datetime


    datetime(1957, 10, 4, 19, 28, 34)
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    datetime.now()
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    datetime.utcnow()
    # datetime.datetime(1957, 10, 4, 17, 28, 34)

Timezone aware datetime:

.. code-block:: python

    from datetime import datetime, timezone


    datetime.now(tz=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    dt = datetime(1957, 10, 4, 19, 28, 34)
    dt.replace(tzinfo=timezone.utc)
    # datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)

    datetime.utcnow(tz=timezone.utc)
    # Traceback (most recent call last):
    # TypeError: utcnow() takes no keyword arguments

    datetime.utcnow(timezone.utc)
    # Traceback (most recent call last):
    # TypeError: utcnow() takes no arguments (1 given)


IANA Time Zone Database
=======================
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones


Standard Library
================
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library

.. code-block:: python

    from zoneinfo import ZoneInfo
    from datetime import datetime, timedelta


    dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))  # Daylight saving time
    print(dt)
    # 2020-10-31 12:00:00-07:00
    dt.tzname()
    # 'PDT'


    dt += timedelta(days=7)  # Standard time
    print(dt)
    # 2020-11-07 12:00:00-08:00
    print(dt.tzname())
    # PST


``pytz``
========
``pytz`` brings the Olson tz database into Python:

.. code-block:: python

    from pytz import timezone


    timezone('UTC')
    timezone('US/Eastern')
    timezone('Europe/Warsaw')
    timezone('Asia/Almaty')

From naive to local time:

.. code-block:: python

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1969, 7, 21, 2, 56, 15)

    timezone('UTC').localize(my_date)
    # datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=<UTC>)

From naive to local time:

.. code-block:: python

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1961, 4, 12, 6, 7)

    timezone('Asia/Almaty').localize(my_date)
    # datetime.datetime(1961, 4, 12, 6, 7, tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)

From UTC to local time:

.. code-block:: python

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1969, 7, 21, 2, 56, 15, tzinfo=timezone('UTC'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1969, 7, 21, 3, 56, 15, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

Between timezones:

.. code-block:: python

    from datetime import datetime
    from pytz import timezone


    my_date = datetime(1961, 4, 12, 6, 7, tzinfo=timezone('Asia/Almaty'))

    my_date.astimezone(timezone('Europe/Warsaw'))
    # datetime.datetime(1961, 4, 12, 1, 59, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)


Assignments
===========

.. literalinclude:: assignments/datetime_timezone_convert.py
    :caption: :download:`Solution <assignments/datetime_timezone_convert.py>`
    :end-before: # Solution
