.. _Files Read:

*********
File Read
*********


Rationale
=========
.. highlights::
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * Fails when file cannot be accessed
    * Uses context manager
    * ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='rt'``)


Read From File
==============
.. highlights::
    * Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE)
    data = file.read()
    file.close()


Read Using Context Manager
==========================
.. highlights::
    * Context managers use ``with ... as ...:`` syntax
    * It closes file automatically upon block exit (dedent)
    * Using context manager is best practice
    * More information in :ref:`Context Managers`

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File at Once
=================
.. highlights::
    * Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File as List of Lines
==========================
.. highlights::
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
.. highlights::
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
            total += sum(line)

    print(total)

.. code-block:: python

    moving_average = 0
    window = 10
    tmp = []

    with open(FILE) as file:
        for i, line in enumerate(file):
            line = line.strip().split(',')
            values = [x for x in line if x.isnumeric()]
            tmp.append(sum(values) / len(values))

            if i % window == 0:
                moving_average += sum(tmp) / len(tmp)
                tmp = []

    print(mean)


Assignments
===========

File Read Str
-------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_read_str.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Read ``FILE`` to ``result: str``
    #. Print ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Wczytaj ``FILE`` do ``result: str``
    #. Wypisz ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_hello.txt'
        DATA = 'hello world'

:Output:
    .. code-block:: python

        result: str
        # hello world

File Read Multiline
-------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/file_read_multiline.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Read ``FILE`` to ``result: list[str]``
    #. Print ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Wczytaj ``FILE`` do ``result: list[str]``
    #. Wypisz ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_write_hello.txt'
        DATA = 'sepal_length\nsepal_width\npetal_length\npetal_width\nspecies\n'

:Output:
    .. code-block:: python

        result: list[str]
        # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

File Read CSV
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/file_read_csv.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Read ``FILE``
    #. Separate header from data
    #. Write header (first line) to ``header``
    #. Read file and for each line:

        * Strip whitespaces
        * Split line by coma ``,``
        * Convert measurements do ``tuple[float]``
        * Append measurements to ``features``
        * Append species name to ``labels``

    #. Print ``header``, ``features`` and ``labels``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Wczytaj ``FILE``
    #. Odseparuj nagłówek od danych
    #. Zapisz nagłówek (pierwsza linia) do ``header``
    #. Zaczytaj plik i dla każdej linii:

        * Usuń białe znaki z początku i końca linii
        * Podziel linię po przecinku ``,``
        * Przekonwertuj pomiary do ``tuple[float]``
        * Dodaj pomiary do ``features``
        * Dodaj gatunek do ``labels``

    #. Wyświetl ``header``, ``features`` i ``labels``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_read_csv.csv'
        DATA = """sepal_length,sepal_width,petal_length,petal_width,species
        5.4,3.9,1.3,0.4,setosa
        5.9,3.0,5.1,1.8,virginica
        6.0,3.4,4.5,1.6,versicolor
        7.3,2.9,6.3,1.8,virginica
        5.6,2.5,3.9,1.1,versicolor
        5.4,3.9,1.3,0.4,setosa
        5.5,2.6,4.4,1.2,versicolor
        5.7,2.9,4.2,1.3,versicolor
        4.9,3.1,1.5,0.1,setosa
        6.7,2.5,5.8,1.8,virginica
        6.5,3.0,5.2,2.0,virginica
        5.1,3.3,1.7,0.5,setosa
        """

        header = []
        features = []
        labels = []

:Output:
    .. code-block:: python

        header: list[str]
        # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

        features: list[tuple[float]]
        # [(5.4, 3.9, 1.3, 0.4), (5.9, 3.0, 5.1, 1.8), (6.0, 3.4, 4.5, 1.6),
        #  (7.3, 2.9, 6.3, 1.8), (5.6, 2.5, 3.9, 1.1), (5.4, 3.9, 1.3, 0.4),
        #  (5.5, 2.6, 4.4, 1.2), (5.7, 2.9, 4.2, 1.3), (4.9, 3.1, 1.5, 0.1), ...]

        labels: list[str]
        # ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor',
        #  'setosa', 'versicolor', 'versicolor', 'setosa', 'virginica',
        #  'virginica', 'setosa', 'setosa', ...]

:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

:Hints:
    * ``tuple(float(x) for x in X)``

File Read Parsing Dict
----------------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/file_read_parsing_dict.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write ``DATA`` to file ``FILE``
    #. Read ``FILE`` and for each line:

        * Remove leading and trailing whitespaces
        * Skip line if it is empty
        * Split line by whitespace
        * Separate IP address and hosts names
        * Append IP address and hosts names to ``result``

    #. Merge hostnames for the same IP
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz ``DATA`` do pliku ``FILE``
    #. Wczytaj ``FILE`` i dla każdej lini:

        * Usuń białe znaki na początku i końcu linii
        * Pomiń linię, jeżeli jest pusta
        * Podziel linię po białych znakach
        * Odseparuj adres IP i nazwy hostów
        * Dodaj adres IP i nazwy hostów do ``result``

    #. Scal nazwy hostów dla tego samego IP
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FILE = r'file_read_parsing_dict.txt'
        DATA = """
        127.0.0.1       localhost
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost"""

:Output:
    .. code-block:: python

        result: dict
        # {'127.0.0.1': ['localhost'],
        #  '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
        #  '255.255.255.255': ['broadcasthost'],
        #  '::1': ['localhost']}

:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

:Hints:
    * ``str.isspace()``
    * ``str.split()``

File Read Parsing List of Dicts
-------------------------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/file_read_parsing_listdict.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list[dict]``
    #. Using ``file.write()`` save input data from listing below to file ``hosts-advanced.txt``
    #. Read file and for each line:

        * Skip line if it's empty, is whitespace or starts with comment ``#``
        * Remove leading and trailing whitespaces
        * Split line by whitespace
        * Separate IP address and hosts names
        * Use one line ``if`` to check whether dot ``.`` is in the IP address
        * If is present then protocol is IPv4 otherwise IPv6
        * Append IP address and hosts names to ``result``

    #. Merge hostnames for the same IP
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: list[dict]``
    #. Używając ``file.write()`` zapisz dane wejściowe z listingu poniżej do pliku ``hosts-advanced.txt``
    #. Przeczytaj plik i dla każdej lini:

        * Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza ``#``
        * Usuń białe znaki na początku i końcu linii
        * Podziel linię po białych znakach
        * Odseparuj adres IP i nazwy hostów
        * Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka ``.`` w adresie IP
        * Jeżeli jest obecna to protokół  jest IPv4, w przeciwnym przypadku IPv6
        * Dodaj adres IP i nazwy hostów do ``result``

    #. Scal nazwy hostów dla tego samego IP
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = """
        ##
        # ``/etc/hosts`` structure:
        #   - IPv4 or IPv6
        #   - Hostnames
         ##

        127.0.0.1       localhost
        127.0.0.1       astromatt
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost
        """

:Output:
    .. code-block:: python

        result: list[dict]
        # [{'ip': '127.0.0.1', 'protocol': 'ipv4', 'hostnames': {'localhost', 'astromatt'}},
        #  {'ip': '10.13.37.1', 'protocol': 'ipv4', 'hostnames': {'nasa.gov', 'esa.int', 'roscosmos.ru'}},
        #  {'ip': '255.255.255.255', 'protocol': 'ipv4', 'hostnames': {'broadcasthost'}},
        #  {'ip': '::1', 'protocol': 'ipv6', 'hostnames': {'localhost'}}]

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Hints:
    * ``str.split()``
    * ``str.isspace()``
    * ``value = True if ... else False``
