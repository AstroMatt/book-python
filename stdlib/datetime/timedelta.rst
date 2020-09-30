********************
Datetime Time Deltas
********************


Timedelta object
================
.. code-block:: python
    :caption: Shifting datetime objects

    from datetime import datetime


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    between_dates = armstrong - gagarin

    str(between_dates)                  # '3021 days, 20:49:15'
    between_dates                       # datetime.timedelta(days=3021, seconds=74955)
    between_dates.days                  # 3021
    between_dates.seconds               # 74955
    between_dates.total_seconds()       # 261089355.0 (days * seconds per day + seconds)


Time Shift
==========

Simple Shifts
-------------
.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, datetime


    gagarin = datetime(1961, 4, 12)

    gagarin - timedelta(minutes=15)
    # datetime.datetime(1961, 4, 11, 23, 45)

    gagarin + timedelta(minutes=10)
    # datetime.datetime(1961, 4, 12, 0, 10)


.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    armstrong - timedelta(hours=21)
    # datetime.datetime(1969, 7, 20, 5, 56, 15)

    armstrong + timedelta(hours=5)
    # datetime.datetime(1969, 7, 21, 7, 56, 15)

.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import timedelta, date


    sputnik = date(1957, 10, 4)

    sputnik + timedelta(days=5)
    # datetime.date(1957, 10, 9)

    sputnik - timedelta(days=3)
    # datetime.date(1957, 10, 1)

.. code-block:: python
    :caption: Simple ``timedelta`` shifts

    from datetime import datetime, timedelta


    gagarin = datetime(1961, 4, 12)

    gagarin + timedelta(weeks=2)
    # datetime.datetime(1961, 4, 26, 0, 0)

    gagarin - timedelta(weeks=3)
    # datetime.datetime(1961, 3, 22, 0, 0)

Complex Shifts
--------------
.. code-block:: python
    :caption: Complex ``timedelta`` shifts

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    armstrong - timedelta(days=2, hours=21)
    # datetime.datetime(1969, 7, 18, 5, 56, 15)

.. code-block:: python
    :caption: Complex ``timedelta`` shifts

    from datetime import timedelta, datetime


    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    duration = timedelta(
        weeks=3,
        days=2,
        hours=21,
        minutes=5,
        seconds=12,
        milliseconds=10,
        microseconds=55)
    # datetime.timedelta(days=23, seconds=75912, microseconds=10055)

    between_dates = armstrong - duration
    # datetime.datetime(1969, 6, 27, 5, 51, 2, 989945)

Month Shifts
------------
.. code-block:: python
    :caption: Subtract month from ``datetime``

    from datetime import timedelta, date


    MONTH = timedelta(days=30.436875)

    gagarin = date(1961, 4, 12)
    gagarin - MONTH
    # datetime.date(1961, 3, 13)

.. code-block:: python
    :caption: Subtract month from ``datetime``

    from calendar import monthlen
    from datetime import timedelta, date


    def month_before(dt):
        MONTH = monthlen(dt.year, dt.month)
        return dt - timedelta(days=MONTH)


    gagarin = date(1961, 4, 12)
    month_before(gagarin)
    # datetime.date(1961, 3, 13)


Duration
========
.. code-block:: python
    :caption: Duration between two datetimes

    from datetime import datetime

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 30.436875 * DAY  # Average days a month in solar calendar
    YEAR = 365.2425 * DAY  # Solar calendar

    def duration(dt):
        years, seconds = divmod(dt.total_seconds(), YEAR)
        months, seconds = divmod(seconds, MONTH)
        days, seconds = divmod(seconds, DAY)
        hours, seconds = divmod(dt.seconds, HOUR)
        minutes, seconds = divmod(seconds, MINUTE)

        return {
            'years': int(years),
            'months': int(months),
            'days': int(days),
            'hours': int(hours),
            'minutes': int(minutes),
            'seconds': int(seconds),
        }


    gagarin = datetime(1961, 4, 12, 6, 7)
    armstrong = datetime(1969, 7, 21, 2, 56, 15)

    dt = armstrong - gagarin
    # datetime.timedelta(days=3021, seconds=74955)

    duration(dt)
    # {'years': 8, 'months': 3, 'days': 8, 'hours': 20, 'minutes': 49, 'seconds': 15}


Assignments
===========

Datetime Timedelta Period
-------------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/datetime_timedelta_period.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Given period is the time between Gagarin launch and Armstrong first step on the Moon
    #. Assume:

        * year = 365.2425 days
        * month = 30.436875 days

    #. From current date subtract this period
    #. Print calculated date
    #. How old were you at the given moment?

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Podany jest czas, który upłynął między startem Gagarina a pierwszym krokiem Armstronga na Księżycu
    #. Uwzględnij założenie:

        * rok = 365.2425 dni
        * miesiąc = 30.436875 dni

    #. Od obecnej chwili odejmij ten czas
    #. Wyświetl wyliczoną datę
    #. Ile miałeś wtedy lat?

:Input:
    * 8 years
    * 3 months
    * 8 days
    * 20 hours
    * 49 minutes
    * 15 seconds
