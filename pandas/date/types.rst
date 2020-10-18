.. _Date and Time Types:

*******************
Date and Time Types
*******************


Timestamp
=========
* subclass of ``datetime.datetime``
* Timezone naive or :ref:`Timezone aware <Date and Time Timezones>`

.. code-block:: python

    import pandas as pd


    pd.Timestamp('1961-04-12')
    # Timestamp('1961-04-12 00:00:00')

    pd.Timestamp('1961-04-12T06:07:00')
    # Timestamp('1961-04-12 06:07:00')

    pd.Timestamp('1961-04-12 6:07')
    # Timestamp('1961-04-12 06:07:00')

.. code-block:: python

    import pandas as pd


    pd.Timestamp('12/4/69')
    # Timestamp('1969-12-04 00:00:00')

    pd.Timestamp('12/4/69, 6:07')
    # Timestamp('1969-12-04 06:07:00')

    pd.Timestamp('12/4/69, 6:07 pm')
    # Timestamp('1969-12-04 18:07:00')

.. code-block:: python
    :caption: 2016-12-31 23:59:60 is a valid date (UTC leap second)

    import pandas as pd


    pd.Timestamp('2016-12-31 23:59:60')
    # Traceback (most recent call last):
    #     ...
    # ValueError: second must be in 0..59


Date Ranges
===========

Period
------
* Read more in :ref:`Date and Time Frequency`

.. code-block:: python

    import pandas as pd


    apollo11 = pd.Period('1969-07-16', '9D')

    apollo11.start_time
    # Timestamp('1969-07-16 00:00:00')

    apollo11.end_time
    # Timestamp('1969-07-24 23:59:59.999999999')

Days in a row
-------------
* Read more in :ref:`Date and Time Frequency`

.. code-block:: python

    import pandas as pd


    pd.date_range('1970-01-01', periods=3, freq='D')
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03'], dtype='datetime64[ns]', freq='D')

    pd.date_range('1970-01-01', periods=3, freq='M')
    # DatetimeIndex(['1970-01-31', '1970-02-28', '1970-03-31'], dtype='datetime64[ns]', freq='M')

    pd.date_range('1970-01-01', periods=3, freq='Y')
    # DatetimeIndex(['1970-12-31', '1971-12-31', '1972-12-31'], dtype='datetime64[ns]', freq='A-DEC')

Days between
------------
.. code-block:: python

    from datetime import datetime
    import pandas as pd


    start = datetime(1969, 7, 16)
    end = datetime(1969, 7, 21)

    pd.date_range(start, end)
    # DatetimeIndex(['1969-07-16', '1969-07-17', '1969-07-18',
    #                '1969-07-19', '1969-07-20', '1969-07-21'],
    #                dtype='datetime64[ns]', freq='D')

Attributes
----------
* Read more in :ref:`Date and Time Frequency`

.. code-block:: python

    import pandas as pd


    space_race = pd.date_range(start='1961-04-12', end='1969-07-21', freq='D')

    space_race.freq
    # <Day>

    space_race.dtype
    # dtype('<M8[ns]')

    space_race.shape
    # (3023,)

    space_race.ndim
    # 1

    len(space_race)
    # 3023

    space_race.array
    # <DatetimeArray>
    # ['1961-04-12 00:00:00', '1961-04-13 00:00:00', '1961-04-14 00:00:00',
    #  '1961-04-15 00:00:00', '1961-04-16 00:00:00', '1961-04-17 00:00:00',
    #  '1961-04-18 00:00:00', '1961-04-19 00:00:00', '1961-04-20 00:00:00',
    #  '1961-04-21 00:00:00',
    #  ...
    #  '1969-07-12 00:00:00', '1969-07-13 00:00:00', '1969-07-14 00:00:00',
    #  '1969-07-15 00:00:00', '1969-07-16 00:00:00', '1969-07-17 00:00:00',
    #  '1969-07-18 00:00:00', '1969-07-19 00:00:00', '1969-07-20 00:00:00',
    #  '1969-07-21 00:00:00']
    # Length: 3023, dtype: datetime64[ns]

    space_race.values
    # array(['1961-04-12T00:00:00.000000000', '1961-04-13T00:00:00.000000000',
    #        '1961-04-14T00:00:00.000000000', ...,
    #        '1969-07-19T00:00:00.000000000', '1969-07-20T00:00:00.000000000',
    #        '1969-07-21T00:00:00.000000000'], dtype='datetime64[ns]')


Assignments
===========
.. todo:: Create assignments
