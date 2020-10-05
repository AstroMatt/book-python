.. _Stdlib Tempfile:

********
Tempfile
********


Create Temporary File
=====================
.. code-block:: python

    from tempfile import TemporaryFile


    file = TemporaryFile()
    file.write(b'Hello world!')
    file.seek(0)
    file.read()
    file.close()


Context Manager
===============
* preferred

.. code-block:: python

    from tempfile import TemporaryFile


    with TemporaryFile() as file:
        file.write(b'Hello world!')
        file.seek(0)
        file.read()


Temporary Directory
===================
.. code-block:: python

    from tempfile import TemporaryDirectory


    with TemporaryDirectory() as dir:
        print('created temporary directory', dir)
