*******************************
Datetime Parsing and Formatting
*******************************


Date formats
============
* https://en.wikipedia.org/wiki/Date_format_by_country

Date format in USA
------------------
.. code-block:: text
    :caption: Formal date format in USA :cite:`DateFormatUS`

    4/12/61
    April 12, 1961

Date format in Japan
--------------------
.. code-block:: text
    :caption: Formal date format in Japan :cite:`DateFormatJapan`

    20/12/31

Date format in Germany
----------------------
.. code-block:: text
    :caption: Formal date format in Germany

    12.04.1961

Date format in Poland
---------------------
* Which format is a formal standard in Poland?
* https://en.wikipedia.org/wiki/ISO_8601

.. code-block:: text

    12.4.1961
    12.04.1961

    12 IV 1961
    12.IV.1961

    12/4/1961
    12/04/1961

    12 kwietnia 1961
    12 kwiecień 1961


Time formats
============

24 and 12 hour clock
--------------------
* What AM stands for?
* What PM stands for?

.. code-block:: text

    17:00
    5:00 PM

Noon and Midnight
-----------------
* Which time is a midnight?
* Which time is a noon?
* `Confusion at noon and midnight <https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight>`_
* Is 12:00 a noon (in 24h format), or someone just simply forgot to put AM/PM?

.. code-block:: text

    12:00 am
    12:00 pm

    12:00
    24:00

    00:00
    0:00

Times after 24:00
-----------------
* `Times after 24:00 <https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00>`_

.. code-block:: text

    23:59:59
    23:59:60

.. code-block:: text

    24:00
    24:01
    25:00
    27:45
    14:00-30:00

Military time
-------------
* `Military time <https://en.wikipedia.org/wiki/24-hour_clock#Military_time>`_
* `Military time zones <https://en.wikipedia.org/wiki/List_of_military_time_zones>`_

.. code-block:: text

    1200J
    1200Z


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
* "T" separates date and time

.. code-block:: text
    :caption: Date and time

    1961-04-12T06:07:00Z
    1961-04-12T06:07:00.123Z
    1961-04-12T06:07:00.123456Z

Noon and Midnight
-----------------
* "00:00" - midnight, at the beginning of a day
* "24:00" - midnight, at the end of a day (not recommended)
* "2007-04-05T24:00" is equal to "2007-04-06T00:00"

Weeks
-----
.. code-block:: text
    :caption: Note year/month changes during the week

    2009-W01            # First week of 2009
    2009-W01-1          # Monday 29 December 2008
    2009-W53-7          # Sunday 3 January 2010

Timezone
--------
* "Z" (Zulu) means UTC

.. code-block:: text
    :caption: Time zone notation
    :emphasize-lines: 1-3

    <time>UTC
    <time>Z
    <time>±hh:mm
    <time>±hhmm
    <time>±hh

Duration
--------
* Format: ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``

.. csv-table:: Duration format
    :header: "Format", "Designator", "Description"
    :widths: 10, 15, 75

    "``P``", "duration (period)",  "placed at the start of the duration representation"
    "``Y``", "year",  "number of years"
    "``M``", "month",  "number of months"
    "``W``", "week",  "number of weeks"
    "``D``", "day",  "number of days"
    "``T``", "time",  "precedes the time components of the representation"
    "``H``", "hour",  "number of hours"
    "``M``", "minute",  "number of minutes"
    "``S``", "second",  "number of seconds"

.. code-block:: text
    :caption: Example
    :emphasize-lines: 1

    P8Y3M8DT20H49M15S

    # Period of:
    #   8 years
    #   3 months
    #   8 days
    #   20 hours
    #   49 minutes
    #   15 seconds


Date and time parsing and formatting parameters
===============================================
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
* ``%-I`` or ``%_I`` on \*nix systems (macOS, BSD, Linux) to remove leading zero
* ``%#I`` on Windows to remove leading zero
* \*nix: ``%-d``, ``%-H``, ``%-I``, ``%-j``, ``%-m``, ``%-M``, ``%-S``, ``%-U``, ``%-w``, ``%-W``, ``%-y``, ``%-Y``
* Windows: ``%#d``, ``%#H``, ``%#I``, ``%#j``, ``%#m``, ``%#M``, ``%#S``, ``%#U``, ``%#w``, ``%#W``, ``%#y``, ``%#Y``

.. note:: Almost any programming language has very similar date formatting parameters. There are only some minor differences like in JavaScript minutes are ``i``, not ``M``.

.. csv-table:: Date and time parsing and formatting parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.


Date formatting
===============

ISO Format
----------
.. code-block:: python
    :caption: Datetime formatting to ISO format

    from datetime import datetime

    dt = datetime(1969, 7, 21, 2, 56, 15)

    dt.isoformat()
    # 1969-07-21T02:56:15

.. code-block:: python
    :caption: Date formatting to ISO format

    from datetime import date

    d = date(1969, 7, 21)

    d.isoformat()
    # 1969-07-21

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
    # Gagarin launched on 1961-04-12 06:07

Format to string
----------------
.. code-block:: python
    :caption: Datetime formatting as string with ``.strftime()``

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    formatted = gagarin.strftime('%Y-%m-%d %H:%M')

    print(f'Gagarin launched on {formatted}')
    # Gagarin launched on 1961-04-12 06:07


Parsing dates
=============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. code-block:: python
    :caption: Datetime parsing from string

    from datetime import datetime

    sputnik = '4 October 1957, 19:28:34 [UTC]'

    result = datetime.strptime(sputnik, '%d %B %Y, %H:%M:%S [%Z]')
    # datetime.datetime(1957, 10, 4, 19, 28, 34)

    print(result)
    # 1957-10-04 19:28:34

Examples
========
.. code-block:: python

    from datetime import datetime


    log = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'

    date, level, message = log.split(maxsplit=2)
    format = '%Y-%m-%dT%H:%M:%S.%f'
    date = datetime.strptime(date, format)

    print(date)
    # 1969-07-21 02:56:15.123000

    print(level)
    # [WARNING]

    print(message)
    # First step on the Moon


Assignments
===========

Datetime Parse ISO
------------------
* Assignment name: Datetime Parse ISO
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/datetime_parse_iso.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. The date and time is given in ISO format:
    #. Convert it to ``datetime`` object

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dana jest data w formacie ISO
    #. Przedstaw datę jako obiekt ``datetime``

:Input:
    .. code-block:: python

        DATA = '1969-07-21T02:56:15.123Z'

Datetime Parse Local
--------------------
* Assignment name: Datetime Parse Local
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/datetime_parse_local.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Create ``datetime`` object by parsing the given date
    #. Using formatting parameters print the date and time in ISO format
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Podaną datę przekonwertuj do obiektu ``datetime``
    #. Używając parametrów formatujących wyświetl datę i czas w formacie ISO
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = 'April 12, 1961 6:07 local time'

:Output:
    .. code-block:: python

        data: datetime
        # datetime.datetime(1961, 4, 12, 6, 7)

        print(result)
        # 1961-04-12T06:07:00.000000Z

:Hints:
    * Add string ``local time`` to format statement

Datetime Parse US
-----------------
* Assignment name: Datetime Parse US
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/datetime_parse_us.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Using given date and time from below (copy with quotes inside)
    #. Create ``datetime`` object by parsing the date
    #. Using formatting parameters print american short date format
    #. Make sure, that hour is without leading zero
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając podaną poniżej datę i czas (skopiuj z cudzysłowami)
    #. Parsując stwórz obiekt ``datetime``
    #. Używając parametrów formatowania wyświetl datę w formacie amerykańskim krótkim
    #. Upewnij się, że godzina jest bez wiodącego zera
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = '"July 21st, 1969 2:56:15 AM UTC"'

:Output:
    .. code-block:: python

        data: datetime
        # datetime.datetime(1969, 7, 21, 2, 56)

        print(result)
        # 7/21/69 2:56 AM

:Hints:
    * Add quote sign ``"`` like normal text to ``fmt`` parameter of ``.strptime()``
    * Use ``%-I`` or ``%_I`` on \*nix systems (macOS, BSD, Linux) to remove leading zero
    * Use ``%#I`` on Windows to remove leading zero

Datetime Parse Logs
-------------------
* Assignment name: Datetime Parse Logs
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/datetime_parse_logs.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Save input data to file ``apollo11-timeline.log``
    #. Extract ``datetime`` object, level name and message from each line
    #. Collect data to ``result: list[dict]``
    #. Print ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz dane wejściowe do pliku ``apollo11-timeline.log``
    #. Wyciągnij obiekt ``datetime``, poziom logowania oraz wiadomość z każdej linii
    #. Zbierz dane do ``result: list[dict]``
    #. Wyświetl ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python
        :caption: Apollo 11 timeline https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

        DATA = """
            1969-07-14, 21:00:00, INFO, Terminal countdown started
            1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
            1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
            1969-07-16, 13:34:44, WARNING, S-II ignition
            1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
            1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
            1969-07-16, 16:22:13, INFO, Translunar injection
            1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
            1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
            1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
            1969-07-20, 17:44:00, INFO, CSM/LM undocked
            1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
            1969-07-20, 20:10:22, ERROR, LM 1202 alarm
            1969-07-20, 20:14:18, ERROR, LM 1201 alarm
            1969-07-20, 20:17:39, WARNING, LM lunar landing
            1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
            1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
            1969-07-21, 02:56:15, WARNING, That's one small step for [a] man... one giant leap for mankind
            1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
            1969-07-21, 03:15:16, INFO, LMP on lunar surface
            1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
            1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
            1969-07-21, 21:35:00, INFO, CSM/LM docked
            1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
            1969-07-24, 16:21:12, INFO, CM/SM separation
            1969-07-24, 16:35:05, WARNING, Entry
            1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
            1969-07-24, 17:29, INFO, Crew egress
        """

:Output:
    .. code-block:: python

        result  # doctest: +NORMALIZE_WHITESPACE
        [{'date': datetime.datetime(1969, 7, 14, 21, 0),
          'level': 'INFO',
          'message': 'Terminal countdown started'},
         {'date': datetime.datetime(1969, 7, 16, 13, 31, 53),
          'level': 'WARNING',
          'message': 'S-IC engine ignition (#5)'},
         {'date': datetime.datetime(1969, 7, 16, 13, 33, 23),
          'level': 'DEBUG',
          'message': 'Maximum dynamic pressure (735.17 lb/ft^2)'},
         ...]
