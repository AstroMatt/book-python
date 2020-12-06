****************
DataFrame Create
****************


Create from List of Dicts
=========================
.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'A': 1.0, 'B': 2.0},
        {'A': 3.0, 'B': 4.0},
    ])

    #      A    B
    # 0  1.0  2.0
    # 1  3.0  4.0

.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'A': 1.0, 'B': 2.0},
        {'B': 3.0, 'C': 4.0},
    ])

    #      A    B    C
    # 0  1.0  2.0  NaN
    # 1  NaN  3.0  4.0

.. code-block:: python

    import pandas as pd

    pd.DataFrame([
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'},
    ])

    #    firstname    lastname
    # 0       Mark      Watney
    # 1        Jan  Twardowski
    # 2       Ivan    Ivanovic
    # 3    Melissa       Lewis


Create from Dict
================
.. code-block:: python

    import pandas as pd

    pd.DataFrame({
        'A': ['a', 'b', 'c'],
        'B': [1.0, 2.0, 3.0],
        'C': [1, 2, 3],
    })

    #    A    B  C
    # 0  a  1.0  1
    # 1  b  2.0  2
    # 2  c  3.0  3

.. code-block:: python

    import pandas as pd

    pd.DataFrame({
        'firstname': ['Mark', 'Jan', 'Ivan', 'Melissa'],
        'lastname': ['Watney', 'Twardowski', 'Ivanovic', 'Lewis'],
    })

    #    firstname    lastname
    # 0       Mark      Watney
    # 1        Jan  Twardowski
    # 2       Ivan    Ivanovic
    # 3    Melissa       Lewis

.. code-block:: python

    import pandas as pd
    import numpy as np

    pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('1961-04-12'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo',
        'G': [1,2,3,4],
    })

    #      A           B    C  D      E    F  G
    # 0  1.0  1961-04-12  1.0  3   test  foo  1
    # 1  1.0  1961-04-12  1.0  3  train  foo  2
    # 2  1.0  1961-04-12  1.0  3   test  foo  3
    # 3  1.0  1961-04-12  1.0  3  train  foo  4


Create from NDArray
===================
.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(np.random.randn(7, 4))

    df
    #           0         1         2         3
    # 0  1.764052  0.400157  0.978738  2.240893
    # 1  1.867558 -0.977278  0.950088 -0.151357
    # 2 -0.103219  0.410599  0.144044  1.454274
    # 3  0.761038  0.121675  0.443863  0.333674
    # 4  1.494079 -0.205158  0.313068 -0.854096
    # 5 -2.552990  0.653619  0.864436 -0.742165
    # 6  2.269755 -1.454366  0.045759 -0.187184


Assignments
===========

DataFrame Create
----------------
* Assignment: DataFrame Create
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min
* Filename: :download:`assignments/df_create.py`

English:
    #. Use data from "Given" section (see below)
    #. Create ``DataFrame`` for input data

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz ``DataFrame`` dla danych wejściowych

Given:
    .. csv-table::
        :header: "Crew", "Role", "Astronaut"

        "Prime", "CDR", "Neil Armstrong"
        "Prime", "LMP", "Buzz Aldrin"
        "Prime", "CMP", "Michael Collins"
        "Backup", "CDR", "James Lovell"
        "Backup", "LMP", "William Anders"
        "Backup", "CMP", "Fred Haise"

Hints:
    * Use selection with ``alt`` key in your IDE
    * If it's not working use CSV:

        .. code-block:: text

            "Crew", "Role", "Astronaut"
            "Prime", "CDR", "Neil Armstrong"
            "Prime", "LMP", "Buzz Aldrin"
            "Prime", "CMP", "Michael Collins"
            "Backup", "CDR", "James Lovell"
            "Backup", "LMP", "William Anders"
            "Backup", "CMP", "Fred Haise"

