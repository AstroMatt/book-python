**************
DataFrame Join
**************


.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df1999 = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-29', periods=3),
        data = np.random.randn(3, 4))

    df1999
    #              Morning      Noon   Evening  Midnight
    # 1999-12-29  1.764052  0.400157  0.978738  2.240893
    # 1999-12-30  1.867558 -0.977278  0.950088 -0.151357
    # 1999-12-31 -0.103219  0.410599  0.144044  1.454274

    df2000 = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('2000-01-01', periods=3),
        data = np.random.randn(3, 4))

    #              Morning      Noon   Evening  Midnight
    # 2000-01-01  0.761038  0.121675  0.443863  0.333674
    # 2000-01-02  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-03 -2.552990  0.653619  0.864436 -0.742165


Concatenate
===========
* Useful for merging data from two files or datasources

.. code-block:: python

    pd.concat([df1999, df2000])
    #              Morning      Noon   Evening  Midnight
    # 1999-12-29  1.764052  0.400157  0.978738  2.240893
    # 1999-12-30  1.867558 -0.977278  0.950088 -0.151357
    # 1999-12-31 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-01  0.761038  0.121675  0.443863  0.333674
    # 2000-01-02  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-03 -2.552990  0.653619  0.864436 -0.742165

Append
======
* jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
* Resulting ``DataFrame`` will have auto-incremented indexes

.. code-block:: python

    df1999.append(df2000)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-29  1.764052  0.400157  0.978738  2.240893
    # 1999-12-30  1.867558 -0.977278  0.950088 -0.151357
    # 1999-12-31 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-01  0.761038  0.121675  0.443863  0.333674
    # 2000-01-02  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-03 -2.552990  0.653619  0.864436 -0.742165

    df1999.append(df2000, ignore_index=True)
    #     Morning      Noon   Evening  Midnight
    # 0  1.764052  0.400157  0.978738  2.240893
    # 1  1.867558 -0.977278  0.950088 -0.151357
    # 2 -0.103219  0.410599  0.144044  1.454274
    # 3  0.761038  0.121675  0.443863  0.333674
    # 4  1.494079 -0.205158  0.313068 -0.854096
    # 5 -2.552990  0.653619  0.864436 -0.742165

.. code-block:: python
    :caption: Add Row

    import pandas as pd

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32

    df.append({'A': 77, 'B': 88, 'C': 99})
    # TypeError: Can only append a Series if ignore_index=True or if the Series has a name

    df.append({'A': 77, 'B': 88, 'C': 99}, ignore_index=True)
    #     A   B   C
    # 0  10  20  30
    # 1  11  21  31
    # 2  12  22  32
    # 3  77  88  99

.. code-block:: python

    import pandas as pd

    simple = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    new = pd.DataFrame([
        {'A': 13, 'B': 23, 'C': 33},
        {'A': 13, 'B': 23, 'C': 33},
        {'A': 13, 'B': 23, 'C': 33},
    ])

    simple.append(new)
    simple.append(new, ignore_index=True)

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)


    temp = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=2),
        data = np.random.randn(2, 4))

    temp
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.532779  1.469359  0.154947  0.378163
    # 1999-12-31 -0.887786 -1.980796 -0.347912  0.156349


    new1 = pd.DataFrame([
        {'Morning': 1, 'Noon': 2, 'Evening': 3, 'Midnight': 4}])

    temp.append(new1)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.532779  1.469359  0.154947  0.378163
    # 1999-12-31 -0.887786 -1.980796 -0.347912  0.156349
    # 0                    1.000000  2.000000  3.000000  4.000000

    temp.append(new1, ignore_index=True)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.532779  1.469359  0.154947  0.378163
    # 1999-12-31 -0.887786 -1.980796 -0.347912  0.156349
    # 7  1.000000  2.000000  3.000000  4.000000


    new2 = pd.DataFrame(
        data = [{'Morning': 1, 'Noon': 2, 'Evening': 3, 'Midnight': 4}],
        index= [pd.Timestamp('2000-01-01')])

    temp.append(new2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.532779  1.469359  0.154947  0.378163
    # 1999-12-31 -0.887786 -1.980796 -0.347912  0.156349
    # 2000-01-01  1.000000  2.000000  3.000000  4.000000

    temp.append(new2, ignore_index=True)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.532779  1.469359  0.154947  0.378163
    # 1999-12-31 -0.887786 -1.980796 -0.347912  0.156349
    # 7  1.000000  2.000000  3.000000  4.000000


Merge
=====
* Merge DataFrame or named Series objects with a database-style join.
* The join is done on columns or indexes.
* If joining columns on columns, the DataFrame indexes will be ignored.
* Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on.

.. code-block:: python

    first_names = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'first_name': ['Mark', 'Jan', 'Ivan', 'Melissa']})

    last_names = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'last_name': ['Watney', 'Twardowski', 'Ivanovic', 'Lewis']})

    first_names
    #    id first_name
    # 0   1       Mark
    # 1   2        Jan
    # 2   3       Ivan
    # 3   4    Melissa

    last_names
    #    id   last_name
    # 0   1      Watney
    # 1   2  Twardowski
    # 2   3    Ivanovic
    # 3   4       Lewis

.. code-block:: python

    first_names.merge(last_names)
    #    id first_name   last_name
    # 0   1       Mark      Watney
    # 1   2        Jan  Twardowski
    # 2   3       Ivan    Ivanovic
    # 3   4    Melissa       Lewis

    first_names.merge(last_names, on='id')
    #    id first_name   last_name
    # 0   1       Mark      Watney
    # 1   2        Jan  Twardowski
    # 2   3       Ivan    Ivanovic
    # 3   4    Melissa       Lewis

    first_names.merge(last_names, left_on='id', right_on='id')
    #    id first_name   last_name
    # 0   1       Mark      Watney
    # 1   2        Jan  Twardowski
    # 2   3       Ivan    Ivanovic
    # 3   4    Melissa       Lewis

    first_names.merge(last_names).set_index('id')
    #    first_name   last_name
    # id
    # 1        Mark      Watney
    # 2         Jan  Twardowski
    # 3        Ivan    Ivanovic
    # 4     Melissa       Lewis

.. code-block:: python

    df1999.merge(df2000)
    # Empty DataFrame
    # Columns: [Morning, Noon, Evening, Midnight]
    # Index: []

    df1999.merge(df2000, right_index=True, left_index=True, how='left', suffixes=('_1999', '_2000'))
    #             Morning_1999  Noon_1999  ...  Evening_2000  Midnight_2000
    # 1999-12-29      1.764052   0.400157  ...           NaN            NaN
    # 1999-12-30      1.867558  -0.977278  ...           NaN            NaN
    # 1999-12-31     -0.103219   0.410599  ...           NaN            NaN
    # [3 rows x 8 columns]

    df1999.merge(df2000, how='outer')
    #     Morning      Noon   Evening  Midnight
    # 0  1.764052  0.400157  0.978738  2.240893
    # 1  1.867558 -0.977278  0.950088 -0.151357
    # 2 -0.103219  0.410599  0.144044  1.454274
    # 3  0.761038  0.121675  0.443863  0.333674
    # 4  1.494079 -0.205158  0.313068 -0.854096
    # 5 -2.552990  0.653619  0.864436 -0.742165


Join
====
* Join columns of another DataFrame.
* Join columns with other DataFrame either on index or on a key column.
* Efficiently join multiple DataFrame objects by index at once by passing a list.
* ``rfuffix`` - If two columns has the same name, add suffix to right
* ``lfuffix`` - If two columns has the same name, add suffix to left

.. figure:: img/pandas-df-join.png
    :width: 75%
    :align: center

    Pandas DataFrame Joins

.. code-block:: python

    first_names = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'first_name': ['Mark', 'Jan', 'Ivan', 'Melissa']})

    last_names = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'last_name': ['Watney', 'Twardowski', 'Ivanovic', 'Lewis']})

    first_names
    #    id first_name
    # 0   1       Mark
    # 1   2        Jan
    # 2   3       Ivan
    # 3   4    Melissa

    last_names
    #    id   last_name
    # 0   1      Watney
    # 1   2  Twardowski
    # 2   3    Ivanovic
    # 3   4       Lewis

.. code-block:: python
    :caption: Join DataFrames using their indexes.

    first_names.join(last_names, lsuffix='_fname', rsuffix='_lname')
    #    id_fname first_name  id_lname   last_name
    # 0         1       Mark         1      Watney
    # 1         2        Jan         2  Twardowski
    # 2         3       Ivan         3    Ivanovic
    # 3         4    Melissa         4       Lewis

.. code-block:: python

    first_names.set_index('id').join(last_names.set_index('id'))
    #    first_name   last_name
    # id
    # 1        Mark      Watney
    # 2         Jan  Twardowski
    # 3        Ivan    Ivanovic
    # 4     Melissa       Lewis

.. code-block:: python
    :caption: This method preserves the original DataFrame's index in the result.

    first_names.join(last_names.set_index('id'), on='id')
    #    id first_name   last_name
    # 0   1       Mark      Watney
    # 1   2        Jan  Twardowski
    # 2   3       Ivan    Ivanovic
    # 3   4    Melissa       Lewis

.. code-block:: python

    df1999.join(df2000, how='left', lsuffix='_1999', rsuffix='_2000')
    #                 Morning_1999  Noon_1999  ...  Evening_2000  Midnight_2000
    # 1999-12-29      1.764052   0.400157  ...           NaN            NaN
    # 1999-12-30      1.867558  -0.977278  ...           NaN            NaN
    # 1999-12-31     -0.103219   0.410599  ...           NaN            NaN
    # [3 rows x 8 columns]

    df1999.join(df2000, how='outer', lsuffix='_1999', rsuffix='_2000')
    #             Morning_1999  Noon_1999  ...  Evening_2000  Midnight_2000
    # 1999-12-29      1.764052   0.400157  ...           NaN            NaN
    # 1999-12-30      1.867558  -0.977278  ...           NaN            NaN
    # 1999-12-31     -0.103219   0.410599  ...           NaN            NaN
    # 2000-01-01           NaN        NaN  ...      0.443863       0.333674
    # 2000-01-02           NaN        NaN  ...      0.313068      -0.854096
    # 2000-01-03           NaN        NaN  ...      0.864436      -0.742165
    # [6 rows x 8 columns]


Assignments
===========

DataFrame Join
--------------
* Assignment name: DataFrame Join
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/df_join_eva.py`

:English:
    .. todo:: Translate to English

:Polish:
    #. Na podstawie podanych URL:

        * https://www.worldspaceflight.com/bios/eva/eva.php
        * https://www.worldspaceflight.com/bios/eva/eva2.php
        * https://www.worldspaceflight.com/bios/eva/eva3.php
        * https://www.worldspaceflight.com/bios/eva/eva4.php

    #. Scrappuj stronę wykorzystując ``pandas.read_html()``
    #. Połącz dane wykorzystując ``pd.concat``
    #. Przygotuj plik ``CSV`` z danymi dotyczącymi spacerów kosmicznych
    #. Zapisz dane do pliku
