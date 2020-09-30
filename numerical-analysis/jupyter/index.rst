*******
Jupyter
*******

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

* http://jupyter.org/
* http://jupyter.readthedocs.io/en/latest/install.html
* https://github.com/jupyter/notebook


Install
=======
.. code-block:: console

    $ pip install jupyter


Run
===
.. code-block:: console

    $ jupyter-notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

.. code-block:: console

    $ jupyter-notebook filename.ipynb


Using
=====
* Add code
* Run code
* Modify code and run
* Autocomplete
* Cell type (Markdown, LaTeX, Code)


Shortcut keys
=============

Indent
------
* ``Tab``
* ``Shift + Tab``

Comment Code
------------
* ``Ctrl + /``

Run
---
* ``Shift`` + ``Enter``


Cells
=====

Insert Below/Above Cells
------------------------

Add, Delete Cells
-----------------

Cut, Copy, Paste Cells
----------------------

Move Up/Down Cells
------------------

Merge, Split Cells
------------------


Run
===

Run Cell
--------
* ``Shift-Enter``

Run All (above/below)
---------------------

Clear Output
------------


Magic commands
==============
* ``%magic``
* ``%`` - Line Magics
* ``%%`` - Cell magic
* ``%run`` - Run the named file inside IPython as a program.
* ``!pip freeze``
* Full list https://ipython.readthedocs.io/en/stable/interactive/magics.html#

Kernels
=======
* Python 3
* https://github.com/jupyter/jupyter/wiki/Jupyter-kernels


Functions
=========

Checkpoints
-----------

Download
--------

Trust Notebook
--------------

Close and Halt
--------------


Performance and profiling
=========================
* ``%%timeit``
* ``%%timeit -n 1000 -r 7``


Markdown
========

Unorganized lists
-----------------
.. code-block:: md

    * first element
    * second element
    * third element

.. code-block:: md

    - first element
    - second element
    - third element

Organized lists
---------------
.. code-block:: md

    1. first element
    1. second element
    1. third element

Headers
-------
.. code-block:: md

    # Header level 1
    ## Header level 2
    ### Header level 3
    #### Header level 4
    ##### Header level 5
    ###### Header level 6

Formatting
----------
.. code-block:: md

    *italic*
    **bold**

Code inline
-----------
.. code-block:: md

    `class`

Code blocks
-----------
.. code-block:: md

    ```python
    name = 'José Jiménez'
    print(f'My name... {name}')
    ```

Tables
------
* https://www.tablesgenerator.com/markdown_tables

.. code-block:: md

    | id | first_name | last_name |    agency |
    |----|:-----------|:---------:|----------:|
    | 1  | José       |  Jiménez  |      NASA |
    | 2  | Иван       |  Иванович | Roscosmos |
    | 3  | Mark       |   Watney  |      NASA |
    | 4  | Alex       |   Vogel   |      NASA |


Embedding objects
=================

LaTeX
-----
* ``%%latex``

.. code-block:: text

    %%latex

    $$c = \sqrt{a^2 + b^2}$$

.. code-block:: text

    %%latex

    $$\int_{x=0}^{x=\infty} x^\pi dx$$

.. code-block:: text

    %%latex

    \begin{equation}
    H← ​​​60 ​+​ \frac{​​30(B-R)​​}{Vmax-Vmin}  ​​, if V​max​​ = G
    \end{equation}

.. code-block:: python

    from IPython.display import Latex

    Latex(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')
    Latex(r'$\lim_{x \to 0} (1+x)^{1/x} = e$')


Matplotlib charts
-----------------
.. code-block:: python

    x = np.linspace(-5, 5, 100)  # vector z 100 równo odległymi wartościami od -5 do 5
    y = np.sin(X)                # sinus wszystkich wartości x

    plt.plot(x, y);               # wykres liniowy


.. code-block:: text

    %matplotlib inline

.. code-block:: python

    import math
    import random
    from matplotlib import pyplot as plt

    x1 = [x*0.01 for x in range(0,628)]
    y1 = [math.sin(x*0.01)+random.gauss(0, 0.1) for x in range(0,628)]
    plt.plot(x1, y1)

    x2 = [x*0.5 for x in range(0,round(63/5))]
    y2 = [math.cos(x*0.5) for x in range(0,round(63/5))]
    plt.plot(x2, y2, 'o-')

    plt.show()

HTML
----
.. code-block:: python

    from IPython.display import HTML

    HTML("We can <i>generate</i> <code>html</code> code <b>directly</b>!")

JavaScript
----------
.. code-block:: python

    from IPython.display import Javascript

    Javascript("alert('It is JavaScript!')")

Image
-----
.. code-block:: python

    from IPython.display import Image

    Image(url="https://python.astrotech.io/_static/favicon.png")

YouTube
-------
.. code-block:: python

    from IPython.display import YouTubeVideo

    YouTubeVideo("h8mDUc5L0XM")


Workflow
========
.. code-block:: console

    $ pip install pandas

.. code-block:: python

    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(FILE, skiprows=1)

    df.head(5)
    #      5.1  3.5  1.4  0.2  0
    # 0    4.9  3.0  1.4  0.2  0
    # 1    4.7  3.2  1.3  0.2  0
    # 2    4.6  3.1  1.5  0.2  0
    # 3    5.0  3.6  1.4  0.2  0
    # 4    5.4  3.9  1.7  0.4  0

    df.columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

    df.head(5)
    #    Sepal length  Sepal width  Petal length  Petal width  Species
    # 0           5.1          3.5           1.4          0.2        0
    # 1           4.9          3.0           1.4          0.2        0
    # 2           4.7          3.2           1.3          0.2        0
    # 3           4.6          3.1           1.5          0.2        0
    # 4           5.0          3.6           1.4          0.2        0

    df.tail(3)
    #      Sepal length  Sepal width  Petal length  Petal width  Species
    # 147           6.5          3.0           5.2          2.0        2
    # 148           6.2          3.4           5.4          2.3        2
    # 149           5.9          3.0           5.1          1.8        2

    df['Species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

    df = df.sample(frac=1.0)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 120           5.6          2.8           4.9          2.0   virginica
    # 9             5.4          3.7           1.5          0.2      setosa
    # 54            5.7          2.8           4.5          1.3  versicolor
    # 46            4.6          3.2           1.4          0.2      setosa
    # 2             4.6          3.1           1.5          0.2      setosa
    # ...

    df.reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # ...

    df.describe()
    #        Sepal length  Sepal width  Petal length  Petal width
    # count    150.000000   150.000000    150.000000   150.000000
    # mean       5.843333     3.057333      3.758000     1.199333
    # std        0.828066     0.435866      1.765298     0.762238
    # min        4.300000     2.000000      1.000000     0.100000
    # 25%        5.100000     2.800000      1.600000     0.300000
    # 50%        5.800000     3.000000      4.350000     1.300000
    # 75%        6.400000     3.300000      5.100000     1.800000
    # max        7.900000     4.400000      6.900000     2.500000

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'

    df = pd.read_csv(DATA)
    df.hist()
    plt.show()

.. figure:: img/matplotlib-pd-hist.png
    :width: 75%
    :align: center

    Visualization using hist

Density
-------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(DATA)
    df.plot(kind='density', subplots=True, layout=(2,2), sharex=False)
    plt.show()

.. figure:: img/matplotlib-pd-density.png
    :width: 75%
    :align: center

    Visualization using density

Box
---
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(DATA)
    df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()

.. figure:: img/matplotlib-pd-box.png
    :width: 75%
    :align: center

    Visualization using density

Scatter matrix
--------------
* The in ``pandas`` version ``0.22`` plotting module has been moved from ``pandas.tools.plotting`` to ``pandas.plotting``
* As of version ``0.19``, the ``pandas.plotting`` library did not exist

.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas.plotting import scatter_matrix


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv'


    df = pd.read_csv(DATA)
    scatter_matrix(df)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :width: 75%
    :align: center

    Visualization using density

Descriptive statistics
----------------------
.. csv-table:: Descriptive statistics
    :header: "Function", "Description"

    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Execute terminal commands
=========================
* ``!``
* ``!pwd``
* ``!ls``
* .. code-block:: python
    :force:

    dirs = !ls

    for file in dirs:
        if file.find("1_") >= 0:
            print(file)


Output to different formats
===========================
File -> Download as:

    * Notebook (.ipynb)
    * Python (.py)
    * HTML (.html)
    * Reveal.js Slides (.html)
    * Markdown (.md)
    * reST (.rst)
    * LaTeX (.lex)
    * PDF via LaTeX (.pdf)

Generate HTML
-------------
#. File -> Save and Checkpoint
#. File -> Download as -> HTML (.html)

Slides
------
#. View -> Cell Toolbar -> Slideshow
#. Select slides, subslides and speaker notes
#. File -> Save and Checkpoint
#. File -> Download as -> Reveal.js slides (.slides.html)

Github pages with Jupyter Slides
--------------------------------
.. code-block:: console

    $ git submodule add https://github.com/hakimel/reveal.js.git reveal.js

    $ jupyter nbconvert --to slides index.ipynb --reveal-prefix=reveal.js

    $ jupyter nbconvert --to slides index.ipynb --reveal-prefix=reveal.js \
        --SlidesExporter.reveal_theme=serif \
        --SlidesExporter.reveal_scroll=True \
        --SlidesExporter.reveal_transition=none

Assignments
===========

Jupyter First
-------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/jupyter_first.ipynb`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Stwórz notebook jupyter o nazwie ``jupyter_first.ipynb``
    #. dodaj tekst opisujący następne polecenia
    #. dodaj trzy różne 'code cell'
    #. uruchom code cell z wynikiem wszystkich powyżej
    #. dodaj code cell, który pokaże czas wykonywania instrukcji
    #. dodaj Code Cell, który wyświetli wykres funkcji ``sin()`` inplace

Jupyter Slides
--------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/jupyter_slides.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Poprzedni skrypt przekonwertuj na slajdy i uruchom prezentację w przeglądarce
