***********
Plot Styles
***********


Axis naming
===========
.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1,2,3]
    y = [4,5,6]

    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    plt.plot(x, y)
    plt.show()


Title
=====
.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1,2,3]
    y = [4,5,6]

    plt.title('This is my chart')

    plt.plot(x, y)
    plt.show()

.. code-block:: python

    import matplotlib.pyplot as plt


    x = [1,2,3]
    y = [4,5,6]

    plt.title('This is my chart\nSecond line')

    plt.plot(x, y)
    plt.show()


Legend
======
* Good practice: always have labels

.. code-block:: python

    import matplotlib.pyplot as plt


    x1 = [1,2,3]
    y1 = [4,5,6]

    x2 = [1,2,3]
    y2 = [10,11,12]

    plt.plot(x1, y1, label='first line')
    plt.plot(x2, y2, label='second line')

    plt.legend()
    plt.show()


Colors
======
* first color name letter (not recommended):

    * ``r`` - red
    * ``g`` - green
    * ``b`` - blue
    * ``c`` - cyan
    * ``m`` - magenta
    * ``y`` - yellow
    * ``k`` - karmin
    * ``w`` - white

* color names (X11/CSS4):

    * red
    * green
    * blue
    * cyan
    * magenta
    * yellow
    * karmin
    * white
    * https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart

* hexadecimal code (RGB or RGBA):

    * ``#FF0000`` - red
    * ``#00FF00`` - green
    * ``#0000FF`` - blue
    * ``#FF000033`` - semi-transparent red

* tuple (RGB or RGBA):

    * ``(0.1, 0.2, 0.5)``
    * ``(0.1, 0.2, 0.5, 0.3)``

.. code-block:: python

    plt.bar(x1, y1, label='Bars 1', color='blue')
    plt.bar(x2, y2, label='Bars 2', color='red')


Line styles
===========
* Other line styles https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html#sphx-glr-gallery-lines-bars-and-markers-linestyles-py

.. figure:: img/matplotlib-plt-linestyle-basic.png
    :width: 75%
    :align: center

    Basic line styles

.. figure:: img/matplotlib-plt-linestyle-advanced.png
    :width: 75%
    :align: center

    Advanced line styles

.. code-block:: python

    pylab.plot(x, y, color="red", linestyle='--')

.. csv-table:: ``fmt`` parameters
    :header-rows: 1

    "Character", "Description"
    "``-``",  "solid line style"
    "``--``", "dashed line style"
    "``-.``", "dash-dot line style"
    "``:``",  "dotted line style"
    "``.``",  "point marker"
    "``,``",  "pixel marker"
    "``o``",  "circle marker"
    "``v``",  "triangle_down marker"
    "``^``",  "triangle_up marker"
    "``<``",  "triangle_left marker"
    "``>``",  "triangle_right marker"
    "``1``",  "tri_down marker"
    "``2``",  "tri_up marker"
    "``3``",  "tri_left marker"
    "``4``",  "tri_right marker"
    "``s``",  "square marker"
    "``p``",  "pentagon marker"
    "``*``",  "star marker"
    "``h``",  "hexagon1 marker"
    "``H``",  "hexagon2 marker"
    "``+``",  "plus marker"
    "``x``",  "x marker"
    "``D``",  "diamond marker"
    "``d``",  "thin_diamond marker"
    "``|``",  "vline marker"
    "``_``",  "hline marker"


Line2D parameters
=================
.. csv-table:: Line2D parameters
    :header: "Property", "Value Type"
    :widths: 30, 70

    "``alpha``",                       "float"
    "``animated``",                    "[True | False]"
    "``antialiased`` or ``aa``",       "[True | False]"
    "``clip_box``",                    "a matplotlib.transform.Bbox instance"
    "``clip_on``",                     "[True | False]"
    "``clip_path``",                   "a Path instance and a Transform instance, a Patch"
    "``color`` or ``c``",              "any matplotlib color"
    "``contains``",                    "the hit testing function"
    "``dash_capstyle``",               "[``'butt'`` | ``'round'`` | ``'projecting'``]"
    "``dash_joinstyle``",              "[``'miter'`` | ``'round'`` | ``'bevel'``]"
    "``dashes``",                      "sequence of on/off ink in points"
    "``data``",                        "(np.array xdata, np.array ydata)"
    "``figure``",                      "a matplotlib.figure.Figure instance"
    "``label``",                       "any string"
    "``linestyle`` or ``ls``",         "[ ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'steps'`` | ...]"
    "``linewidth`` or ``lw``",         "float value in points"
    "``lod``",                         "[True | False]"
    "``marker``",                      "[ ``'+'`` | ``','`` | ``'.'`` | ``'1'`` | ``'2'`` | ``'3'`` | ``'4'`` ]"
    "``markeredgecolor`` or ``mec``",  "any matplotlib color"
    "``markeredgewidth`` or ``mew``",  "float value in points"
    "``markerfacecolor`` or ``mfc``",  "any matplotlib color"
    "``markersize`` or ``ms``",        "float"
    "``markevery``",                   "[ None | integer | (startind, stride) ]"
    "``picker``",                      "used in interactive line selection"
    "``pickradius``",                  "the line pick selection radius"
    "``solid_capstyle``",              "[``'butt'`` | ``'round'`` | ``'projecting'``]"
    "``solid_joinstyle``",             "[``'miter'`` | ``'round'`` | ``'bevel'``]"
    "``transform``",                   "a matplotlib.transforms.Transform instance"
    "``visible``",                     "[True | False]"
    "``xdata``",                       "np.array"
    "``ydata``",                       "np.array"
    "``zorder``",                      "any number"
