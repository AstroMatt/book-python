**********************
DataFrame Aggregations
**********************


.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-en.csv'

    df = pd.read_csv(DATA, parse_dates=['date'])
    df.drop(columns='index', inplace=True)

.. csv-table:: Data
    :header: Column, Description
    :widths: 10, 90

    "date", "The date and time of the entry"
    "duration", "The duration (in seconds) for each call, the amount of data (in MB) for each data entry, and the number of texts sent (usually 1) for each sms entry"
    "item", "A description of the event occurring – can be one of call, sms, or data"
    "month", "The billing month that each entry belongs to – of form ``YYYY-MM``"
    "network", "The mobile network that was called/texted for each entry"
    "network_type", "Whether the number being called was a mobile, international ('world'), voicemail, landline, or other ('special') number."


.. note:: Source [PandasAggregations]_


Single Statistic
================
.. code-block:: python
    :caption: The groupby output will have an index or multi-index on rows corresponding to your chosen grouping variables. To avoid setting this index, pass ``as_index=False`` to the groupby operation.

    df.groupby('month', as_index=False).agg({'duration': 'sum'})
    #      month   duration
    # 0  2014-11  26639.441
    # 1  2014-12  14641.870
    # 2  2015-01  18223.299
    # 3  2015-02  15522.299
    # 4  2015-03  22750.441


Multiple Statistics per Group
=============================
.. code-block:: python
    :caption: Group the data frame by month and item and extract a number of stats from each group

    df.groupby(['month', 'item']).agg({

        # Sum duration per group
        'duration': 'sum',

        # get the count of networks
        'network_type': 'count',

        # get the first date per group
        'date': 'first'
    })
    # month    item   duration  network_type  date
    # 2014-11  call  25547.000           107  2014-10-15 06:58:00
    #          data    998.441            29  2014-10-15 06:58:00
    #          sms      94.000            94  2014-10-16 22:18:00
    # 2014-12  call  13561.000            79  2014-11-14 17:24:00
    #          data   1032.870            30  2014-11-13 06:58:00
    #          sms      48.000            48  2014-11-14 17:28:00
    # 2015-01  call  17070.000            88  2014-12-15 20:03:00
    #          data   1067.299            31  2014-12-13 06:58:00
    #          sms      86.000            86  2014-12-15 19:56:00
    # 2015-02  call  14416.000            67  2015-01-15 10:36:00
    #          data   1067.299            31  2015-01-13 06:58:00
    #          sms      39.000            39  2015-01-15 12:23:00
    # 2015-03  call  21727.000            47  2015-02-12 20:15:00
    #          data    998.441            29  2015-02-13 06:58:00
    #          sms      25.000            25  2015-02-19 18:46:00

.. code-block:: python
    :caption: Define the aggregation procedure outside of the groupby operation

    df.groupby('month').agg({
        'duration': 'sum',
        'date': lambda x: max(x) - 1
    })
    # Traceback (most recent call last):
    # ValueError: Cannot add integral value to Timestamp without freq.


Applying multiple functions to columns in groups
================================================
.. code-block:: python
    :caption: Group the data frame by month and item and extract a number of stats from each group

    df.groupby(['month', 'item']).agg({

        # Find the min, max, and sum of the duration column
        'duration': ['min', 'max', 'sum'],

        # find the number of network type entries
        'network_type': 'count',

        # minimum, first, and number of unique dates
        'date': ['min', 'first', 'nunique']
    })
    #                            duration          network_type                     date
    # month    item     min        max        sum      count     min                  first                nunique
    # 2014-11  call   1.000   1940.000  25547.000        107     2014-10-15 06:58:00  2014-10-15 06:58:00      104
    #          data  34.429     34.429    998.441         29     2014-10-15 06:58:00  2014-10-15 06:58:00       29
    #          sms    1.000      1.000     94.000         94     2014-10-16 22:18:00  2014-10-16 22:18:00       79
    # 2014-12  call   2.000   2120.000  13561.000         79     2014-11-14 17:24:00  2014-11-14 17:24:00       76
    #          data  34.429     34.429   1032.870         30     2014-11-13 06:58:00  2014-11-13 06:58:00       30
    #          sms    1.000      1.000     48.000         48     2014-11-14 17:28:00  2014-11-14 17:28:00       41
    # 2015-01  call   2.000   1859.000  17070.000         88     2014-12-15 20:03:00  2014-12-15 20:03:00       84
    #          data  34.429     34.429   1067.299         31     2014-12-13 06:58:00  2014-12-13 06:58:00       31
    #          sms    1.000      1.000     86.000         86     2014-12-15 19:56:00  2014-12-15 19:56:00       58
    # 2015-02  call   1.000   1863.000  14416.000         67     2015-01-15 10:36:00  2015-01-15 10:36:00       67
    #          data  34.429     34.429   1067.299         31     2015-01-13 06:58:00  2015-01-13 06:58:00       31
    #          sms    1.000      1.000     39.000         39     2015-01-15 12:23:00  2015-01-15 12:23:00       27
    # 2015-03  call   2.000  10528.000  21727.000         47     2015-02-12 20:15:00  2015-02-12 20:15:00       47
    #          data  34.429     34.429    998.441         29     2015-02-13 06:58:00  2015-02-13 06:58:00       29
    #          sms    1.000      1.000     25.000         25     2015-02-19 18:46:00  2015-02-19 18:46:00       17


Named Aggregations
==================
.. code-block:: python
    :caption: Named Aggregations

    df[df['item'] == 'call'].groupby('month').agg(

        # Get max of the duration column for each group
        max_duration=('duration', 'max'),

        # Get min of the duration column for each group
        min_duration=('duration', 'min'),

        # Get sum of the duration column for each group
        total_duration=('duration', 'sum'),

        # Apply a lambda to date column
        num_days=('date', lambda x: (max(x) - min(x)).days)
    )
    #   month  max_duration  min_duration  total_duration  num_days
    # 2014-11        1940.0           1.0         25547.0        28
    # 2014-12        2120.0           2.0         13561.0        30
    # 2015-01        1859.0           2.0         17070.0        30
    # 2015-02        1863.0           1.0         14416.0        25
    # 2015-03       10528.0           2.0         21727.0        19

.. code-block:: python

    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-en.csv'

    df = pd.read_csv(DATA, parse_dates=['date'])
    df.drop(columns='index', inplace=True)

    df.groupby(['month', 'item']).agg(
        duration_count=('duration', 'count'),
        duration_sum=('duration', 'sum'),
        duration_min=('duration', 'min'),
        duration_max=('duration', 'max'),
        duration_mean=('duration', 'mean'),
        duration_median=('duration', 'median'),
        first=('date', 'first'),
        last=('date', 'last'),
    )

Renaming index
==============
* using ``droplevel`` and ``ravel``
* Dictionary ``groupby`` format is deprecated

.. code-block:: python
    :caption: Drop the top level (using ``.droplevel()``) of the newly created multi-index on columns using

    grouped = df.groupby('month').agg({'duration': ['min', 'max', 'mean']})
    # duration
    #   month  min      max        mean
    # 2014-11  1.0   1940.0  115.823657
    # 2014-12  1.0   2120.0   93.260318
    # 2015-01  1.0   1859.0   88.894141
    # 2015-02  1.0   1863.0  113.301453
    # 2015-03  1.0  10528.0  225.251891

    grouped.columns = grouped.columns.droplevel(level=0)
    #   month  min      max        mean
    # 2014-11  1.0   1940.0  115.823657
    # 2014-12  1.0   2120.0   93.260318
    # 2015-01  1.0   1859.0   88.894141
    # 2015-02  1.0   1863.0  113.301453
    # 2015-03  1.0  10528.0  225.251891

    grouped.rename(columns={
        'min': 'min_duration',
        'max': 'max_duration',
        'mean': 'mean_duration'
    }, inplace=True)
    #   month  min_duration  max_duration  mean_duration
    # 2014-11           1.0        1940.0     115.823657
    # 2014-12           1.0        2120.0      93.260318
    # 2015-01           1.0        1859.0      88.894141
    # 2015-02           1.0        1863.0     113.301453
    # 2015-03           1.0       10528.0     225.251891

    grouped.head()

.. code-block:: python
    :caption: Quick renaming of grouped columns from the groupby() multi-index can be achieved using the ravel() function.

    grouped = df.groupby('month').agg({'duration': ['min', 'max', 'mean']})
    # duration
    #   month  min      max        mean
    # 2014-11  1.0   1940.0  115.823657
    # 2014-12  1.0   2120.0   93.260318
    # 2015-01  1.0   1859.0   88.894141
    # 2015-02  1.0   1863.0  113.301453
    # 2015-03  1.0  10528.0  225.251891

.. code-block:: python
    :caption: Using ravel, and a string join, we can create better names for the columns:

    grouped.columns = ['_'.join(x) for x in grouped.columns.ravel()]
    #   month  min_duration  max_duration  mean_duration
    # 2014-11           1.0        1940.0     115.823657
    # 2014-12           1.0        2120.0      93.260318
    # 2015-01           1.0        1859.0      88.894141
    # 2015-02           1.0        1863.0     113.301453
    # 2015-03           1.0       10528.0     225.251891


Assignments
===========
.. todo:: Create assignments


References
==========
.. [PandasAggregations] Lynn, Shane. Summarising, Aggregating, and Grouping data in Python Pandas. https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/ Access date: 2019-12-03. 2019.
