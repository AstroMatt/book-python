*****************
Matplotlib Scales
*****************


Rationale
=========
* Liniowa
* Logarytmiczna
* Symmetrical log (można ustawić fragmentami liniowo ``linthreshx: int``)
* Logit - odwrotność logistycznej

* Subtracting ``x.mean()`` is used to better highlight the function


Linear Scale
============
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('linear')

    plt.plot(x, y)
    plt.show()


Logarithmic Scale
=================
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('log')

    plt.plot(x, y)
    plt.show()


Symmetrical Logarithmic Scale
=============================
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('symlog', linthresh=0.01)

    plt.plot(x, y)
    plt.show()


Logit Scale
===========
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.linspace(0, 10, 1000)
    y = x - x.mean()

    plt.yscale('logit')

    plt.plot(x, y)
    plt.show()
