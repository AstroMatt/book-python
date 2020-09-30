.. _Files Write:

**********
File Write
**********


Rationale
=========
.. highlights::
    * Creates file if not exists
    * Truncate the file before writing
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * ``mode`` parameter to ``open()`` function is required


Write to File
=============
.. highlights::
    * Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = 'We choose to go to the Moon...'

    file = open(FILE, mode='w')
    file.write(DATA)
    file.close()


Write One Line
==============
.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = 'We choose to go to the Moon...'

    with open(FILE, mode='w') as file:
        file.write(DATA)


Write Multiple Lines
====================
.. highlights::
    * Write a list of lines to the file.
    * ``.writelines()`` does not add a line separator (``\n``)!!
    *  Each line must add a separator at the end.

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = [
        'We choose to go to the Moon.',
        'We choose to go to the Moon in this decade and do the other things.',
        'Not because they are easy, but because they are hard.']

    result = '\n'.join(DATA)

    with open(FILE, mode='w') as file:
        file.write(result)

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = [
        'We choose to go to the Moon.',
        'We choose to go to the Moon in this decade and do the other things.',
        'Not because they are easy, but because they are hard.']

    result = [line+'\n' for line in DATA]

    with open(FILE, mode='w') as file:
        file.writelines(result)


Write Non-Str Data
==================
.. highlights::
    * Join works only for strings
    * Conversion to ``str`` must be performed before adding a separator and writing to file.

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = [1, 2, 3]

    result = ','.join(str(x) for x in DATA) + '\n'

    with open(FILE, mode='w') as file:
        file.write(result)

    # 1,2,3

.. note:: When writing output to the stream, if newline is ``None``, any ``'\n'`` characters written are translated to the system default line separator, ``os.linesep``. If newline is ``''`` or ``'\n'``, no translation takes place. If newline is any of the other legal values, any ``'\n'`` characters written are translated to the given string. Source: https://docs.python.org/3/library/io.html#io.TextIOWrapper


Reading From One File and Writing to Another
============================================
.. code-block:: python

    FILE_READ = r'/tmp/my-infile.txt'
    FILE_WRITE = r'/tmp/my-outfile.txt'

    with open(FILE_READ) as infile, \
         open(FILE_WRITE, mode='w') as outfile:

        for line in infile:
            outfile.write(line)


Assignments
===========

File Write Str
--------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_write_str.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Check in your operating system if data was written correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_hello.txt'
        DATA = 'hello'

File Write Multiline
--------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_write_multiline.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Check in your operating system if data was written correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_multiline.txt'
        DATA = """
        127.0.0.1       localhost
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost
        """

File Write List
---------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_write_list.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Check in your operating system if data was written correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_newline.txt'
        DATA = ['hello', 'world']

File Write Non-Str
------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_write_nonstr.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Check in your operating system if data was written correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_nonstr.txt'
        DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

File Write Iris
---------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_write_iris.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Check in your operating system if data was written correctly
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_iris.txt'
        DATA = [
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor')]

File Write CSV
--------------
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/file_write_csv.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Write data to file: ``FILE``
    #. First line in file must be a header (first line of ``DATA``)
    #. For each row, convert it's values to ``str``
    #. Use coma (``,``) as a value separator
    #. Add line terminator (``\n``) to each row
    #. Save row values to file

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Zapisz dane do pliku: ``FILE``
    #. Pierwsza linia w pliku musi być nagłówkiem (pierwsza linia ``DATA``)
    #. Dla każdego wiersza przekonwertuj jego wartości do ``str``
    #. Użyj przecinka (``,``) jako separatora wartości
    #. Użyj ``\n`` jako koniec linii w każdym wierszu
    #. Zapisz do pliku wartości z wiersza

:Input:
    .. code-block:: python

        FILE = r'file_write_csv.csv'
        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Hints:
    * ``[str(x) for x in ...]``
