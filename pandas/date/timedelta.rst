********************
Date and Time Shifts
********************


Timedelta
=========
* Represents a duration, the difference between two dates or times
* Difference expressed in: days, hours, minutes, seconds
* Similar to ``datetime.timedelta`` from the standard library
* Can be both positive and negative
* https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html#timedelta-data

.. code-block:: python

    import pandas as pd


    pd.Timedelta('1 day')
    # Timedelta('1 days 00:00:00')

    pd.Timedelta(days=1)
    # Timedelta('1 days 00:00:00')

.. code-block:: python

    import pandas as pd


    feb = pd.Timestamp('2001-02-28')
    mar = pd.Timestamp('2001-03-01')

    feb + pd.Timedelta(days=1)
    # Timestamp('2001-03-01 00:00:00')

    mar - pd.Timedelta(days=1)
    # Timestamp('2001-02-28 00:00:00')

.. code-block:: python

    import pandas as pd


    feb = pd.Timestamp('2000-02-28')
    mar = pd.Timestamp('2000-03-01')

    feb + pd.Timedelta(days=1)
    # Timestamp('2000-02-29 00:00:00')

    feb + pd.Timedelta(days=2)
    # Timestamp('2000-03-01 00:00:00')

    mar - pd.Timedelta(days=1)
    # Timestamp('2000-02-29 00:00:00')

.. code-block:: python
    :caption: Leap second has not been added

    import pandas as pd


    leap = pd.Timestamp('2016-12-31 23:59:59')

    leap + pd.Timedelta(seconds=1)
    # Timestamp('2017-01-01 00:00:00')


DateOffset
==========
* A relative time duration that respects calendar arithmetic
* If a date is Sat then adding a ``Bday`` will return the next Monday (next Business day) instead of a Saturday
* Test if a date is in the ``DateOffset().onOffset(date)``

.. code-block:: python

    import pandas as pd


    first_step = pd.Timestamp('1969-07-21 02:56:15')

    first_step + pd.DateOffset(months=3)
    # Timestamp('1969-10-21 02:56:15')

.. code-block:: python

    import pandas as pd


    epoch = pd.Timestamp('1970-01-01 00:00:00')

    epoch + pd.DateOffset(month=3)
    # Timestamp('1970-03-01 00:00:00')


.. code-block:: python

    import pandas as pd


    mar = pd.Timestamp('1970-03-01 00:00:00')

    mar - pd.DateOffset(days=1)
    # Timestamp('1970-02-28 00:00:00')
