**********
Entry Test
**********


Entry Test List of Dict
=======================
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 8 min

:English:
    #. Use data from "Input" section (see below)
    #. Separate header and data
    #. Print ``List[dict]``:

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Wypisz ``List[dict]``:

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

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

:Output:
    .. code-block:: python

        result: List[dict]
        # [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
        #  {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        #  {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        #  ...]

:The whys and wherefores:
    * Working with nested data structures
    * Iterating over dict and lists


Entry Test Endswith
===================
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Iterating over data unpack row to ``*features`` and ``label``
    #. Print species names ending with "ca" or "osa"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Iterując po danych rozpakuj wiersz do ``*features`` oraz ``label``
    #. Wypisz nazwy gatunków kończące się na "ca" lub "osa"

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'setosa'}),
        ]

:The whys and wherefores:
    * Accessing ``set`` items
    * Iterating over nested structure
    * Unpacking in ``for`` loop

:Hint:
    * ``str.endswith()``
    * ``set.pop()``
    * ``isinstance`` or ``type``


Entry Test File
===============
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min

:English:
    #. Use data from "Input" section (see below)
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
    #. ``result`` must be list of dicts (``List[dict]``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
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
    #. ``result`` ma być listą dictów (``List[dict]``)
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

        result: List[dict]
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
