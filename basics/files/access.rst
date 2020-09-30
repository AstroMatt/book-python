.. _Files Access Modes:

*****************
File Access Modes
*****************

Rationale
=========
* Text - easy to read and write
* Binary - Fast and efficient
* Read - Get data from file
* Write - Save data to file (overwrite existing data)
* Append - Add line to file
* Update - Read and Write
* If mode is not specified it will read in text mode (``mode='rt'``)

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        ...


Text Mode
=========
.. highlights::
    * Text - easy to read and write
    * ``mode='rt'`` - read in text mode (default)
    * ``mode='wt'`` - write in text mode
    * ``mode='at'`` - append in text mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='rt') as file:
        ...

    with open(FILE, mode='wt') as file:
        ...

    with open(FILE, mode='at') as file:
        ...


Binary Mode
===========
.. highlights::
    * Binary - Fast and efficient
    * ``mode='rb'`` - read in binary mode
    * ``mode='wb'`` - write in binary mode
    * ``mode='ab'`` - append in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='rb') as file:
        ...

    with open(FILE, mode='wb') as file:
        ...

    with open(FILE, mode='ab') as file:
        ...

Update in Text Mode
===================
.. highlights::
    * Reading and Writing
    * ``mode='rt+'`` - update in binary mode
    * ``mode='wt+'`` - update in binary mode
    * ``mode='at+'`` - update in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='rt+') as file:
        ...

    with open(FILE, mode='wt+') as file:
        ...

    with open(FILE, mode='at+') as file:
        ...


Update in Binary Mode
=====================
.. highlights::
    * Reading and Writing
    * ``mode='rb+'`` - update in binary mode
    * ``mode='wb+'`` - update in binary mode
    * ``mode='ab+'`` - update in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='rb+') as file:
        ...

    with open(FILE, mode='wb+') as file:
        ...

    with open(FILE, mode='ab+') as file:
        ...


Short Notation
==============
.. highlights::
    * By default text mode is used
    * Most commonly used
    * ``mode='r'`` - read in text mode
    * ``mode='w'`` - write in text mode
    * ``mode='a'`` - append in text mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='r') as file:
        ...

    with open(FILE, mode='w') as file:
        ...

    with open(FILE, mode='a') as file:
        ...


Short Notation Update Mode
==========================
.. highlights::
    * By default text mode is used
    * ``mode='r+'`` - read in text mode
    * ``mode='w+'`` - write in text mode
    * ``mode='a+'`` - append in text mode

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='r+') as file:
        ...

    with open(FILE, mode='w+') as file:
        ...

    with open(FILE, mode='a+') as file:
        ...


Recap
=====
* ``mode='r'`` - read in text mode
* ``mode='w'`` - write in text mode
* ``mode='a'`` - append in text mode

* ``mode='rt'`` - read in text mode (default)
* ``mode='wt'`` - write in text mode
* ``mode='at'`` - append in text mode

* ``mode='rb'`` - read in binary mode
* ``mode='wb'`` - write in binary mode
* ``mode='ab'`` - append in binary mode

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
        with open(FILE) as file:
            print(file.read())

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')


Assignments
===========

File Access Error
-----------------
* Assignment name: File Access Error
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 3 min
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

