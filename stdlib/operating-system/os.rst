.. _Stdlib OS:

****************
Operating System
****************


Bitwise operators
=================
* ``|`` - OR
* ``&`` - AND
* ``~`` - NOT
* ``^`` - XOR
* ``<<`` - Shift left
* ``>>`` - Shift right

.. code-block:: python

    0 ^ 0  # 0
    1 ^ 1  # 0
    1 ^ 0  # 1
    0 ^ 1  # 1
    8 ^ 5  # 13

.. code-block:: text

    1000  # 8 (binary)
    0101  # 3 (binary)
    ----  # APPLY XOR ('vertically')
    1101  # result = 13 (dec)


Accessing Environmental Variables
=================================
.. code-block:: python

    import os

    os.getenv('HOME')  # /home/jose


Getting filenames and extensions
================================

Extensions
----------
.. code-block:: python

    import os

    path, ext = os.path.splitext(r'c:\Python\README.rst')
    path        # 'c:\\Python\\README'
    ext         # '.rst'

Checking OS version
===================
* Linux: Linux
* Mac: Darwin
* Windows: Windows

``platform``
------------
.. code-block:: python

    import platform

    platform.system()                           # Windows
    platform.release()                          # 7
    platform.platform()                         # 'Windows-7-6.1.7601-SP1'
    platform.os.name                            # 'nt'

    platform.uname()
    # uname_result(
    #     system='Windows',
    #     node='Lenovo-Komputer',
    #     release='7',
    #     version='6.1.7601',
    #     machine='AMD64',
    #     processor='Intel64 Family 6 Model 42 Stepping 7, GenuineIntel')
    #
    # uname_result(
    #     system='Darwin',
    #     node='mainframe.local',
    #     release='15.3.0',
    #     version='Darwin Kernel Version 15.3.0: Thu Dec 10 18:40:58 PST 2015; root:xnu-3248.30.4~1/RELEASE_X86_64',
    #     machine='x86_64',
    #     processor='i386')

``os``
------
.. code-block:: python

    import os

    os.name         # 'nt'
    os.name         # 'posix'

``psutil``
----------
.. code-block:: python

    import psutil

    psutil.OSX      # False
    psutil.WINDOWS  # True
    psutil.LINUX    # False

``sys``
-------
.. code-block:: python

    import sys

    sys.platform    # 'win32'


``sys``
=======

Most commonly used methods
--------------------------
.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.platform
    sys.path.insert(0, '/path/to/directory')
    sys.path.insert(index=0, object='/path/to/directory')

System exit and exit codes
--------------------------
.. code-block:: python

    import sys

    sys.exit(0)

.. csv-table:: System Exit Codes
    :header-rows: 1
    :file: data/system-exit-codes.csv


``os``
======
.. code-block:: python

    import os

    os.walk()
    os.scandir()
    os.getcwd()
    os.stat()

    os.is_dir()
    os.is_file()
    os.is_symlink()

    os.path.join()
    os.path.abspath()
    os.path.dirname()
    os.path.basename()

    os.mkdir()
    os.remove()
    os.rmdir()

.. code-block:: python

    import os

    os.path.isdir(os.path.join("c:", "\\", "Users"))    # True
    os.path.isdir(os.path.join("c:", "/", "Users"))     # True
    os.path.isdir(os.path.join("c:", os.sep, "Users"))  # True

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)
    print(path)

.. code-block:: python

    import os
    from os.path import getsize


    for root, dirs, files in os.walk('/home/'):
        size = sum(getsize(os.path.join(root, name)) for name in files)
        count = len(files)
        print(f'Size: {size} bytes in {count} non-directory files')

        # skip ``.git`` directories
        if '.git' in dirs:
            dirs.remove('.git')

.. code-block:: python

    # Delete everything reachable from the directory named in "top",
    # assuming there are no symbolic links.
    # CAUTION:  This is dangerous!  For example, if top == '/', it
    # could delete all your disk files.
    import os

    for root, dirs, files in os.walk(top, topdown=False):

        for name in files:
            os.remove(os.path.join(root, name))

        for name in dirs:
            os.rmdir(os.path.join(root, name))

Stats and permissions
---------------------
.. code-block:: python

    import os

    file = os.stat(r'/tmp/myfile.py')

    print(file)
    # os.stat_result(
    #     st_mode=33206,
    #     st_ino=3659174697409906,
    #     st_dev=3763209288,
    #     st_nlink=1,
    #     st_uid=0,
    #     st_gid=0,
    #     st_size=780,
    #     st_atime=1530775767,
    #     st_mtime=1530775767,
    #     st_ctime=1523261133)

    oct(file.st_mode)
    # 0o100666

Permissions
-----------
.. code-block:: python

    import os

    os.access(r'C:\Python\README.rst', os.R_OK)     # True
    os.access(r'C:\Python\README.rst', os.W_OK)     # True
    os.access(r'C:\Python\README.rst', os.X_OK)     # True

    os.access(r'C:\Python\notREADME.rst', os.R_OK)  # False
    os.access(r'C:\Python\notREADME.rst', os.W_OK)  # False
    os.access(r'C:\Python\notREADME.rst', os.X_OK)  # False


``subprocess``
==============

Most commonly used methods
--------------------------
.. code-block:: python

    import subprocess

    subprocess.call('clear')
    subprocess.run()    # preferred over ``Popen()`` for Python >= 3.5
    subprocess.Popen()

``subprocess.run()``
--------------------
* New in Python 3.5
* Preferred

.. code-block:: python

    subprocess.run(
        args,
        stdin=None,
        stdout=None,
        stderr=None,
        shell=False,
        timeout=None,  # important
        check=False,
        encoding=None
        # ... there are other, less commonly used parameters
    )

``shell=True``
--------------
Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process, and tell it to run the command. In other words, using an intermediate shell means that variables, glob patterns, and other special shell features in the command string are processed before the command is run. Here, in the example, ``$HOME`` was processed before the echo command. Actually, this is the case of command with shell expansion while the command ``ls -l`` considered as a simple command.

.. note:: source: `Subprocess Module <https://stackoverflow.com/a/36299483/228517>`

.. code-block:: python

    import subprocess

    subprocess.call('echo $HOME')
    # OSError: [Errno 2] No such file or directory

.. code-block:: python

    import subprocess

    subprocess.call('echo $HOME', shell=True)
    # /home/jose-jimenez

Execute command in OS
---------------------
.. code-block:: python

    subprocess.run('ls -la /home')  # without capturing output

.. code-block:: python

    import os
    import subprocess

    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, 'README.rst')

    subprocess.run(f'echo "ehlo world" > {path}')

.. code-block:: python

    import subprocess

    cmd = 'dir ..'

    result = subprocess.run(
        cmd,
        timeout=2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')

    print(result.stdout)
    print(result.stderr)

.. code-block:: python

    subprocess.run("exit 1", shell=True, check=True)
    # subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

.. code-block:: python

    subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE, encoding='utf-8')
    # CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
    #                  stdout='crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

Timeout for subprocesses
------------------------
.. code-block:: python

    import subprocess
    cmd = ['ping', 'nasa.gov']

    try:
        subprocess.run(cmd, timeout=5)
    except subprocess.TimeoutExpired:
        print('process ran too long')

Stdout and Stderr
-----------------
.. code-block:: python

    import logging
    import subprocess
    import shlex


    def run(command, timeout=15, clear=True):

        if clear:
            subprocess.call('clear')

        logging.debug(f'Execute: {command}\n')

        result = subprocess.run(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            timeout=timeout,
            encoding='utf-8')

        if result.stdout:
            logging.info(f'{result.stdout}')

        if result.stderr:
            logging.warning(f'{result.stderr}')

        return result

Parsing and sanitizing arguments
--------------------------------
.. code-block:: python

    import shlex
    import subprocess

    command_line = input()
    # /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"

    cmd = shlex.split(command_line)
    # ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]

    subprocess.run(cmd)

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'dir ..'

    result = subprocess.run(
        shlex.split(cmd),  # ['dir', '..']
        timeout=2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')

    print(result.stdout)
    print(result.stderr)


``tempfile``
============

Creating temporary files
------------------------
.. code-block:: python

    import tempfile

    with tempfile.TemporaryFile() as file:
        file.write(b'Hello world!')
        file.seek(0)
        file.read()  # b'Hello world!'

    # file is now closed and removed

Creating temporary directories
------------------------------
.. code-block:: python

    with tempfile.TemporaryDirectory() as dir:
        print('created temporary directory', dir)

    # directory and contents have been removed


``io``
======
* ``io`` to biblioteka do obsługi strumienia wejściowego i wyjściowego
* StringIO jest wtedy traktowany jak plik wejściowy.

.. code-block:: python

    import io

    io.StringIO
    io.BytesIO

.. code-block:: python

    f = open("myfile.txt", "r", encoding="utf-8")
    f = io.StringIO("some initial text data")

.. code-block:: python

    f = open("myfile.jpg", "rb")
    f = io.BytesIO(b"some initial binary data: \x00\x01")

.. code-block:: python

    import io

    result = io.StringIO()
    result.write('First line.\n')
    print('Second line.', file=result)

    # Retrieve file contents -- this will be
    # 'First line.\nSecond line.\n'
    contents = result.getvalue()

    # Close object and discard memory buffer --
    # .getvalue() will now raise an exception.
    result.close()

.. code-block:: python

    result = io.BytesIO(b"abcdef")
    view = result.getbuffer()
    view[2:4] = b"56"
    result.getvalue()  # b'ab56ef'


``configparser``
================

Writing configuration
---------------------
.. code-block:: python

    import configparser

    config = configparser.ConfigParser()

    config['DEFAULT'] = {'ServerAliveInterval': '45',
                          'Compression': 'yes',
                          'CompressionLevel': '9'}

    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}

    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'
    topsecret['ForwardX11'] = 'no'
    config['DEFAULT']['ForwardX11'] = 'yes'

    with open('example.ini', 'w') as configfile:
        config.write(configfile)

.. code-block:: ini

    [DEFAULT]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes

    [bitbucket.org]
    User = hg

    [topsecret.server.com]
    Port = 50022
    ForwardX11 = no

Reading configuration
---------------------
.. code-block:: python

    import configparser

    config = configparser.ConfigParser()

    config.read('example.ini')          # ['example.ini']
    config.sections()                   # ['bitbucket.org', 'topsecret.server.com']

    'bitbucket.org' in config           # True
    'example.com' in config             # False

    config['bitbucket.org']['User']     # 'hg'
    config['DEFAULT']['Compression']    # 'yes'

    config.getboolean('BatchMode', fallback=True)        # True
    config.getfloat('DEFAULT', 'a_float', fallback=0.0)  # 0.0
    config.getint('DEFAULT', 'an_int', fallback=0)       # 0

    topsecret = config['topsecret.server.com']
    topsecret.get('ForwardX11', 'yes')          # 'no'
    topsecret.get('Port', 8000)                 # '50022'


    for key in config['bitbucket.org']:  # 'bitbucket.org' has laso entries from DEFAULT
        print(key)

        # user
        # compressionlevel
        # serveraliveinterval
        # compression
        # forwardx11

Alternative syntax and using variables in config
------------------------------------------------
.. code-block:: ini

    [Common]
    home_dir: /Users
    library_dir: /Library
    system_dir: /System
    macports_dir: /opt/local

    [Frameworks]
    Python: 3.2
    path: ${Common:system_dir}/Library/Frameworks/

    [Arthur]
    nickname: Two Sheds
    last_name: Jackson
    my_dir: ${Common:home_dir}/twosheds
    my_pictures: ${my_dir}/Pictures
    python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}



Running commands in parallel across many hosts
==============================================
* https://linux.die.net/man/1/pssh

.. figure:: img/system-pssh-1.jpg
    :align: center
    :width: 75%

.. figure:: img/system-pssh-2.jpg
    :align: center
    :width: 75%

.. figure:: img/system-pssh-3.png
    :align: center
    :width: 75%


Passwords and secrets
=====================
* UMASK
* Sticky bit
* setuid
* configparser


Allegro Tipboard
================
* http://allegro.tech/tipboard/
* https://github.com/allegro/tipboard

Tipboard is a system for creating dashboards, written in JavaScript and Python. Its widgets ('tiles' in Tipboard's terminology) are completely separated from data sources, which provides great flexibility and relatively high degree of possible customizations.

Because of its intended target (displaying various data and statistics in your office), it is optimized for larger screens.

Similar projects: Geckoboard, Dashing.

.. code-block:: console

    $ pip install tipboard
    $ tipboard create_project my_test_dashboard
    $ tipboard runserver


Assignments
===========

Recursive folders walking
-------------------------
* Assignment name: Recursive folders walking
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/system_walk.py`

:English:
    .. todo:: English Translation

:Polish:
    #. Sprawdź czy katalog "Python" już istnieje na pulpicie w Twoim systemie
    #. Jeżeli nie istnieje to za pomocą ``os.mkdir()`` stwórz go w tym miejscu
    #. Za pomocą ``subprocess.call()`` w tym katalogu stwórz plik ``README.rst`` i dodaj do niego tekst "Ehlo World"
    #. Przeszukaj rekurencyjnie wszystkie katalogi na pulpicie
    #. Znajdź wszystkie pliki ``README`` (z dowolnym rozszerzeniem)
    #. Wyświetl ich zawartość za pomocą polecenia:

        * ``cat`` (macOS, Linux)
        * ``type`` (Windows)

    #. Ścieżkę do powyższego pliku ``README`` skonstruuj za pomocą ``os.path.join()``
    #. Ścieżka ma być względna w stosunku do pliku, który aktualnie jest uruchamiany
    #. Jeżeli po przeszukaniu całego Pulpitu rekurencyjnie skrypt nie znajdzie pliku ``LICENSE.rst``, to ma rzucić informację ``logging.critical()`` i wyjść z kodem błędu ``1``.

:Hints:
    * Gdyby był problem ze znalezieniem pliku, a ścieżka jest poprawna to zastosuj ``shell=True``
    * ``os.walk()``
    * ``subprocess.run()``

:Co to zadanie sprawdza?:
    * Przeglądanie katalogów i algorytm przeszukiwania
    * Sanityzacja parametrów
    * Logowanie wydarzeń w programie
    * Uruchamianie poleceń w systemie
    * Przechwytywanie outputu poleceń
    * Kody błędów
    * Przechodzenie do katalogów
    * Ścieżki względne i bezwzględne
    * Łączenie ścieżek

Tree
----
* Assignment name: Tree
* Last update: 2020-10-01
* Complexity level: hard
* Lines of code to write: 60 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/system_tree.py`

:English:
    .. todo:: English Translation

:Polish:
    #. Za pomocą znaków unicode: "┣━", "┗━" , "┃  "
    #. Wygeneruj wynik przypominający wynik polecenia ``tree``.

:Output:
    .. code-block:: text

        root:.
        [.]
        ┣━[.idea]
        ┃  ┣━[scopes]
        ┃  ┃  ┗━scope_settings.xml
        ┃  ┣━.name
        ┃  ┣━demo.iml
        ┃  ┣━encodings.xml
        ┃  ┣━misc.xml
        ┃  ┣━modules.xml
        ┃  ┣━vcs.xml
        ┃  ┗━workspace.xml
        ┣━[test1]
        ┃  ┗━test1.txt
        ┣━[test2]
        ┃  ┣━[test2-2]
        ┃  ┃  ┗━[test2-3]
        ┃  ┃      ┣━test2
        ┃  ┃      ┗━test2-3-1
        ┃  ┗━test2
        ┣━folder_tree_maker.py
        ┗━tree.py

