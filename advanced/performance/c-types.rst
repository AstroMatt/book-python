*******
C Types
*******


Workflow
========

Code
----
.. code-block:: C

    long factorial(long n) {
        if (n == 0)
            return 1;

        return (n * factorial(n - 1));
    }

Build
-----
.. code-block:: console

    $ INCLUDES='-I/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/include/python3.7m/'
    $ FILE='my_library'
    $ gcc -fPIC -c -o ${FILE}.o ${FILE}.c ${INCLUDE}
    $ gcc -shared ${FILE}.o -o ${FILE}.so

Run
---
.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')

    lib.factorial(16)  # 2004189184
    lib.factorial(17)  # -288522240


Arguments
=========
* ``ctypes.c_double``
* ``ctypes.c_int``
* ``ctypes.c_char``
* ``ctypes.c_char_p``
* ``ctypes.POINTER(ctypes.c_double)``

.. code-block:: python

    lib.my_function.argtypes = [
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_double),
    ]

.. code-block:: python

    lib.my_function.restype = ctypes.c_char_p


Use cases
=========

Example 1
---------
.. code-block:: C

    #include <stdio.h>

    void ehlo() {
        printf("Ehlo World");
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')
    lib.ehlo()

Example 2
---------
.. code-block:: C

    #include <stdio.h>

    void greeting(char *name) {
        printf("Ehlo %s!\n", name);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')

    lib.greeting.argtypes = [ctypes.c_char_p]
    name = ctypes.create_string_buffer('Twardowski'.encode('ASCII'))
    lib.greeting(name)

Example 3
---------
.. code-block:: C

    #include <stdio.h>

    void number(int num) {
        printf("My number %d\n", num);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')
    lib.number(10)

Example 4
---------
.. code-block:: C

    int return_int(int num) {
        return num;
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')

    i = lib.return_int(15)
    print(i)

Multi OS code
-------------
.. code-block:: python

    import sys
    import ctypes


    if sys.platform == 'darwin':
       lib = ctypes.CDLL('/usr/lib/libc.dylib')
    elif sys.platform == 'win32':
        lib = ctypes.CDLL('/usr/lib/libc.dll')
    else:
        lib = ctypes.CDLL('/usr/lib/libc.so')


    lib.printf("I'm C printf() function called from Python")


.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')
    print(dir(lib))

Overflow
--------
.. code-block:: C

    #include <stdio.h>

    void wypisz_liczbe(int liczba) {
        printf("Liczba to: %d", liczba);
    }

.. code-block:: python

    import ctypes


    lib = ctypes.CDLL('my_library.so')

    lib.wypisz_liczbe(10 ** 10)  # Liczba to: 1410065408

    lib.wypisz_liczbe(10 ** 30)
    # Traceback (most recent call last):
    #   ...
    # ctypes.ArgumentError: argument 1: <class 'OverflowError'>: int too long to convert


Assignments
===========

C Types
-------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/ctypes_datetime.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Wykorzystując C Types wypisz datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``
