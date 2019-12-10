*************
Series Update
*************


Fill NaN - Scalar value
=======================
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = [1, np.nan, np.nan, np.nan, 2, np.nan, 3, np.inf]
    s = pd.Series(data)

    s
    # 0    1.0
    # 1    NaN
    # 2    NaN
    # 3    NaN
    # 4    2.0
    # 5    NaN
    # 6    3.0
    # 7    inf
    # dtype: float64

    s.fillna(0.0)
    # 0    1.0
    # 1    0.0
    # 2    0.0
    # 3    0.0
    # 4    2.0
    # 5    0.0
    # 6    3.0
    # 7    inf
    # dtype: float64


Fill NaN - Forward Fill
=======================
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = [1, np.nan, np.nan, np.nan, 2, np.nan, 3, np.inf]
    s = pd.Series(data)

    s
    # 0    1.0
    # 1    NaN
    # 2    NaN
    # 3    NaN
    # 4    2.0
    # 5    NaN
    # 6    3.0
    # 7    inf
    # dtype: float64

    s.ffill()
    # 0    1.0
    # 1    1.0
    # 2    1.0
    # 3    1.0
    # 4    2.0
    # 5    2.0
    # 6    3.0
    # 7    inf
    # dtype: float64


Fill NaN - Backward Fill
========================
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = [1, np.nan, np.nan, np.nan, 2, np.nan, 3, np.inf]
    s = pd.Series(data)

    s
    # 0    1.0
    # 1    NaN
    # 2    NaN
    # 3    NaN
    # 4    2.0
    # 5    NaN
    # 6    3.0
    # 7    inf
    # dtype: float64

    s.bfill()
    # 0    1.0
    # 1    2.0
    # 2    2.0
    # 3    2.0
    # 4    2.0
    # 5    3.0
    # 6    3.0
    # 7    inf
    # dtype: float64


Fill NaN - Interpolate
======================
* ``method: str``, default ``linear``

.. list-table:: Interpolation techniques
    :widths: 25, 75
    :header-rows: 1

    * - Method
      - Description

    * - ``linear``
      - Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes

    * - ``time``
      - Works on daily and higher resolution data to interpolate given length of interval

    * - ``index``, ``values``
      - use the actual numerical values of the index.

    * - ``pad``
      - Fill in NaNs using existing values

    * - ``nearest``, ``zero``, ``slinear``, ``quadratic``, ``cubic``, ``spline``, ``barycentric``, ``polynomial``
      - Passed to ``scipy.interpolate.interp1d``. These methods use the numerical values of the index.  Both ``polynomial`` and ``spline`` require that you also specify an ``order`` (int), e.g. ``df.interpolate(method='polynomial', order=5)``

    * - ``krogh``, ``piecewise_polynomial``, ``spline``, ``pchip``, ``akima``
      - Wrappers around the SciPy interpolation methods of similar names

    * - ``from_derivatives``
      - Refers to ``scipy.interpolate.BPoly.from_derivatives`` which replaces ``piecewise_polynomial`` interpolation method in scipy 0.18.

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = [1, np.nan, np.nan, np.nan, 2, np.nan, 3, np.inf]
    s = pd.Series(data)

    s
    # 0    1.0
    # 1    NaN
    # 2    NaN
    # 3    NaN
    # 4    2.0
    # 5    NaN
    # 6    3.0
    # 7    inf
    # dtype: float64

    s.interpolate()
    # 0    1.00
    # 1    1.25
    # 2    1.50
    # 3    1.75
    # 4    2.00
    # 5    2.50
    # 6    3.00
    # 7     inf
    # dtype: float64
