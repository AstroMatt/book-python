.. _Files Access Modes:

*****************
File Access Modes
*****************


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

    FILE = r'/tmp/myfile.txt'

    file = open(FILE)


Short Notation
==============
.. highlights::
    * Most commonly used
    * By default text mode is used
    * ``mode='r'`` - read in text mode
    * ``mode='w'`` - write in text mode
    * ``mode='a'`` - append in text mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE, mode='r')
    file = open(FILE, mode='w')
    file = open(FILE, mode='a')


Text Mode
=========
.. highlights::
    * Text - easy to read and write
    * ``mode='rt'`` - read in text mode (default)
    * ``mode='wt'`` - write in text mode
    * ``mode='at'`` - append in text mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE, mode='rt')
    file = open(FILE, mode='wt')
    file = open(FILE, mode='at')


Binary Mode
===========
.. highlights::
    * Binary - Fast and efficient
    * ``mode='rb'`` - read in binary mode
    * ``mode='wb'`` - write in binary mode
    * ``mode='ab'`` - append in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE, mode='rb')
    file = open(FILE, mode='wb')
    file = open(FILE, mode='ab')


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

    FILE = r'/tmp/myfile.txt'

    file = open(FILE, mode='r+')
    file = open(FILE, mode='w+')
    file = open(FILE, mode='a+')

    file = open(FILE, mode='rt+')
    file = open(FILE, mode='wt+')
    file = open(FILE, mode='at+')

    file = open(FILE, mode='rb+')
    file = open(FILE, mode='wb+')
    file = open(FILE, mode='ab+')


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


Exception Handling
==================
.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    try:
        file = open(FILE)
    except FileNotFoundError:
        print('File does not exist')
    except PermissionError:
        print('Permission denied')


Assignments
===========

File Access Error
-----------------
* Assignment name: File Access Error
* Last update: 2020-11-19
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 2 min
* Solution: :download:`solution/file_access_error.py`

:English:
    #. Using ``input()`` ask user for a file path
    #. Print file content
    #. Handle exception for not existing file
    #. Handle exception for not having sufficient permissions

:Polish:
    #. Używając ``input()`` zapytaj użytkownika o ścieżkę do pliku
    #. Wypisz zawartość pliku
    #. Obsłuż wyjątek dla nieistniejącego pliku
    #. Obsłuż wyjątek dla braku wystarczających uprawnień

