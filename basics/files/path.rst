.. _Files Path:

*********
File Path
*********


Rationale
=========
.. highlights::
    * Python works with both relative and absolute path
    * Path separator ``\`` (backslash) is used on Windows
    * Path separator ``/`` (slash) is used on ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)
    * In newer Windows versions both ``\`` and ``/`` works the same

.. code-block:: text
    :caption: Absolute path on Windows

    C:\Users\Watney\myfile.txt

.. code-block:: text
    :caption: Absolute path on ``*nix`` (Linux, macOS, BSD, etc.)

    /tmp/myfile.txt

.. code-block:: text
    :caption: Relative paths works the same on Windows and ``*nix`` (Linux, macOS, BSD, etc.)

    myfile.txt
    tmp/myfile.txt
    ../myfile.txt


Good Engineering Practices
==========================
.. highlights::
    * Never hardcode paths, use constant as a file name or file path
    * Convention (singular form): ``FILE``, ``FILENAME``, ``FILEPATH``, ``PATH``
    * Convention (plural form): ``FILES``, ``FILENAMES``, ``FILEPATHS``, ``PATHS``
    * Note, that ``PATH`` is usually used for other purposes (``sys.path`` or ``os.getenv('PATH')``)

.. code-block:: python

    FILE = 'myfile.txt'

.. code-block:: python

    FILES = [
        'myfile.txt',
        'myfile.csv']


Raw Strings
===========
.. highlights::
    * Always use raw-strings (``r"..."``) for paths
    * Escapes does not matters

.. code-block:: python

    print(r'C:\Users\Admin\file.txt')
    # C:\Users\Admin\file.txt

    print('C:\\Users\\Admin\\file.txt')
    # C:\Users\Admin\file.txt

    print('C:\Users\Admin\file.txt')
    # Traceback (most recent call last):
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex i.e. '\U0001F680' which is 🚀 emoticon
* ``s`` is invalid hexadecimal character
* Only valid characters are ``0123456789abcdefABCDEF``

.. code-block:: python

    import string

    print(string.hexdigits)
    # 0123456789abcdefABCDEF


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
    * "\\ " (backslash space) - escapes space
    * Note that in Python escapes in paths are not required

.. code-block:: python

    FILE = '/tmp/my file.txt'

    file = open(FILE)
    # Success!

.. code-block:: python

    FILE = r'/tmp/my file.txt'

    file = open(FILE)
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


Exception Handling
==================
.. code-block:: python

    try:
        file = open('/tmp/myfile.txt')
    except FileNotFoundError:
        print('Sorry, file not found')
    except PermissionError:
        print('Sorry, not permitted')


Create Directories
==================
.. code-block:: python

    from os import mkdir


    mkdir('/tmp/a')
    # directory /tmp/a created

    mkdir('/tmp/a/b/c')
    # Traceback (most recent call last):
    # FileNotFoundError: [Errno 2] No such file or directory: '/tmp/a/b/c'

.. code-block:: python

    from os import makedirs


    makedirs('/tmp/a')
    # directory /tmp/a created

    makedirs('/tmp/a')
    # Traceback (most recent call last):
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

.. literalinclude:: assignments/file_path_exception.py
    :caption: :download:`Solution <assignments/file_path_exception.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_abspath.py
    :caption: :download:`Solution <assignments/file_path_abspath.py>`
    :end-before: # Solution
