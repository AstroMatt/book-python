.. _CI/CD Type Checking:

*************
Type Checking
*************


``MyPy``
========
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True


``PyType``
==========
* https://github.com/google/pytype

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.7 FILE


``pyre-check``
==============
