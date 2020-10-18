*******************
Matplotlib Subplots
*******************


Rationale
=========
* `plt.subplot()`
* `plt.subplots()`


Subplot
=======
* nrows
* ncols
* index

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)


    plt.figure(figsize=(12, 6))

    plt.subplot(221)
    plt.plot(x, y, label='a')
    plt.legend()

    plt.subplot(222)
    plt.plot(x, y, label='b')
    plt.legend()

    plt.subplot(223)
    plt.plot(x, y, label='c')
    plt.legend()

    plt.subplot(224)
    plt.plot(x, y, label='d')
    plt.legend()

    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)


    plt.subplot(2, 2, 1)
    plt.plot(x, y, label='a')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(x, y, label='b')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(x, y, label='c')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(x, y, label='d')
    plt.legend()

    plt.show()


Subplots
========
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

    ax[0,0].plot(x, y, label='a')
    ax[0,1].plot(x, y, label='b')
    ax[1,0].plot(x, y, label='c')
    ax[1,1].plot(x, y, label='d')

    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

    ax[0,0].plot(x, y, label='a')
    ax[0,0].legend()

    ax[0,1].plot(x, y, label='b')
    ax[0,1].legend()

    ax[1,0].plot(x, y, label='c')
    ax[1,0].legend()

    ax[1,1].plot(x, y, label='d')
    ax[1,1].legend()


    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

    ax[0,0].plot(x, y, label='a')
    ax[0,1].plot(x, y, label='b')
    ax[1,0].plot(x, y, label='c')
    ax[1,1].plot(x, y, label='d')

    for chart in ax.ravel():
        chart.legend()


    plt.show()


Adjustments
===========
* https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))

    ax[0,0].plot(x, y, label='a')
    ax[0,1].plot(x, y, label='b')
    ax[1,0].plot(x, y, label='c')
    ax[1,1].plot(x, y, label='d')

    plt.subplots_adjust(
        left = 0.125,  # the left side of the subplots of the figure
        right = 0.9,   # the right side of the subplots of the figure
        bottom = 0.1,  # the bottom of the subplots of the figure
        top = 0.9,     # the top of the subplots of the figure
        wspace = 0.5,  # the amount of width reserved for space between subplots,
                       # expressed as a fraction of the average axis width
        hspace = 0.5,  # the amount of height reserved for space between subplots,
                       # expressed as a fraction of the average axis height
    )

    plt.show()
