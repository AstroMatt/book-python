**********************
Parsing and Formatting
**********************


Date and time formats
=====================
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Date formats
------------
* https://en.wikipedia.org/wiki/Date_format_by_country

Formal date format in USA
^^^^^^^^^^^^^^^^^^^^^^^^^
* https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States

.. code-block:: text
    :caption: Formal date format in USA

    4/12/61
    April 12, 1961

Formal date format in Japan
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* https://en.wikipedia.org/wiki/Date_and_time_notation_in_Japan#Date

.. code-block:: text
    :caption: Formal date format in Japan

    20/12/31

Formal date format in Germany
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text
    :caption: Formal date format in Germany

    12.4.1961
    12.04.1961

Formal date format in Poland
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Which format is a formal standard in Poland?
* https://en.wikipedia.org/wiki/ISO_8601

.. code-block:: text

    12.4.1961
    12.04.1961

.. code-block:: text

    12 IV 1961
    12.IV.1961

.. code-block:: text

    12/4/1961
    12/04/1961

.. code-block:: text

    12 kwietnia 1961
    12 kwiecień 1961

Time formats
------------

24 and 12 hour clock
^^^^^^^^^^^^^^^^^^^^
* What AM stands for?
* What PM stands for?
* Is 12:00 a noon, or someone just simply forgot to put AM/PM?

.. code-block:: text

    17:00
    5:00 PM
    5:00

Noon and Midnight
^^^^^^^^^^^^^^^^^
* Which time is a midnight?
* Which time is a noon?
* `Confusion at noon and midnight <https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight>`_

.. code-block:: text

    12:00 am
    12:00 pm

.. code-block:: text

    12:00
    24:00

.. code-block:: text

    00:00
    0:00

Are those times correct?
^^^^^^^^^^^^^^^^^^^^^^^^
* `Times after 24:00 <https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00>`_
* Military `time <https://en.wikipedia.org/wiki/24-hour_clock#Military_time>`_ and `timezones <https://en.wikipedia.org/wiki/List_of_military_time_zones>`_

.. code-block:: text

    23:59:59
    23:59:60

.. code-block:: text

    24:00
    24:01
    25:00
    27:45
    14:00-30:00

.. code-block:: text

    1200J


ISO 8601 Standard
=================
* https://en.wikipedia.org/wiki/ISO_8601

Dates
-----
.. code-block:: text

   1961-04-12

Date and time
-------------
* "Z" (Zulu) means UTC

.. code-block:: text

    1961-04-12T06:07:00Z

* Date and time with milliseconds:

.. code-block:: text

    1961-04-12T06:07:00.123Z

* Date and time with microseconds:

.. code-block:: text

    1961-04-12T06:07:00.123456Z

Noon and Midnight
^^^^^^^^^^^^^^^^^
* The notation "00:00" is used at the beginning of a calendar day and is the more frequently used.
* At the end of a day use "24:00".
* "2007-04-05T24:00" is the same as "2007-04-06T00:00"

Weeks
-----
* Monday 29 December 2008 is written "2009-W01-1"
* Sunday 3 January 2010 is written "2009-W53-7"

.. code-block:: text

    2009-W01

.. code-block:: text

    2009-W53-7

Timezone
--------
* "Z" (Zulu) means UTC

.. code-block:: text

    <time>Z
    <time>±hh:mm
    <time>±hhmm
    <time>±hh

Duration
--------
* ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``:

    - ``P`` is the duration designator (for period) placed at the start of the duration representation.
    - ``Y`` is the year designator that follows the value for the number of years.
    - ``M`` is the month designator that follows the value for the number of months.
    - ``W`` is the week designator that follows the value for the number of weeks.
    - ``D`` is the day designator that follows the value for the number of days.
    - ``T`` is the time designator that precedes the time components of the representation.
    - ``H`` is the hour designator that follows the value for the number of hours.
    - ``M`` is the minute designator that follows the value for the number of minutes.
    - ``S`` is the second designator that follows the value for the number of seconds.

.. code-block:: text

    "P3Y6M4DT12H30M5S" represents a duration of "three years, six months, four days, twelve hours, thirty minutes, and five seconds".


Table of date and time parsing and formatting parameters
========================================================
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv


Date formatting
===============

``f-string`` formatting
-----------------------
.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)

    print(f'Gagarin launched on {gagarin:%Y-%m-%d}')
    # Gagarin launched on 1961-04-12

.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)

    print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
    # Gagarin launched on 1961-04-12 06:07

.. code-block:: python
    :caption: Datetime formatting as string with ``f'...'``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    format = '%Y-%m-%d %H:%M'

    print(f'Gagarin launched on {gagarin:{format}}')
    # Gagarin launched on 1961-04-12  06:07

Format to string
----------------
.. code-block:: python
    :caption: Datetime formatting as string with ``.strftime()``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    formatted = gagarin.strftime('%Y-%m-%d %H:%M')

    print(f'Gagarin launched on {formatted}')
    # Gagarin launched on 1961-04-12 06:07

ISO Format
----------
.. code-block:: python
    :caption: Datetime formatting to ISO format

    from datetime import datetime

    dt = datetime(1969, 7, 21, 14, 56, 15)

    dt.isoformat()
    # 1969-07-21T14:56:15

.. code-block:: python
    :caption: Date formatting to ISO format

    from datetime import date

    d = date(1969, 7, 21)

    d.isoformat()
    # 1969-07-21


Parsing dates
=============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. code-block:: python
    :caption: Datetime parsing from string

    from datetime import datetime

    sputnik = '4 October 1957, 19:28:34 [UTC]'

    out = datetime.strptime(sputnik, '%d %B %Y, %H:%M:%S [%Z]')
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    print(out)
    # 1957-10-04 19:28:34


Assignments
===========

From ISO date format
--------------------
* Filename: ``datetime_from_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Input data: :numref:`listing-time-from-iso`

#. Przedstaw datę jako obiekt ``datetime``

.. code-block:: text
    :name: listing-time-from-iso
    :caption: Convert ``str`` from ISO date format to ``datetime`` objects

    1969-07-21T14:56:15.123Z

To ISO date format
------------------
* Filename: ``datetime_to_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Datę:

    .. code-block:: python

        datetime.datetime(1961, 4, 12, 6, 7, 0, 123456)

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl w formacie ISO datę i czas, tj.:

    .. code-block:: text

        "Rok-Miesiąc-DzieńTGodzina:Minuta:Sekunda.UłamkiSekundZ"
        1961-04-12T06:07:00.123456

#. Wyświetl w formacie ISO samą datę, tj. bez czasu:

    .. code-block:: text

        "Rok-Miesiąc-Dzień"
        1961-04-12

US date and time format
-----------------------
* Filename: ``datetime_from_us.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Rozczytaj datę z formatu amerykańskiego długiego (skopiuj z cudzysłowami):

    .. code-block:: python

        gagarin = '"April 12, 1961 06:07:00 AM local time"'

#. Wyświetl datę w formacie amerykańskim krótkim:

    .. code-block:: text

        "Miesiąc/Dzień/Rok Godzina:Minuta AM/PM"
        04/12/61 06:07 AM

:Hint:
    * Wpisz "local time" jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Wpisz znaki cudzysłowia ``"`` jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
