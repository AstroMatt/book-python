.. _Stdlib Pathlib:

*******
Pathlib
*******


Getting filenames and extensions
================================

Extensions
----------
.. code-block:: python

    import pathlib

    pathlib.Path('my/library/setup.py').suffix   # '.py'
    pathlib.Path('my/library.tar.gz').suffix     # '.gz'
    pathlib.Path('my/library').suffix            # ''
    pathlib.Path('my/library.tar.gar').suffixes  # ['.tar', '.gar']
    pathlib.Path('my/library.tar.gz').suffixes   # ['.tar', '.gz']
    pathlib.Path('my/library').suffixes          # []

Filenames
---------
.. code-block:: python

    import pathlib

    pathlib.Path('//some/share/setup.py').name  # 'setup.py'
    pathlib.Path('//some/share').name           # ''
    pathlib.Path('my/library.tar.gz').stem      # 'library.tar'
    pathlib.Path('my/library.tar').stem         # 'library'
    pathlib.Path('my/library').stem             # 'library'


System ``os`` vs. ``pathlib``
=============================
.. csv-table:: System ``os`` vs. ``pathlib``
    :header-rows: 1
    :file: data/system-os-vs-pathlib.csv

``.home()``
===========
.. code-block:: python

    import pathlib

    pathlib.home()  # WindowsPath('C:/Users/José')

``.drive``
==========
.. code-block:: python

    import pathlib

    PureWindowsPath('c:/Program Files/').drive  # 'c:'
    PureWindowsPath('/Program Files/').drive    # ''
    PurePosixPath('/etc').drive                 # ''

``.parents``
============
.. code-block:: python

    import pathlib

    p = PureWindowsPath('c:/foo/bar/setup.py')

    p.parents[0]    # PureWindowsPath('c:/foo/bar')
    p.parents[1]    # PureWindowsPath('c:/foo')
    p.parents[2]    # PureWindowsPath('c:/')

``.parent``
===========
.. code-block:: python

    import pathlib

    p = PurePosixPath('/a/b/c/d')
    p.parent        # PurePosixPath('/a/b/c')

``.as_posix()``
===============
.. code-block:: python

    import pathlib

    p = PureWindowsPath('c:\\windows')

    str(p)          # 'c:\\windows'
    p.as_posix()    # 'c:/windows'

``.as_uri()``
=============
.. code-block:: python

    import pathlib

    p = PurePosixPath('/etc/passwd')
    p.as_uri()      # 'file:///etc/passwd'

    p = PureWindowsPath('c:/Windows')
    p.as_uri()      # 'file:///c:/Windows'

``Path.chmod()``
================
.. code-block:: python

    import pathlib

    p = Path('setup.py')

    oct(p.stat().st_mode)  # 0o100775
    p.chmod(0o444)
    oct(p.stat().st_mode)  # 0o100444

``.glob()``
===========
.. code-block:: python

    import pathlib

    sorted(Path('.').glob('*.py'))
    # [PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]

    sorted(Path('.').glob('*/*.py'))
    # [PosixPath('docs/conf.py')]

    sorted(Path('.').glob('**/*.py'))
    # [PosixPath('docs/conf.py'), ...]

``.iterdir()``
==============
.. code-block:: python

    import pathlib

    p = Path('docs')

    for child in p.iterdir():
        print(child)

    # PosixPath('docs/conf.py')
    # PosixPath('docs/index.rst')
    # PosixPath('docs/Makefile')
    # PosixPath('docs/_build')
    # PosixPath('docs/_static')
    # PosixPath('docs/_templates')

joining paths
=============
.. code-block:: python

    from pathlib import Path

    directory = Path("/etc")
    filepath = directory / "my_file.txt"

    if filepath.exists():
        print('ok')
