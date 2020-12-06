.. _Date and Time Timezones:

***********************
Date and Time Timezones
***********************


Timezone aware
==============
.. code-block:: python

    import pandas as pd


    gagarin = pd.Timestamp('1961-04-12 12:07:00', tz='Asia/Almaty')

    gagarin.astimezone('UTC')
    # Timestamp('1961-04-12 06:07:00+0000', tz='UTC')

    gagarin.astimezone('Europe/Moscow')
    #Timestamp('1961-04-12 09:07:00+0300', tz='Europe/Moscow')

    gagarin.astimezone('Europe/Warsaw')
    # Timestamp('1961-04-12 07:07:00+0100', tz='Europe/Warsaw')

    gagarin.astimezone('EST')
    # Timestamp('1961-04-12 01:07:00-0500', tz='EST')

    gagarin.astimezone('America/New_York')
    # Timestamp('1961-04-12 01:07:00-0500', tz='America/New_York')

.. code-block:: python

    import pandas as pd


    armstrong = pd.Timestamp('1969-07-21 2:56:15', tz='UTC')

    armstrong.tz_convert('Europe/Warsaw')
    # Timestamp('1969-07-21 03:56:15+0100', tz='Europe/Warsaw')

    armstrong.astimezone('Europe/Warsaw')
    # Timestamp('1969-07-21 03:56:15+0100', tz='Europe/Warsaw')
