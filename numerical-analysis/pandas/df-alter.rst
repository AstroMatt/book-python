***************
DataFrame Alter
***************


Add Rows and Columns
====================
.. code-block:: python
    :caption: Add Column

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

    df['X'] = ['a', 'b', 'c']
    #     A   B   C  X
    # 0  10  20  30  a
    # 1  11  21  31  b
    # 2  12  22  32  c

    df['X'] = ['a', 'b']
    # ValueError: Length of values does not match length of index

    df['X'] = ['a', 'b', 'c', 'd']
    # ValueError: Length of values does not match length of index

    df['Z'] = np.arange(3.0)
    #     A   B   C    Z
    # 0  10  20  30  0.0
    # 1  11  21  31  1.0
    # 2  12  22  32  2.0

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


Drop Rows and Columns
=====================
* Works with ``inplace=True``

.. code-block:: python
    :caption: Drop Column

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

    df.drop('A', axis='columns')
    #     B   C
    # 0  20  30
    # 1  21  31
    # 2  22  32

    df.drop(columns='A')
    #     B   C
    # 0  20  30
    # 1  21  31
    # 2  22  32

    df.drop(columns=['A', 'B'])
    #     C
    # 0  30
    # 1  31
    # 2  32

.. code-block:: python
    :caption: Drop Row

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

    df.drop(1)
    #     A   B   C
    # 0  10  20  30
    # 2  12  22  32

    df.drop([0, 2])
    #     A   B   C
    # 1  11  21  31

    rows = df1[:2].index
    df.drop(rows)
    #     A   B   C
    # 2  12  22  32

.. code-block:: python
    :caption: Drop from Timeseries

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.drop('1999-12-30')
    # Traceback (most recent call last):
    #    ...
    # KeyError: "['1999-12-30'] not found in axis"

    df.drop(pd.Timestamp('1999-12-30'))
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Transpose
=========
* ``df.transpose()`` or ``df.T``
* ``df.transpose()`` is preferred

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

    df.transpose()
    #     0   1   2
    # A  10  11  12
    # B  20  21  22
    # C  30  31  32

    df.T
    #     0   1   2
    # A  10  11  12
    # B  20  21  22
    # C  30  31  32

.. code-block:: python

    df = pd.DataFrame({
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': [30, 31, 32]})

    df['A']         # will select column A
    df['B']         # will select column B
    df['C']         # will select column C

    df.A            # will select column A
    df.B            # will select column B
    df.C            # will select column C

    df.T            # will transpose data
    df.transpose()  # will transpose data

.. code-block:: python

    df = pd.DataFrame({
        'R': [10, 11, 12],
        'S': [20, 21, 22],
        'T': [30, 31, 32]})

    df['R']         # will select column R
    df['S']         # will select column S
    df['T']         # will select column T

    df.R            # will select column R
    df.S            # will select column S
    df.T            # will transpose data

    df.transpose()  # will transpose data


Assignments
===========
.. todo:: Create assignments
