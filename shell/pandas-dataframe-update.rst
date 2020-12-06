****************
DataFrame Update
****************


Update Column
=============
.. code-block:: python

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

    df['C'] = 0
    df
    #     A   B  C
    # 0  10  20  0
    # 1  11  21  0
    # 2  12  22  0


Update Row
==========
.. code-block:: python

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

    df[1:2] = 0
    df
    #     A   B   C
    # 0  10  20  30
    # 1   0   0   0
    # 2  12  22  32

    df[::2] = 99
    df
    #     A   B   C
    # 0  99  99  99
    # 1   0   0   0
    # 2  99  99  99

.. code-block:: python

    df.loc[df['Species'] == 0, 'Species'] = 'Setosa'
    df.loc[df['Species'] == 1, 'Species'] = 'Versicolor'
    df.loc[df['Species'] == 2, 'Species'] = 'Virginica'

.. code-block:: python

    df['Species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)


Assignments
===========
.. todo:: Create assignments
