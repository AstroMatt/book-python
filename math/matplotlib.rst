
``matplotlib``
==============
* biblioteka zewnętrzna ``pip install matplotlib``

.. note:: Moduł jest szczegółowo opisany w :ref:`Matplotlib`.

Moduł ``matplotlib`` pozwala na rysowanie wykresów i diagramów. Jest to bardzo rozbudowana biblioteka z setkami opcji konfiguracyjnych. Najczęściej używanym modułem biblioteki ``matplotlib`` jest moduł ``pyplot``, który implementuje szereg funkcji umożliwiających rysowanie wykresów 2d.

``Matplotlib`` and ``Jupyter``
------------------------------
* To display ``matplotlib`` figures inline, you have run at least once per kernel run:

    .. code-block:: text

        %matplotlib inline

Points
------
.. figure:: img/matplotlib-01.png
    :scale: 50%
    :align: center

    Points chart

.. code-block:: python
    :caption: Matplotlib example

    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    plt.plot(x, y, 'o')
    plt.show()

Sinusoid on grid
----------------
.. figure:: img/matplotlib-02.png
    :scale: 50%
    :align: center

    Sinusoid on grid

.. code-block:: python
    :caption: Matplotlib example

    import matplotlib.pyplot as plt
    import numpy as np

    y = np.arange(0.0, 2.0, 0.01)
    x = 1 + np.sin(2 * np.pi * y)

    fig, ax = plt.subplots()

    ax.plot(y, x)
    ax.grid()
    ax.set(
        xlabel='time (s)',
        ylabel='voltage (mV)',
        title='Voltage in Time')

    plt.show()


Multiple charts
---------------
.. figure:: img/matplotlib-03.png
    :scale: 50%
    :align: center

    Multiple charts

.. code-block:: python
    :caption: Matplotlib example

    import numpy as np
    import matplotlib.pyplot as plt


    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi * t)


    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    plt.show()
