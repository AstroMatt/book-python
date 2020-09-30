.. _Files Path:

*********
File Path
*********


Rationale
=========
.. highlights::
    * Never hardcode paths (put path directly to open function)
    * Use constant as a file name or file path
    * Convention ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
    * Or their respective plural forms for multiple files
    * Note, that ``PATH`` is usually used for other purposes (``sys.path`` or ``os.getenv('PATH')``)
    * Always use raw-strings ``r"..."``
    * Paths on Windows uses ``\``
    * Paths on ``*nix`` uses ``/``
    * ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)
    * In newer Windows versions both ``\`` and ``/`` works


Absolute Path
=============
.. highlights::
    * Absolute path on Windows starts with drive letter
    * Absolute path on ``*nix`` starts with root ``/`` dir
    * Absolute path include all entries in the directories hierarchy

.. code-block:: python

    FILE = r'C:\Users\Watney\myfile.txt'

.. code-block:: python

    FILE = r'/tmp/myfile.txt'


Relative Path
=============
.. highlights::
    * Path is relative to currently running script
    * ``.`` - Current directory
    * ``..`` - Parent directory

.. code-block:: python

    FILE = r'myfile.txt'
    FILE = r'./myfile.txt'

    FILE = r'tmp/myfile.txt'
    FILE = r'./tmp/myfile.txt'

    FILE = r'../myfile.txt'
    FILE = r'../tmp/myfile.txt'

    FILE = r'../../myfile.txt'
    FILE = r'../../tmp/myfile.txt'


Escaping Characters in Path
===========================
.. highlights::
    * "\\ " (slash space) - escapes space
    * Note escapes are not needed

.. code-block:: python

    FILE = '/tmp/my file.txt'

    with open(FILE) as file:
        print(file.read())

    # Success!

.. code-block:: python

    FILE = r'/tmp/my file.txt'

    with open(FILE) as file:
        print(file.read())

    # Success!

.. code-block:: python

    FILE = r'C:\Users\Admin\myfile.txt'

    repr(FILE)
    # "'C:\\\\Users\\\\Admin\\\\myfile.txt'"

    str(FILE)
    # 'C:\\Users\\Admin\\myfile.txt'

    print(repr(FILE))
    # 'C:\\Users\\Admin\\myfile.txt'

    print(FILE)
    # C:\Users\Admin\myfile.txt

Create Directories
==================
.. code-block:: python

    from os import mkdir


    mkdir('/tmp/a')
    # directory /tmp/a created

    mkdir('/tmp/a/b/c')
    # FileNotFoundError: [Errno 2] No such file or directory: '/tmp/a/b/c'

.. code-block:: python

    from os import makedirs


    makedirs('/tmp/a')
    # directory /tmp/a created

    makedirs('/tmp/a')
    # FileExistsError: [Errno 17] File exists: '/tmp/a'

    makedirs('/tmp/a', exist_ok=True)
    # No error

    makedirs('/tmp/a/b/c')
    # directory /tmp/a/b/c created


Exists and is Directory or File
===============================
.. code-block:: python

    from pathlib import Path


    path = Path(r'/tmp/myfile.txt')

    path.exists()
    # True

    path.is_dir()
    # False

    path.is_file()
    # True

Current Working Directory
=========================
.. highlights::
    * Returns an absolute path to current working directory

.. code-block:: python

    from pathlib import Path

    Path.cwd()
    # PosixPath('/home/python/')


Convert Relative Path to Absolute
=================================
.. code-block:: python

    from pathlib import Path


    Path(Path.cwd(), 'myfile.txt')
    # PosixPath('/home/python/myfile.txt')


Script Path
===========
.. highlights::
    * Returns an absolute path to currently running script

.. code-block:: python

    print(__file__)
    # /home/python/myscript.py


Assignments
===========

File Path Abspath
-----------------
* Assignment name: File Path Abspath
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/file_path_abspath.py`

:English:
    #. Using ``input()`` ask user for a file path
    #. Convert path to absolute
    #. Print if path exists and leads to file or directory

:Polish:
    #. Używając ``input()`` zapytaj użytkownika o ścieżkę do pliku
    #. Przekonwertuj ścieżkę do bezwzględnej
    #. Wypisz czy ścieżka istnieje i czy prowadzi do pliku czy katalogu

