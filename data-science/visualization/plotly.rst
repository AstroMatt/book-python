******
Plotly
******

Installation
============
.. code-block:: console

    $ pip install plotly

Offline usage
=============
.. code-block:: python

    # Change from (this will upload chart to plot.ly)
    import plotly.plotly as py

    # to (this will render chart offline - on your computer)
    import  plotly.offline as py

Jupyter Usage
=============
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go


    x = [1, 2, 3, 4]
    y = [4, 3, 2, 1]


    # For in script chart rendering
    py.plot({
        "data": [go.Scatter(x=x, y=y)],
        "layout": go.Layout(title="hello world")
    })

    # If you want to use Plotly with Jupyter
    # Note the ``i`` before ``plot``
    py.iplot({
        "data": [go.Scatter(x=x, y=y)],
        "layout": go.Layout(title="hello world")
    })


Plot Controls & IPython widgets
===============================
.. literalinclude:: src/plotly-controls.py
    :language: python
    :caption: Plot Controls & IPython widgets

Charts
======

Tabl
-----
.. literalinclude:: src/plotly-table.py
    :language: python
    :caption: Plotting Table

Bars
----

Simple Bars
^^^^^^^^^^^
.. literalinclude:: src/plotly-bars-simple.py
    :language: python
    :caption: Simple Bars

Multi Bars
^^^^^^^^^^
.. literalinclude:: src/plotly-bars-simple.py
    :language: python
    :caption: Multi Bars

Box Plot
--------

Basic Box Plot
^^^^^^^^^^^^^^
.. literalinclude:: src/plotly-box-basic.py
    :language: python
    :caption: Basic Box Plot

Colored Box Plot
^^^^^^^^^^^^^^^^
.. literalinclude:: src/plotly-box-colored.py
    :language: python
    :caption: Colored Box Plot

Grouped Box Plot
^^^^^^^^^^^^^^^^
.. literalinclude:: src/plotly-box-grouped.py
    :language: python
    :caption: Grouped Box Plot

Outliers
^^^^^^^^
.. literalinclude:: src/plotly-box-outliers.py
    :language: python
    :caption: Outliers

Line Chart
----------
.. literalinclude:: src/plotly-line-chart.py
    :language: python
    :caption: Line Chart

Time Series
===========

Simple Time Series
------------------
.. literalinclude:: src/plotly-timeseries-simple.py
    :language: python
    :caption: Simple Time Series

Timeseries Range
----------------
.. literalinclude:: src/plotly-timeseries-range.py
    :language: python
    :caption: Timeseries Range

Rangeslider
-----------
.. literalinclude:: src/plotly-timeseries-rangeslider.py
    :language: python
    :caption: Timeseries Range

Two plots
=========

Multiple x-axis
---------------
.. literalinclude:: src/plotly-multiaxis-x.py
    :language: python
    :caption: Multiple x-axis

Multiple y-axis
---------------
.. literalinclude:: src/plotly-multiaxis-x.py
    :language: python
    :caption: Multiple y-axis

Line Plot Modes
---------------
.. literalinclude:: src/plotly-multiaxis-modes.py
    :language: python
    :caption: Line Plot Modes

Labels with annotations
-----------------------
.. literalinclude:: src/plotly-multiaxis-annotations.py
    :language: python
    :caption: Labels with annotations

Filled Line
-----------
.. literalinclude:: src/plotly-multiaxis-filled.py
    :language: python
    :caption: Filled Line

3D Plotting
===========

Simple
------
.. literalinclude:: src/plotly-3d-simple.py
    :language: python
    :caption: Simple 3D Plotting
