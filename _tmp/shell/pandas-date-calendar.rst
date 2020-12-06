.. _Date and Time Calendar:

**********************
Date and Time Calendar
**********************


Business Days
=============
.. code-block:: python

    from pandas.tseries.holiday import USFederalHolidayCalendar
    from pandas.tseries.offsets import CustomBusinessDay


    business_days = CustomBusinessDay(calendar=USFederalHolidayCalendar())

    pd.date_range(start='2019-12-24',end='2019-12-31', freq=business_days)
    # DatetimeIndex(['2019-12-24', '2019-12-26', '2019-12-27',
    #                '2019-12-30', '2019-12-31'],
    #                dtype='datetime64[ns]', freq='C')


Business Hours
==============
.. code-block:: python

    from datetime import datetime, time
    import pandas as pd
    from pandas.tseries.holiday import USFederalHolidayCalendar


    today = datetime(2020, 1, 4, 15, 0, 0)

    BUSINESS_HOURS = pd.offsets.CustomBusinessHour(
        calendar=USFederalHolidayCalendar(),
        start='08:00',
        end=time(16, 0),
        weekmask='Mon Tue Wed Thu Fri')


    today + 5*BUSINESS_HOURS
    # Timestamp('2020-01-06 13:00:00')


Custom Calendar
===============
.. code-block:: python

    import pandas as pd
    from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
    from pandas.tseries.offsets import Day, CustomBusinessDay, CustomBusinessHour


    class PLHolidayCalendar(AbstractHolidayCalendar):
        """
        Custom Holiday calendar for Poland based on
        https://en.wikipedia.org/wiki/Public_holidays_in_Poland
        """
        rules = [
            Holiday('New Years Day', month=1, day=1),
            Holiday('Epiphany', month=1, day=6),
            Holiday('Easter', month=1, day=1, offset=[Easter()]),
            EasterMonday,
            Holiday('May Day', month=5, day=1),
            Holiday('Constitution Day', month=5, day=3),
            Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
            Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
            Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
            Holiday('All Saints Day', month=11, day=1),
            Holiday('Independence Day', month=11, day=11),
            Holiday('Christmas Day', month=12, day=25),
            Holiday('Second Day of Christmastide', month=12, day=26),
        ]


    pl_holidays_2019 = PLHolidayCalendar().holidays(start='2019-01-01', end='2019-12-31')
    # DatetimeIndex(['2019-01-01', '2019-01-06', '2019-04-21', '2019-04-22',
    #                '2019-05-01', '2019-05-03', '2019-06-09', '2019-06-20',
    #                '2019-08-15', '2019-11-01', '2019-11-11', '2019-12-25',
    #                '2019-12-26'],
    #               dtype='datetime64[ns]', freq=None)


    BUSINESS_DAY = CustomBusinessDay(
        calendar=PLHolidayCalendar(),
        weekmask='Mon Tue Wed Thu Fri')

    BUSINESS_HOURS = CustomBusinessHour(
        calendar=PLHolidayCalendar(),
        start='08:00',
        end='16:00',
        weekmask='Mon Tue Wed Thu Fri')


    today = pd.Timestamp('2000-01-01 00:00')
    today + 2*BUSINESS_DAY      # Timestamp('2000-01-04 00:00:00')
    today + 3*BUSINESS_DAY      # Timestamp('2000-01-05 00:00:00')
    today + 4*BUSINESS_DAY      # Timestamp('2000-01-07 00:00:00')
    today + 5*BUSINESS_DAY      # Timestamp('2000-01-10 00:00:00')

    now = pd.Timestamp('2000-01-01 00:00')
    now + 23*BUSINESS_HOURS     # Timestamp('2000-01-05 15:00:00')
    now + 24*BUSINESS_HOURS     # Timestamp('2000-01-06 08:00:00')
    now + 25*BUSINESS_HOURS     # Timestamp('2000-01-11 09:00:00')
    now + 26*BUSINESS_HOURS     # Timestamp('2000-01-11 10:00:00')


Custom mask
===========
.. code-block:: python

    from datetime import datetime
    import pandas as pd


    start = datetime(1970, 12, 1)
    end = datetime(1970, 12, 31)
    weekmask = 'Mon Tue Wed Thu Fri'
    holidays = [datetime(1970, 12, 25), datetime(1970, 12, 26)]

    pd.bdate_range(start, end, freq='C', weekmask=weekmask, holidays=holidays)
    # DatetimeIndex(['1970-12-01', '1970-12-02', '1970-12-03', '1970-12-04',
    #                '1970-12-07', '1970-12-08', '1970-12-09', '1970-12-10',
    #                '1970-12-11', '1970-12-14', '1970-12-15', '1970-12-16',
    #                '1970-12-17', '1970-12-18', '1970-12-21', '1970-12-22',
    #                '1970-12-23', '1970-12-24', '1970-12-28', '1970-12-29',
    #                '1970-12-30', '1970-12-31'],
    #                dtype='datetime64[ns]', freq='C')
