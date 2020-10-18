Basic customizations
====================
* figure object is implied
* explicit assignment is needed when customizing

.. code-block:: python

    fig = plt.figure()

Size
----
Local:

    .. code-block:: python

        plt.figure(figsize=(3,4))

Global:
    .. code-block:: python

        import matplotlib.pyplot as plt

        plt.rcParams["figure.figsize"] = (20,10)

    .. code-block:: python

        import matplotlib

        matplotlib.rc('figure', figsize=(20,10))

Font
----
* ``'serif'``
* ``'sans-serif'``
* ``'cursive'``
* ``'fantasy'``
* ``'monospace'``

.. code-block:: python

    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.rc('font', family='Serif', weight='bold', size=8)

    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    plt.plot(x, y)
    plt.grid(True)
    plt.show()

Subplots
--------
.. code-block:: python

    fig = plt.figure()

    ax1 = plt.subplot2grid(shape=(1,1), loc=(0,0)) # ``loc`` = Location to place axis within grid.

    plt.subplot_adjust(left=0.9, bottom=0.16)  # set margins
