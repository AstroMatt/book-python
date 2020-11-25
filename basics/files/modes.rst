.. _Files Modes:

**********
File Modes
**********


Rationale
=========
By type:

    * Text - easy to read and write
    * Binary - Fast and efficient

By operation:

    * Read - Get data from file
    * Write - Save data to file (overwrite existing data)
    * Append - Add line to file
    * Update - Read and Write (rarely used)

If mode is not specified it will read in text mode (``mode='rt'``)

.. code-block:: python

    open('myfile.txt')


Short Notation
==============
.. highlights::
    * Most commonly used
    * By default text mode is used
    * ``mode='r'`` - read in text mode
    * ``mode='w'`` - write in text mode
    * ``mode='a'`` - append in text mode

.. code-block:: python

    open('myfile.txt', mode='r')
    open('myfile.txt', mode='w')
    open('myfile.txt', mode='a')


Text Mode
=========
.. highlights::
    * Text - easy to read and write
    * ``mode='rt'`` - read in text mode (default)
    * ``mode='wt'`` - write in text mode
    * ``mode='at'`` - append in text mode

.. code-block:: python

    open('myfile.txt', mode='rt')
    open('myfile.txt', mode='wt')
    open('myfile.txt', mode='at')


Binary Mode
===========
.. highlights::
    * Binary - Fast and efficient
    * ``mode='rb'`` - read in binary mode
    * ``mode='wb'`` - write in binary mode
    * ``mode='ab'`` - append in binary mode

.. code-block:: python

    open('myfile.txt', mode='rb')
    open('myfile.txt', mode='wb')
    open('myfile.txt', mode='ab')


Update Mode
===========
.. highlights::
    * Reading and Writing
    * Text mode is used if not specified otherwise
    * ``mode='r+'`` - read in text mode
    * ``mode='w+'`` - write in text mode
    * ``mode='a+'`` - append in text mode
    * ``mode='rt+'`` - update in text mode
    * ``mode='wt+'`` - update in text mode
    * ``mode='at+'`` - update in text mode
    * ``mode='rb+'`` - update in binary mode
    * ``mode='wb+'`` - update in binary mode
    * ``mode='ab+'`` - update in binary mode

.. code-block:: python

    open('myfile.txt', mode='r+')
    open('myfile.txt', mode='w+')
    open('myfile.txt', mode='a+')

    open('myfile.txt', mode='rt+')
    open('myfile.txt', mode='wt+')
    open('myfile.txt', mode='at+')

    open('myfile.txt', mode='rb+')
    open('myfile.txt', mode='wb+')
    open('myfile.txt', mode='ab+')


Recap
=====
Most common (90% of time):

    * ``mode='r'`` - read in text mode
    * ``mode='w'`` - write in text mode
    * ``mode='a'`` - append in text mode

Text Mode:

    * ``mode='rt'`` - read in text mode (default)
    * ``mode='wt'`` - write in text mode
    * ``mode='at'`` - append in text mode

Binary Mode:

    * ``mode='rb'`` - read in binary mode
    * ``mode='wb'`` - write in binary mode
    * ``mode='ab'`` - append in binary mode

Update (rarely used):

    * ``mode='rb+'`` - update in binary mode
    * ``mode='wb+'`` - update in binary mode
    * ``mode='ab+'`` - update in binary mode
    * ``mode='r+'`` - read in text mode
    * ``mode='w+'`` - write in text mode
    * ``mode='a+'`` - append in text mode

* If mode is not specified it will read in text mode (``mode='rt'``)


Assignments
===========

.. todo:: Create assignments
