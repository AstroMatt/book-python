.. _Module Import:

*************
Module Import
*************


Importing modules
=================

Import module
-------------
* ``import ...``

Syntax
^^^^^^
.. code-block:: python

    import module

.. code-block:: python

    import module.submodule

Example
^^^^^^^
.. code-block:: python

    import random

Importing function from module
------------------------------
* ``from ... import ...``

Syntax
^^^^^^
.. code-block:: python

    from module import function

.. code-block:: python

    from module.submodule import function

Example
^^^^^^^
.. code-block:: python

    from random import randint


Import and alias
----------------
* ``import ... as ...``

Syntax
^^^^^^
.. code-block:: python

    import module as alias

.. code-block:: python

    from module import function as alias

Example
^^^^^^^
.. code-block:: python

    import numpy as np

.. code-block:: python

    from django.utils.translation import gettext_lazy as _

Relative imports
----------------
* ``from . import ...``
* ``from .. import ...``

Syntax
^^^^^^
.. code-block:: python

    from . import module

.. code-block:: python

    from .. import module

.. code-block:: python

    from .module import function

.. code-block:: python

    from ..module import function


What is Python Module
=====================
* Every Python file is a module
* Every directory with ``__init__.py`` file is a module
* Python does not recognize whether it is a file or dir with init
* Useful when you start simple, and then expand
* Usually ``__init__.py`` is empty
* If you define ``__all__: list[str]`` in ``__init__.py`` it will import only those functions when ``from MODULE import *``

Python file is a module
-----------------------
.. code-block:: python

    game.py

Directory with ``__init__.py`` file
-----------------------------------
.. code-block:: python

    game
        __init__.py

Importing from own modules
--------------------------
.. code-block:: python

    from game import run


Examples
========
.. code-block:: text

    game
        __init__.py
        config.py
        api.py
        dragon
            __init__.py
            wawelski.py
            red.py
            black.py
            white.py

Importing variable or constant from module
------------------------------------------
.. code-block:: python

    from game.config import RESOLUTION_X
    from game.config import RESOLUTION_Y

.. code-block:: python
    :caption: Preferred

    from game.config import RESOLUTION_X, RESOLUTION_Y

Importing submodules
--------------------
.. code-block:: python

    from game.dragon import red
    from game.dragon import white


    dragon1 = red.RedDragon()
    dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon import red, white

    dragon1 = red.RedDragon()
    dragon2 = white.WhiteDragon()

Importing all
-------------
.. code-block:: python

    from game.dragon import *

    dragon1 = red.RedDragon()
    dragon2 = white.WhiteDragon()

Importing objects from modules
------------------------------
.. code-block:: python

    from game.dragon.red import RedDragon
    from game.dragon.white import WhiteDragon

    dragon1 = RedDragon()
    dragon2 = WhiteDragon()

Importing with aliases
----------------------
.. code-block:: python

    from game.dragon.red import RedDragon as Smok

    dragon = Smok()


Import path
===========
* Watch-out module names which are the same as in stdlib

.. code-block:: python

    import sys

    sys.path
    # ['/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev',
    #  '/Users/Developer/my_project',
    #  '/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pycharm_display',
    #  '/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/third_party/thriftpy',
    #  '/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev',
    #  '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
    #  '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
    #  '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
    #  '/Users/matt/Developer/book-python/.venv-3.7.3/lib/python3.7/site-packages',
    #  '/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pycharm_matplotlib_backend']

    sys.path.append('/path/to/directory')
    sys.path.insert(0, '/path/to/directory')


``__name__``
============
* Zmienna ``__name__`` pozwala ustalić czy dany plik jest wykonywany czy importowany.
* Jeżeli dany plik jest wykonywany, zmienna ``__name__`` ustawiana jest na ``'__main__'``.
* Jeżeli dany plik jest importowany jako moduł, zmienna ``__name__`` ustawiana jest na nazwę modułu.
* Jest to przydatne na przykład przy testowaniu modułów.

Example 1
---------
* Wypisane na konsoli zostanie ``'hello world!'`` jeżeli dany plik jest uruchamiany z konsoli.
* Powyższy kod nie wykona się natomiast jeżeli plik zaimportujemy jako moduł w innym pliku.

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

Example 2
---------
* Jeżeli skrypt wywoływany jest z konsoli "z ręki" to uruchom funckję ``run()``
* Jeżeli został zaimportowany, to ten fragment będzie zignorowany
* I trzeba uruchomić funkcję ``run()`` samodzielnie - kontrolowanie

.. code-block:: python

    def run():
        ...

    if __name__ == '__main__':
        run()

Example
-------
.. code-block:: python

    import logging

    log = logging.getLogger(__name__)

