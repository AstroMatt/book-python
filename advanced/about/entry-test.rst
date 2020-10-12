**********
Entry Test
**********


Entry Test List of Dict
=======================
* Assignment name: Entry Test List of Dict
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 8 min
* Solution: entry_test_listdict.py

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list[dict]``:

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: list[dict]``:

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
        ]

:Output:
    .. code-block:: text

        >>> assert type(result) is list
        >>> assert all(type(row) is dict for row in result)
        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
         {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
         {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
         {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
         {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
         {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'}]


Entry Test Endswith
===================
* Assignment name: Entry Test Endswith
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 8 min
* Solution: entry_test_endswith.py

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list[str]`` with species names ending with "ca" or "osa"
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: list[str]`` z nazwami gatunków kończącymi się na "ca" lub "osa"
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

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

:Output:
    .. code-block:: text

        >>> assert type(result) is list
        >>> assert all(type(row) is str for row in result)
        >>> result
        ['virginica', 'setosa', 'virginica', 'setosa', 'virginica', 'setosa']


Entry Test File
===============
* Assignment name: Entry Test File
* Last update: 2020-10-01
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: entry_test_file.py

:English:
    #. Use data from "Input" section (see below)
    #. Skip comments (``#``) and empty lines
    #. Extract from each line: ip, host and protocol and add to ``result: list[dict]``
    #. Each line must be a separate dict
    #. Merge host names with the same IP
    #. IPv4 protocol address is when dot (``.``) is in ip address
    #. ``result`` must be list of dicts (``list[dict]``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Pomiń komentarze (``#``) i puste linie
    #. Wyciągnij z każdej linii: ip, host i protokół i dodaj do ``result: list[dict]``
    #. Każda linia ma być osobnym dictem
    #. Protokół IPv4 jest gdy kropka (``.``) znajduje się w adresie
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
    .. code-block:: text

        >>> assert type(result) is list
        >>> assert all(type(row) is dict for row in result)
        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt'], 'protocol': 'ipv4'},
         {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'ipv4'},
         {'ip': '255.255.255.255', 'hosts': ['broadcasthost'], 'protocol': 'ipv4'},
         {'ip': '::1', 'hosts': ['localhost'], 'protocol': 'ipv6'}]
