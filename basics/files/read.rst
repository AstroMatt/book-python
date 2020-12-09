.. _Files Read:

*********
File Read
*********


Rationale
=========
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* Fails when file cannot be accessed
* Uses context manager
* ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='rt'``)


Read From File
==============
* Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE)
    data = file.read()
    file.close()


Read Using Context Manager
==========================
* Context managers use ``with ... as ...:`` syntax
* It closes file automatically upon block exit (dedent)
* Using context manager is best practice
* More information in :ref:`Protocol Context Manager`

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File at Once
=================
* Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File as List of Lines
==========================
 * Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.readlines()

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        lines = file.readlines()[1:30]

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        for line in file.readlines()[1:30]:
            print(line)

.. code-block:: python
    :caption: Read whole file and split by lines, separate header from content

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        header, *content = file.readlines()

        for line in content:
            print(line)


Reading File as Generator
=========================
* Use generator to iterate over other lines
* In those examples, ``file`` is a generator

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        for line in file:
            print(line)

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        header = file.readline()

        for line in file:
            print(line)


Examples
========
.. code-block:: python

    def isnumeric(x):
        try:
            float(x)
            return True
        except ValueError:
            return False


    def clean(line):
        line = line.strip().split(',')
        line = map(lambda x: float(x) if isnumeric(x) else x, line)
        return tuple(line)


    with open(FILE) as file:
        header = clean(file.readline())

        for line in file:
            line = clean(line)
            print(line)

.. code-block:: python

    total = 0

    with open(FILE) as file:
        for line in file:
            total += sum(float(line))

    print(total)


Assignments
===========

.. literalinclude:: assignments/file_read_str.py
    :caption: :download:`Solution <assignments/file_read_str.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_multiline.py
    :caption: :download:`Solution <assignments/file_read_multiline.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_csv.py
    :caption: :download:`Solution <assignments/file_read_csv.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_dict.py
    :caption: :download:`Solution <assignments/file_read_dict.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_read_listdict.py
    :caption: :download:`Solution <assignments/file_read_listdict.py>`
    :end-before: # Solution
