***************
Array Serialize
***************


``list``
========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a.tolist()
    # [1, 2, 3]

    list(a)
    # [1, 2, 3]

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.tolist()
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    list(a)
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


``str``
=======
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a.tostring()
    # b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'

    np.fromstring(b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00')
    # DeprecationWarning: The binary mode of fromstring is deprecated, as it behaves surprisingly on unicode inputs. Use frombuffer instead
    # array([4.9e-324, 9.9e-324, 1.5e-323])

    np.frombuffer(b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00')
    # array([4.9e-324, 9.9e-324, 1.5e-323])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)
    # array([1., 2., 3.])

    a.tostring()
    # b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'

    np.fromstring(b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@')
    # array([1., 2., 3.])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.tostring()
    # b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00'

    np.fromstring(b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x14@\x00\x00\x00\x00\x00\x00\x18@')
    # array([1., 2., 3., 4., 5., 6.])


Assignments
===========
.. todo:: Create assignments
