*****************
Pandas Set Option
*****************


Display Output
==============

Limited
-------
.. code-block:: python

    import pandas as pd

    pd.set_option('display.max_rows', 10)

.. code-block:: python

    import pandas as pd

    pd.set_option('display.height', 1000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

Unlimited
---------
.. code-block:: python

    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

Using in context
----------------
.. code-block:: python

    import pandas as pd

    with pd.option_context('display.max_rows', 100):
        print(df)

.. code-block:: python

    import pandas as pd

    with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
        print(df)


Assignments
===========
.. todo:: Create assignments
