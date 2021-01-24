.. _CSV Serialization:

*****************
Serialization CSV
*****************


Dialects
========
.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* CSV quoting options:

    * ``csv.QUOTE_ALL``
    * ``csv.QUOTE_MINIMAL``
    * ``csv.QUOTE_NONE``
    * ``csv.QUOTE_NONNUMERIC``

* Good practice is to always specify:

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)

* Microsoft Excel 2016 uses:

    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``
    * ``encoding='...'`` - depends on Windows version and settings

* Encoding:

    * ``utf-8`` - international standard (should be always used!)
    * ``iso-8859-1`` - ISO standard for Western Europe and USA
    * ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
    * ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
    * ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
    * ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
    * ``ASCII`` - ASCII characters only


Read data from CSV file
=======================
.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``

    import csv

    FILE = r'/tmp/iris.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


    with open(FILE) as file:
        data = csv.DictReader(file, delimiter=',')

        for line in data:
            print(line)

    # {'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
    # {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
    # {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}

.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``

    import csv

    FILE = r'/tmp/iris.csv'
    # 'sepal_length';'sepal_width';'petal_length';'petal_width';'species'
    # '5,4';'3,9';'1,3';'0,4';'setosa'
    # '5,9';'3,0';'5,1';'1,8';'virginica'
    # '6,0';'3,4';'4,5';'1,6';'versicolor'


    def isnumeric(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def clean(line):
        return {key: float(v) if isnumeric(v) else v
                for key, value in line.items()
                if (v := value.replace(',', '.'))}


    with open(FILE) as file:
        data = csv.DictReader(file, delimiter=';', quotechar="'")

        for line in data:
            print(clean(line))


    # {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'}
    # {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'}
    # {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'}


.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``. While giving custom names note, that first line (typically a header) will be treated like normal data. Therefore we skip it using ``header = file.readline()``

    import csv

    FILE = r'/tmp/iris.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor

    FIELDNAMES = [
        'Sepal Length',
        'Sepal Width',
        'Petal Length',
        'Petal Width',
        'Species',
    ]


    with open(FILE) as file:
        data = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=',')
        header = file.readline()

        for line in data:
            print(line)

    # {'Sepal Length': '5.4', 'Sepal Width': '3.9', 'Petal Length': '1.3', 'Petal Width': '0.4', 'Species': 'setosa'}
    # {'Sepal Length': '5.9', 'Sepal Width': '3.0', 'Petal Length': '5.1', 'Petal Width': '1.8', 'Species': 'virginica'}
    # {'Sepal Length': '6.0', 'Sepal Width': '3.4', 'Petal Length': '4.5', 'Petal Width': '1.6', 'Species': 'versicolor'}


Write data to CSV file
======================
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``

.. code-block:: python
    :caption: Write data to CSV file using ``csv.DictWriter()``

    import csv

    FILE = r'/tmp/iris.csv'

    DATA = [
        {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
        {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
        {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
    ]

    FIELDNAMES = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width',
        'species'
    ]

    with open(FILE, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(
            f=file,
            fieldnames=FIELDNAMES,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        writer.writeheader()
        writer.writerows(DATA)

    # "sepal_length","sepal_width","petal_length","petal_width","species"
    # "5.4","3.9","1.3","0.4","setosa"
    # "5.9","3.0","5.1","1.8","virginica"
    # "6.0","3.4","4.5","1.6","versicolor"


Parsing non-CSV files
=====================

Parsing ``/etc/passwd``
-----------------------
.. code-block:: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

    import csv


    FILE = r'/tmp/etc-passwd.txt'
    # root:x:0:0:root:/root:/bin/bash
    # watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    # jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
    # twardowski:x:1002:1002:Jan Twardowski:/home/twardowski:/bin/bash

    with open(FILE) as file:
        data = csv.DictReader(
            file,
            fieldnames=['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell'],
            delimiter=':',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in data:
            print(line)

    # {'username': 'root', 'password': 'x', 'uid': '0',...}
    # {'username': 'watney', 'password': 'x', 'uid': '1000',...}
    # {'username': 'jimenez', 'password': 'x', 'uid': '1001',...}
    # {'username': 'twardowski', 'password': 'x', 'uid': '1002',...}

Parsing Java properties file
----------------------------
.. code-block:: python
    :caption: Parsing Java properties file with ``csv.DictReader()``

    import csv


    FILE = r'/tmp/sonar-project.properties'
    # sonar.projectKey=habitatOS
    # sonar.projectName=habitatOS
    # sonar.language=py
    # sonar.sourceEncoding=UTF-8
    # sonar.verbose=true

    with open(FILE) as file:

        data = csv.DictReader(
            file,
            fieldnames=['property', 'value'],
            delimiter='=',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in data:
            print(line)

    # {'property': 'sonar.projectKey', 'value': 'habitatOS'}
    # {'property': 'sonar.projectName', 'value': 'habitatOS'}
    # {'property': 'sonar.language', 'value': 'py'}
    # {'property': 'sonar.sourceEncoding', 'value': 'UTF-8'}
    # {'property': 'sonar.verbose', 'value': 'true'}


Assignments
===========

Serialization CSV DictReader
----------------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 7 min
* Solution: :download:`solution/serialization_csv_dictreader.py`

:English:
    #. Use data from "Input" section (see below)
    #. Download :download:`data/iris.csv` file and save as ``iris.csv`` in your script folder
    #. Using ``csv.DictReader`` read the content
    #. Use explicit ``encoding``, ``delimiter`` and ``quotechar``
    #. Replace column names to ``FIELDNAMES``
    #. Skip the first line (header)
    #. Print rows with data
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Pobierz plik :download:`data/iris.csv` i zapisz go jako ``iris.csv`` w katalogu ze skryptami
    #. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
    #. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
    #. Podmień nazwy kolumn na ``FIELDNAMES``
    #. Pomiń pierwszą linię (nagłówek)
    #. Wypisz wiersze z danymi
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        FIELDNAMES = [
            'Sepal Length',
            'Sepal Width',
            'Petal Length',
            'Petal Width',
            'Species',
        ]

:Output:
    .. code-block:: python

        {'Sepal Length': '5.4', 'Sepal Width': '3.9', 'Petal Length': '1.3', 'Petal Width': '0.4', 'Species': 'setosa'}
        {'Sepal Length': '5.9', 'Sepal Width': '3.0', 'Petal Length': '5.1', 'Petal Width': '1.8', 'Species': 'virginica'}
        {'Sepal Length': '6.0', 'Sepal Width': '3.4', 'Petal Length': '4.5', 'Petal Width': '1.6', 'Species': 'versicolor'}
        ...

Serialization CSV DictWriter
----------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 7 min
* Solution: :download:`solution/serialization_csv_dictwriter.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``csv.DictWriter()`` save ``DATA`` to file
    #. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    #. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)
    #. Compare result with "Output" section (see below)
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz ``DATA`` do pliku
    #. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    #. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

:Input:
    .. code-block:: python

        DATA = [
            {'firstname': 'Jan',  'lastname': 'Twardowski'},
            {'firstname': 'José', 'lastname': 'Jiménez'},
            {'firstname': 'Mark', 'lastname': 'Watney'},
            {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
            {'firstname': 'Melissa', 'lastname': 'Lewis'},
        ]

:Output:
    .. code-block:: text

        "firstname","lastname"
        "Jan","Twardowski"
        "José","Jiménez"
        "Mark","Watney"
        "Ivan","Ivanovic"
        "Melissa","Lewis"

Serialization CSV List of Tuples
--------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 7 min
* Solution: :download:`solution/serialization_csv_list_of_tuple.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``csv.DictWriter()`` save ``DATA`` to file
    #. Compare result with "Output" section (see below)
    #. Non functional requirements:

        * Do not use quotes in output CSV file
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz ``DATA`` do pliku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Nie używaj cudzysłowów w wynikowym pliku CSV
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

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
    .. code-block:: text

        Sepal length,Sepal width,Petal length,Petal width,Species
        5.8,2.7,5.1,1.9,virginica
        5.1,3.5,1.4,0.2,setosa
        5.7,2.8,4.1,1.3,versicolor
        6.3,2.9,5.6,1.8,virginica
        6.4,3.2,4.5,1.5,versicolor
        4.7,3.2,1.3,0.2,setosa
        7.0,3.2,4.7,1.4,versicolor
        7.6,3.0,6.6,2.1,virginica
        4.9,3.0,1.4,0.2,setosa
        4.9,2.5,4.5,1.7,virginica
        7.1,3.0,5.9,2.1,virginica
        4.6,3.4,1.4,0.3,setosa
        5.4,3.9,1.7,0.4,setosa
        5.7,2.8,4.5,1.3,versicolor
        5.0,3.6,1.4,0.3,setosa
        5.5,2.3,4.0,1.3,versicolor
        6.5,3.0,5.8,2.2,virginica
        6.5,2.8,4.6,1.5,versicolor
        6.3,3.3,6.0,2.5,virginica
        6.9,3.1,4.9,1.5,versicolor
        4.6,3.1,1.5,0.2,setosa

Serialization CSV Schemaless
-----------------------------
* Complexity level: medium
* Lines of code to write: 8 lines
* Estimated time of completion: 7 min
* Solution: :download:`solution/serialization_csv_schemaless.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``csv.DictWriter()`` write variable schema data to CSV file
    #. ``fieldnames`` must be automatically generated from ``DATA``
    #. ``fieldnames`` must always be in the same order
    #. Compare result with "Output" section (see below)
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``;`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
    #. ``fieldnames`` musi być generowane automatycznie na podstawie ``DATA``
    #. ``fieldnames`` ma być zawsze w takiej samej kolejności
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

:The whys and wherefores:
    * Ability to use ``csv`` module to write data
    * Ability to iterate over nested data structures
    * Dynamically generate data structures from other

:Input:
    .. code-block:: python

        DATA = [
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

:Output:
    .. csv-table:: Output
        :header: "Petal length", "Petal width", "Sepal length", "Sepal width", "Species"

        "", "", "5.1", "3.5", "setosa"
        "4.1", "1.3", "", "", "versicolor"
        "", "1.8", "6.3", "", "virginica"
        "", "0.2", "5.0", "", "setosa"
        "4.1", "", "", "2.8", "versicolor"
        "", "1.8", "", "2.9", "virginica"

Serialization CSV Objects
-------------------------
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/serialization_csv_objects.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``csv.DictWriter()`` save data to CSV file
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz dane do pliku CSV
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

:Input:
    .. code-block:: python

        class Iris:
            def __init__(self, sepal_length, sepal_width,
                         petal_length, petal_width, species):

                self.sepal_length = sepal_length
                self.sepal_width = sepal_width
                self.petal_length = petal_length
                self.petal_width = petal_width
                self.species = species


        DATA = [
            Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
            Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
            Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
            Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
            Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
            Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
        ]

Serialization CSV Relations
---------------------------
* Complexity level: hard
* Lines of code to write: 60 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/serialization_csv_relations.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``csv.DictWriter()`` save contacts from addressbook to CSV file
    #. How to write relations to CSV file (contact has many addresses)?
    #. Recreate object structure from CSV file
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``;`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline
:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
    #. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    #. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``;`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

:Input:
    .. code-block:: python

       class Contact:
            def __init__(self, firstname, lastname, addresses=()):
                self.firstname = firstname
                self.lastname = lastname
                self.addresses = addresses


        class Address:
            def __init__(self, location, city):
                self.location = location
                self.city = city


        DATA = [
            Contact(firstname='Jan', lastname='Twardowski', addresses=(
                Address(location='Johnson Space Center', city='Houston, TX'),
                Address(location='Kennedy Space Center', city='Merritt Island, FL'),
                Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
            )),
            Contact(firstname='Mark', lastname='Watney'),
            Contact(firstname='Melissa', lastname='Lewis', addresses=()),
        ]
