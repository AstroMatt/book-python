***************
DataFrame Query
***************


Rationale
=========
.. code-block:: python

    df[df['sales'] > 50000]
    df.query('sales > 50000')

.. figure:: img/df-query.png
    :width: 90%
    :align: center

    Pandas query expression [sharpsightlabs]_


Query
=====
.. code-block:: python

    import pandas as pd

    df = pd.DataFrame({
        'name': ['William','Emma','Sofia','Markus','Edward','Thomas','Ethan','Olivia','Arun','Anika','Paulo'],
        'region': ['East','North','East','South','West','West','South','West','West','East','South'],
        'sales': [50000,52000,90000,34000,42000,72000,49000,55000,67000,65000,67000],
        'expenses': [42000,43000,50000,44000,38000,39000,42000,60000,39000,44000,45000]})

    df
    #        name region  sales  expenses
    # 0   William   East  50000     42000
    # 1      Emma  North  52000     43000
    # 2     Sofia   East  90000     50000
    # 3    Markus  South  34000     44000
    # 4    Edward   West  42000     38000
    # 5    Thomas   West  72000     39000
    # 6     Ethan  South  49000     42000
    # 7    Olivia   West  55000     60000
    # 8      Arun   West  67000     39000
    # 9     Anika   East  65000     44000
    # 10    Paulo  South  67000     45000

.. code-block:: python
    :caption: Subset a pandas dataframe based on a numeric variable

    df.query('sales > 60000')
    #       name region  sales  expenses
    # 2    Sofia   East  90000     50000
    # 5   Thomas   West  72000     39000
    # 8     Arun   West  67000     39000
    # 9    Anika   East  65000     44000
    # 10   Paulo  South  67000     45000

.. code-block:: python
    :caption: Select rows based on a categorical variable

    df.query('region == "East"')
    #       name region  sales
    # 0  William   East  50000
    # 2    Sofia   East  90000
    # 9    Anika   East  65000

.. code-block:: python
    :caption: Subset a dataframe by index

    df.query('index < 3')
    #       name region  sales  expenses
    # 0  William   East  50000     42000
    # 1     Emma  North  52000     43000
    # 2    Sofia   East  90000     50000

.. code-block:: python
    :caption: Every odd index

    df.query('index%2 == 1')
    #          name region  sales  expenses
    # 1    Emma  North  52000     43000
    # 3  Markus  South  34000     44000
    # 5  Thomas   West  72000     39000
    # 7  Olivia   West  55000     60000
    # 9   Anika   East  65000     44000

.. code-block:: python
    :caption: Subset a pandas dataframe by comparing two columns

    df.query('sales < expenses')
    #      name region  sales  expenses
    # 3  Markus  South  34000     44000
    # 7  Olivia   West  55000     60000

.. code-block:: python
    :caption: Subset a pandas dataframe with multiple conditions

    df.query('(sales > 50000) and (region in ["East", "West"])')
    #          name region  sales  expenses
    # 2   Sofia   East  90000     50000
    # 5  Thomas   West  72000     39000
    # 7  Olivia   West  55000     60000
    # 8    Arun   West  67000     39000
    # 9   Anika   East  65000     44000

.. code-block:: python
    :caption: Reference local variables inside of query

    mean = df['sales'].mean()

    mean
    # 58454.545

    df.query('sales > @mean')
    #       name region  sales  expenses
    # 2    Sofia   East  90000     50000
    # 5   Thomas   West  72000     39000
    # 8     Arun   West  67000     39000
    # 9    Anika   East  65000     44000
    # 10   Paulo  South  67000     45000

.. code-block:: python
    :caption: Modify a dataframe in place

    df2 = df.copy()
    df2.query('index < 5', inplace = True)

    print(df2)
    #       name region  sales  expenses
    # 0  William   East  50000     42000
    # 1     Emma  North  52000     43000
    # 2    Sofia   East  90000     50000
    # 3   Markus  South  34000     44000
    # 4   Edward   West  42000     38000


References
==========
* Source: https://www.sharpsightlabs.com/blog/pandas-query/

.. [sharpsightlabs] https://www.sharpsightlabs.com/blog/pandas-query/
