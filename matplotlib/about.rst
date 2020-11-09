****************
Matplotlib About
****************


What is matplotlib
==================
Moduł ``matplotlib`` pozwala na rysowanie wykresów i diagramów. Jest to bardzo rozbudowana biblioteka z setkami opcji konfiguracyjnych. Najczęściej używanym modułem biblioteki ``matplotlib`` jest moduł ``pyplot``, który implementuje szereg funkcji umożliwiających rysowanie wykresów 2d.

Pyplot's state-machine environment behaves similarly to MATLAB and should be most familiar to users with MATLAB experience.

Matplotlib is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell (à la MATLAB or Mathematica), web application servers, and various graphical user interface toolkits.

It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of matplotlib.

* https://github.com/matplotlib/matplotlib
* http://matplotlib.org/


Install
=======
.. code-block:: console

    $ pip install matplotlib


Usage
=====

Import
------
.. code-block:: python

    import matplotlib.pyplot as plt

Running matplotlib in PyCharm
-----------------------------
* Scientific Mode

Running matplotlib in standalone scripts
----------------------------------------
* Scale
* Export to image
* Reposition
* Other options

.. code-block:: python

    import matplotlib.pyplot as plt

    x = [1,2,3]
    y = [4,5,6]

    plt.plot(x, y)
    plt.show()

Exporting plot as an image
--------------------------
.. code-block:: python

    import matplotlib.pyplot as plt

    x = [1,2,3]
    y = [4,5,6]

    plt.plot(x, y)
    plt.savefig('my_file.png')


Charts Gallery
==============
* https://matplotlib.org/gallery/index.html


Further Reading
===============
* https://www.data-to-viz.com/#explore
* https://www.data-to-viz.com/img/poster/poster_big.png
