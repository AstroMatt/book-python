*************
Import/Export
*************

Reading data
============
* ``with open('filename.csv')`` - context manager
* ``numpy.loadtxt('filename.csv', delimeter=',', unpack=True)``
* ``csv.DictReader()``
* ``pandas`` ``DataFrame``


``pandas`` and ``matplotlib``
=============================
* All of plotting functions expect ``np.array`` or ``np.ma.masked_array`` as input
* Classes that are 'array-like' such as ``pandas`` data objects and ``np.matrix`` may or may not work as intended
* It is best to convert these to ``np.array`` objects prior to plotting
* Convert a ``pandas.DataFrame``:

    .. code-block:: python

        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        np.random.seed(0)

        a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
        a_asndarray = a.values

Exporting
=========
.. glossary::

    eps
    pdf
    png
    ps
    svg
    raster graphics
    vector graphics

.. csv-table::
    :header: "Renderer", "Filetypes", "Type", "Description"

    "AGG", ":term:`png`", ":term:`raster graphics`", "High quality images using the Anti-Grain Geometry engine"
    "PS", ":term:`ps`, :term:`eps`", ":term:`vector graphics`", "Postscript output"
    "PDF", ":term:`pdf`", ":term:`vector graphics`", "Portable Document Format"
    "SVG", ":term:`svg`", ":term:`vector graphics`", "Scalable Vector Graphics"
    "Cairo", ":term:`png`, :term:`svg`", ":term:`raster graphics`, :term:`vector graphics`", "using the Cairo graphics library"


