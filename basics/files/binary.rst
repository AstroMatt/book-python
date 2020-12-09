.. _Files Binary:

************
Files Binary
************


Rationale
=========
* Text I/O over a binary storage (such as a file) is significantly slower than binary I/O over the same storage
* It requires conversions between unicode and binary data using a character codec
* This can become noticeable handling huge amounts of text data like large log files
* Source: https://docs.python.org/3/library/io.html#id3


Write Binary
============
* ``mode='wb'`` - write in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.bin'
    DATA = 'We choose to go to the Moon...'
    data = DATA.encode()

    with open(FILE, mode='wb') as file:
        file.write(data)


Append Binary
=============
* ``mode='ab'`` - append in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.bin'
    DATA = 'We choose to go to the Moon...'
    data = DATA.encode()

    with open(FILE, mode='ab') as file:
        file.write(data)


Read Binary
===========
* ``mode='rb'`` - read in binary mode

.. code-block:: python

    FILE = r'/tmp/myfile.bin'

    with open(FILE, mode='rb') as file:
        data = file.read()

    result = data.decode()
    print(result)


Pickle
======
* Works with any Python object (variables, functions, classes, nested objects)
* More information in :ref:`Serialization Pickle`

.. code-block:: python
    :caption: Write binary data to file

    import pickle

    FILE = r'/tmp/myfile.pkl'
    data = [1, 2, 3]

    with open(FILE, mode='wb') as file:
        pickle.dump(data, file)

.. code-block:: python
    :caption: Load binary data from file

    import pickle

    FILE = r'/tmp/myfile.pkl'

    with open(FILE, mode='rb') as file:
        result = pickle.load(file)

    print(result)



Seek
====
* Go to the n-th byte in the file
* Supports negative index (from end of file)

.. code-block:: python

    FILE = r'/tmp/myfile.bin'


    with open(FILE, mode='wb') as file:
        file.write(b'0123456789abcdef')

    with open(FILE, mode='rb') as file:
        file.seek(5)      # Go to the 6th byte in the file
        # 5

        file.read(1)
        # b'5'

        file.seek(-3, 2)  # Go to the 3rd byte before the end
        # 13

        file.read(1)
        # b'd'
