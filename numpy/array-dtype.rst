****************
Array Data Types
****************


Rationale
=========
* Array can have only one data type (``dtype``)
* Type can be "non-primitive" - any class


Bits and Bytes
==============
* Signed and unsigned
* For negative numbers "Two's complement" is used

.. code-block:: text

    1       # unsigned

    +1      # signed
    -1      # signed

.. code-block:: text
    :caption: Three-bit unsigned integers. Values: 8, minimal: 0, maximal: 8

    0   000
    1   001
    2   010
    3   011
    4   100
    5   101
    6   110
    7   111

.. code-block:: text
    :caption: Three-bit signed integers. Values: 8, minimal: -4, maximal: 3

    0   000
    1   001
    2   010
    3   011
    −4  100
    −3  101
    −2  110
    −1  111

.. code-block:: text
    :caption: Eight-bit signed integers. Values: 256, minimal: -128, maximal: 127

    0      0000 0000
    1      0000 0001
    2      0000 0010
    126    0111 1110
    127    0111 1111
    −128   1000 0000
    −127   1000 0001
    −126   1000 0010
    −2     1111 1110
    −1     1111 1111

.. code-block:: text
    :caption: 32 bit unsigned int. Values: 2,147,483,647, minimal: 0, maximal: 2,147,483,647

    0000000000000000000000000000000000 => 0
    0000000000000000000000000000000001 => 1
    0000000000000000000000000000000010 => 2
    0000000000000000000000000000000011 => 3
    0000000000000000000000000000000100 => 4
    0000000000000000000000000000000101 => 5
    0000000000000000000000000000000110 => 6
    0000000000000000000000000000000111 => 7

.. code-block:: python
    :caption: Calculates a two's complement integer from the given input value's bits.

    def twos_complement(value: int, num_bits: int) -> int:
        mask = 2 ** (num_bits - 1)
        return -(value & mask) + (value & ~mask)


Signed int
==========
* Signed (positive and negative)
* ``np.int`` alias for ``np.int64``
* ``np.int0`` alias for ``np.int64`` - Integer used for indexing
* ``np.int8``
* ``np.int16``
* ``np.int32``
* ``np.int64``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bytes", "Values", "Minimal", "Maximal"

    "``np.int8``", "8", "256", "-128", "127"
    "``np.int16``", "16", "65,536", "-32,768", "32,767"
    "``np.int32``", "32", "4,294,967,296", "-2,147,483,648", "2,147,483,646"
    "``np.int64``", "64", "18,446,744,073,709,551,616", "-9,223,372,036,854,775,808", "9,223,372,036,854,775,807"

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    type(a)
    # <class 'numpy.np.ndarray'>

    a.dtype
    # dtype('int64')

.. code-block:: python

    import numpy as np


    a = np.array([[1., 2., 3.],
                  [4., 5., 6.]])

    a.astype(int)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.astype(np.int8)
    # array([[1, 2, 3],
    #        [4, 5, 6]], dtype=int8)

    a.astype(np.int64)
    # array([[1, 2, 3],
    #        [4, 5, 6]])


Unsigned int
============
* Unsigned (non-negative only)
* ``np.uint0``
* ``np.uint8``
* ``np.uint16``
* ``np.uint32``
* ``np.uint64``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bytes", "Values", "Minimal", "Maximal"

    "``np.uint8``", "8", "256", "0", "255"
    "``np.uint16``", "16", "65,536", "0", "65,535"
    "``np.uint32``", "32", "4,294,967,296", "0", "4,294,967,295"
    "``np.uint64``", "64", "18,446,744,073,709,551,616", "0", "18,446,744,073,709,551,615"

.. code-block:: python

    import numpy as np


    a = np.array([-1, 0, 1])

    type(a)
    # <class 'numpy.np.ndarray'>

    a.dtype
    # dtype('int64')

.. code-block:: python

    import numpy as np


    a = np.array([-1, 0, 1])

    a.astype(int)
    # array([-1, 0, 1])

    a.astype(np.uint8)
    # array([255, 0, 1], dtype=uint8)

    a.astype(np.uint64)
    # array([18446744073709551615, 0, 1], dtype=uint64)


float
=====
* ``np.float``
* ``np.float16``
* ``np.float32``
* ``np.float64``
* ``np.float128``

.. csv-table:: Number of values is calculated with ``2 ** bytes``
    :header: "Type", "Bytes", "Values", "Minimal", "Maximal", "Precision"

    "``np.float16``", "16", "-65,504", "65,504", "0.0000000596046"
    "``np.float32``", "32", "±0.000000×10−95", "±9.999999×1096"
    "``np.float64``", "64", "±0.000000000000000×10−383", "±9.999999999999999×10384"
    "``np.float128``", "64", "±0.000000000000000000000000000000000×10−6143", "±9.999999999999999999999999999999999×106144"

.. code-block:: python

    import numpy as np


    a = np.array([1., 2., 3.])

    type(a)
    # <class 'numpy.np.ndarray'>

    a.dtype
    # dtype('float64')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.astype(float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float16)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float16)

    a.astype(np.float32)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float32)

    a.astype(np.float64)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float128)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float128)


complex
=======
* ``np.complex``
* ``np.complex64``
* ``np.complex128``
* ``np.complex256``

.. code-block:: python

    import numpy as np


    a = np.array([1+2j])

    a.dtype
    # dtype('complex128')

.. code-block:: python

    import numpy as np


    a = np.array([1.1+2.2j])
    # array([1.1+2.2j])

    a.dtype
    # dtype('complex128')


bool
====
.. code-block:: python

    import numpy as np


    a = np.array([True, False, True])

    a.dtype
    # dtype('bool')

.. code-block:: python

    import numpy as np


    a = np.array([1, 0, 1], bool)

    a.dtype
    # dtype('bool')

    repr(a)
    # array([ True, False,  True])


str
===
.. code-block:: python

    import numpy as np


    np.array(['a', 'b', 'c'])
    # array(['a', 'b', 'c'], dtype='<U1')

    np.array(['one', 'two', 'three'])
    # array(['one', 'two', 'three'], dtype='<U5')


Assignments
===========

Numpy Dtype Astype
------------------
* Assignment: Numpy Dtype Astype
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min
* Filename: :download:`assignments/numpy_astype.py`

English:
    #. Use data from "Given" section (see below)
    #. Given ``a: np.ndarray`` (see below)
    #. Convert to ``int`` type
    #. The result convert to ``bool`` type
    #. What happened in each of those steps?

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Dany ``a: np.ndarray`` (patrz sekcja input)
    #. Przekonwertuj do typu ``int``
    #. Rezultat rzutuj na typ ``bool``
    #. Co się stało w każdym z tych kroków?

Given:
    .. code-block:: python

        a = np.array([[-1.1, 0.0, 1.1],
                      [ 2.2, 3.3, 4.4]])

