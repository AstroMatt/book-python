*************************
Matplotlib Plot Lifecycle
*************************

This tutorial aims to show the beginning, middle, and end of a single
visualization using Matplotlib. We'll begin with some raw data and
end by saving a figure of a customized visualization. Along the way we'll try
to highlight some neat features and best-practices using Matplotlib.

.. note::

    This tutorial is based off of
    `this excellent blog post <http://pbpython.com/effective-matplotlib.html>`_
    by Chris Moffitt. It was transformed into this tutorial by Chris Holdgraf.


A note on the Object-Oriented API vs Pyplot
===========================================
Matplotlib has two interfaces. The first is an object-oriented (OO)
interface. In this case, we utilize an instance of ``axes.Axes``
in order to render visualizations on an instance of ``figure.Figure``.

The second is based on MATLAB and uses a state-based interface. This is
encapsulated in the ``pyplot`` module. See the pyplot tutorials for a more in-depth look at the pyplot
interface.

Most of the terms are straightforward but the main thing to remember
is that:

* The Figure is the final image that may contain 1 or more Axes.
* The Axes represent an individual plot (don't confuse this with the word
  "axis", which refers to the x/y axis of a plot).

We call methods that do the plotting directly from the Axes, which gives
us much more flexibility and power in customizing our plot.

.. note::

   In general, try to use the object-oriented interface over the pyplot
   interface.


Our data
========
We'll use the data from the post from which this tutorial was derived.
It contains sales information for a number of companies.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import FuncFormatter

    data = {'Barton LLC': 109438.50,
            'Frami, Hills and Schmidt': 103569.59,
            'Fritsch, Russel and Anderson': 112214.71,
            'Jerde-Hilpert': 112591.43,
            'Keeling LLC': 100934.30,
            'Koepp Ltd': 103660.54,
            'Kulas Inc': 137351.96,
            'Trantow-Barrows': 123381.38,
            'White-Trantow': 135841.99,
            'Will LLC': 104437.60}

    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)


Getting started
===============

This data is naturally visualized as a barplot, with one bar per
group. To do this with the object-oriented approach, we'll first generate
an instance of ``figure.Figure`` and
``axes.Axes``. The Figure is like a canvas, and the Axes
is a part of that canvas on which we will make a particular visualization.

.. code-block:: python

    fig, ax = plt.subplots()

.. figure:: img/matplotlib-lifecycle-01.png
    :width: 75%
    :align: center

Now that we have an Axes instance, we can plot on top of it.

.. code-block:: python

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)

.. figure:: img/matplotlib-lifecycle-02.png
    :width: 75%
    :align: center


Controlling the style
=====================
There are many styles available in Matplotlib in order to let you tailor
your visualization to your needs. To see a list of styles, we can use
``pyplot.style``.

.. code-block:: python

    print(plt.style.available)
    # ['seaborn-ticks', 'ggplot', 'dark_background', 'bmh', 'seaborn-poster',
    # 'seaborn-notebook', 'fast', 'seaborn', 'classic', 'Solarize_Light2',
    # 'seaborn-dark', 'seaborn-pastel', 'seaborn-muted', '_classic_test',
    # 'seaborn-paper', 'seaborn-colorblind', 'seaborn-bright', 'seaborn-talk',
    # 'seaborn-dark-palette', 'tableau-colorblind10', 'seaborn-darkgrid',
    # 'seaborn-whitegrid', 'fivethirtyeight', 'grayscale', 'seaborn-white',
    # 'seaborn-deep']

You can activate a style with the following:

    .. code-block:: python

        plt.style.use('fivethirtyeight')

Now let's remake the above plot to see how it looks:

    .. code-block:: python


        fig, ax = plt.subplots()
        ax.barh(group_names, group_data)

.. figure:: img/matplotlib-lifecycle-03.png
    :width: 75%
    :align: center

    The style controls many things, such as color, linewidths, backgrounds, etc.


Customizing the plot
====================
Now we've got a plot with the general look that we want, so let's fine-tune
it so that it's ready for print. First let's rotate the labels on the x-axis
so that they show up more clearly. We can gain access to these labels
with the ``axes.Axes.get_xticklabels`` method:

    .. code-block:: python

        fig, ax = plt.subplots()
        ax.barh(group_names, group_data)
        labels = ax.get_xticklabels()

.. figure:: img/matplotlib-lifecycle-04.png
    :width: 75%
    :align: center

If we'd like to set the property of many items at once, it's useful to use
the ``pyplot.setp`` function. This will take a list (or many lists) of
Matplotlib objects, and attempt to set some style element of each one.

    .. code-block:: python


        fig, ax = plt.subplots()
        ax.barh(group_names, group_data)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')

.. figure:: img/matplotlib-lifecycle-05.png
    :width: 75%
    :align: center

It looks like this cut off some of the labels on the bottom. We can
tell Matplotlib to automatically make room for elements in the figures
that we create. To do this we'll set the ``autolayout`` value of our
rcParams.

.. code-block:: python

    plt.rcParams.update({'figure.autolayout': True})

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

.. figure:: img/matplotlib-lifecycle-06.png
    :width: 75%
    :align: center

Next, we'll add labels to the plot. To do this with the OO interface,
we can use the ``axes.Axes.set`` method to set properties of this
Axes object.

.. code-block:: python

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
           title='Company Revenue')

.. figure:: img/matplotlib-lifecycle-07.png
    :width: 75%
    :align: center

We can also adjust the size of this plot using the ``pyplot.subplots``
function. We can do this with the ``figsize`` kwarg.

.. note:: While indexing in NumPy follows the form (row, column), the figsize
   kwarg follows the form (width, height). This follows conventions in
   visualization, which unfortunately are different from those of linear
   algebra.

.. code-block:: python

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
           title='Company Revenue')

.. figure:: img/matplotlib-lifecycle-08.png
    :width: 75%
    :align: center

For labels, we can specify custom formatting guidelines in the form of
functions by using the ``ticker.FuncFormatter`` class. Below we'll
define a function that takes an integer as input, and returns a string
as an output.

.. code-block:: python

    def currency(x, pos):
        """The two args are the value and tick position"""
        if x >= 1e6:
            s = '${:1.1f}M'.format(x*1e-6)
        else:
            s = '${:1.0f}K'.format(x*1e-3)
        return s

    formatter = FuncFormatter(currency)

We can then apply this formatter to the labels on our plot. To do this,
we'll use the ``xaxis`` attribute of our axis. This lets you perform
actions on a specific axis on our plot.

.. code-block:: python

    fig, ax = plt.subplots(figsize=(6, 8))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
           title='Company Revenue')
    ax.xaxis.set_major_formatter(formatter)

.. figure:: img/matplotlib-lifecycle-09.png
    :width: 75%
    :align: center


Combining multiple visualizations
=================================
It is possible to draw multiple plot elements on the same instance of
``axes.Axes``. To do this we simply need to call another one of
the plot methods on that axes object.

.. code-block:: python

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    # Add a vertical line, here we set the style in the function call
    ax.axvline(group_mean, ls='--', color='r')

    # Annotate new companies
    for group in [3, 5, 8]:
        ax.text(145000, group, "New Company", fontsize=10,
                verticalalignment="center")

    # Now we'll move our title up since it's getting a little cramped
    ax.title.set(y=1.05)

    ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
           title='Company Revenue')
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
    fig.subplots_adjust(right=.1)

    plt.show()

.. figure:: img/matplotlib-lifecycle-10.png
    :width: 75%
    :align: center


Saving our plot
===============
Now that we're happy with the outcome of our plot, we want to save it to
disk. There are many file formats we can save to in Matplotlib. To see
a list of available options, use:

.. code-block:: python

    print(fig.canvas.get_supported_filetypes())
    # {'ps': 'Postscript',
    # 'eps': 'Encapsulated Postscript',
    # 'pdf': 'Portable Document Format',
    # 'pgf': 'PGF code for LaTeX',
    # 'png': 'Portable Network Graphics',
    # 'raw': 'Raw RGBA bitmap',
    # 'rgba': 'Raw RGBA bitmap',
    # 'svg': 'Scalable Vector Graphics',
    # 'svgz': 'Scalable Vector Graphics',
    # 'jpg': 'Joint Photographic Experts Group',
    # 'jpeg': 'Joint Photographic Experts Group',
    # 'tif': 'Tagged Image File Format',
    # 'tiff': 'Tagged Image File Format'}

We can then use the ``figure.Figure.savefig`` in order to save the figure
to disk. Note that there are several useful flags we'll show below:

* ``transparent=True`` makes the background of the saved figure transparent
  if the format supports it.
* ``dpi=80`` controls the resolution (dots per square inch) of the output.
* ``bbox_inches="tight"`` fits the bounds of the figure to our plot.

.. code-block:: python

    fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")

Assignments
===========

Iris transformations
--------------------
* Assignment: Iris transformations
* Last update: 2020-10-01
* Complexity: medium
* Lines of code: 20 lines
* Estimated time: 21 min
* Filename: :download:`assignments/matplotlib_lifecycle.py`

English:
    .. todo:: English Translation

Polish:
    #. Opracuj podobny wykres dla danych Irysów
    #. Weź pod uwagę jedynie ``sepal_length`` oraz ``species``
    #. Species ma być w osi ``y``
    #. Na osi ``x`` ma być ``sepal_length``
    #. Czerwony marker opisuje średnią długość ``sepal_length`` dla wszystkich gatunków

Given:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'
