**********
Line Chart
**********


Rationale
=========
* Show linear relation of two variables


Syntax
======
.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    plt.plot(x, y)
    plt.show()


Line Styles
===========
.. figure:: img/matplotlib-plt-linestyle-basic.png
    :width: 75%
    :align: center

.. figure:: img/matplotlib-plt-linestyle-advanced.png
    :width: 75%
    :align: center


Single Plot
===========
.. code-block:: python
    :caption: Vectorized Operations

    import matplotlib.pyplot as plt
    import numpy as np
    np.random.seed(0)

    x = np.arange(0, 10)
    y = np.random.randint(0, 10, size=10)

    plt.plot(x, y)
    plt.show()

.. code-block:: python
    :caption: Universal Function

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()


Multiple Plots
==============
.. code-block:: python

    import matplotlib.pyplot as plt


    x1 = [1, 2, 3, 4]
    y1 = [1, 2, 3, 4]

    x2 = [1, 2, 3, 4]
    y2 = [4, 3, 3, 2]

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.show()

.. code-block:: python
    :caption: Universal Function

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()

.. code-block:: python
    :caption: Inlined Universal Function

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()

.. code-block:: python
    :caption: Vectorized Operation

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 2, 100)

    plt.plot(x, x)
    plt.plot(x, x**2)
    plt.plot(x, x**3)
    plt.show()

.. code-block:: python
    :caption: Universal Function and Vectorized Operation

    import matplotlib.pyplot as plt
    import numpy as np
    np.random.seed(0)


    noise = np.random.normal(0.0, 0.1, size=1000)

    x1 = np.linspace(0, 2*np.pi, 1000)
    y1 = np.sin(x1) + noise

    x2 = np.linspace(2*np.pi, 3*np.pi, 20)
    y2 = np.sin(x2)

    plt.plot(x1, y1)
    plt.plot(x2, y2, linestyle='--')
    plt.show()
