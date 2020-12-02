.. _CSV Serialization:

*****************
Serialization CSV
*****************


Rationale
=========
* CSV - Comma Separated Values
* CSV - Character Separated Values

.. code-block:: text
    :caption: CSV file with numeric values.

    5.4,3.9,1.3,0.4,0
    5.9,3.0,5.1,1.8,1
    6.0,3.4,4.5,1.6,2

.. code-block:: text
    :caption: CSV file with text values. First line is a header.

    "First Name", "Last Name"
    "Mark", "Watney"
    "Jan", "Twardowski"
    "Melissa", "Lewis"
    "Alex", "Vogel"

.. code-block:: text
    :caption: CSV file with mixed values (numeric and strings). First line is a header.

    sepal_length,sepal_width,petal_length,petal_width,species
    5.4,3.9,1.3,0.4,setosa
    5.9,3.0,5.1,1.8,virginica
    6.0,3.4,4.5,1.6,versicolor
    7.3,2.9,6.3,1.8,virginica
    5.6,2.5,3.9,1.1,versicolor
    5.4,3.9,1.3,0.4,setosa


Encoding
========
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
* ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. code-block:: python

    with open(FILE, encoding='utf-8') as file:
        ...


Quoting
=======
* ``csv.QUOTE_ALL`` (safest)
* ``csv.QUOTE_MINIMAL``
* ``csv.QUOTE_NONE``
* ``csv.QUOTE_NONNUMERIC``

.. code-block:: text
    :caption: ``quoting=csv.QUOTE_ALL``

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    "5.8","2.7","5.1","1.9","virginica"
    "5.1","3.5","1.4","0.2","setosa"
    "5.7","2.8","4.1","1.3","versicolor"

.. code-block:: text
    :caption: ``quoting=csv.QUOTE_MINIMAL``

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

.. code-block:: text
    :caption: ``quoting=csv.QUOTE_NONE``

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

.. code-block:: text
    :caption: ``quoting=csv.QUOTE_NONNUMERIC``

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    5.8,2.7,5.1,1.9,"virginica"
    5.1,3.5,1.4,0.2,"setosa"
    5.7,2.8,4.1,1.3,"versicolor"


Quotechar
=========
* ``"`` - quote char (best)
* ``'`` - apostrophe

.. code-block:: text
    :caption: ``quotechar='"'``

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    "5.8","2.7","5.1","1.9","virginica"
    "5.1","3.5","1.4","0.2","setosa"
    "5.7","2.8","4.1","1.3","versicolor"

.. code-block:: text
    :caption: ``quotechar="'"``

    'Sepal length','Sepal width','Petal length','Petal width','Species'
    '5.8','2.7','5.1','1.9','virginica'
    '5.1','3.5','1.4','0.2','setosa'
    '5.7','2.8','4.1','1.3','versicolor'

.. code-block:: text
    :caption: ``quotechar='|'``

    |Sepal length|,|Sepal width|,|Petal length|,|Petal width|,|Species|
    |5.8|,|2.7|,|5.1|,|1.9|,|virginica|
    |5.1|,|3.5|,|1.4|,|0.2|,|setosa|
    |5.7|,|2.8|,|4.1|,|1.3|,|versicolor|


.. code-block:: text
    :caption: ``quotechar='/'``

    /Sepal length/,/Sepal width/,/Petal length/,/Petal width/,/Species/
    /5.8/,/2.7/,/5.1/,/1.9/,/virginica/
    /5.1/,/3.5/,/1.4/,/0.2/,/setosa/
    /5.7/,/2.8/,/4.1/,/1.3/,/versicolor/

Delimiter
=========
.. code-block:: text
    :caption: ``delimiter=','``

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

.. code-block:: text
    :caption: ``delimiter=';'``

    Sepal length;Sepal width;Petal length;Petal width;Species
    5.8;2.7;5.1;1.9;virginica
    5.1;3.5;1.4;0.2;setosa
    5.7;2.8;4.1;1.3;versicolor

.. code-block:: text
    :caption: ``delimiter='|'``

    Sepal length|Sepal width|Petal length|Petal width|Species
    5.8|2.7|5.1|1.9|virginica
    5.1|3.5|1.4|0.2|setosa
    5.7|2.8|4.1|1.3|versicolor

.. code-block:: text
    :caption: ``delimiter='\t'``

    Sepal length	Sepal width	Petal length	Petal width	Species
    5.8	2.7	5.1	1.9	virginica
    5.1	3.5	1.4	0.2	setosa
    5.7	2.8	4.1	1.3	versicolor


Lineterminator
==============
* ``\r\n`` - New line on Windows
* ``\n`` - New line on ``*nix``
* ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)


Dialects
========
.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* Microsoft Excel 2016 uses:

    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``
    * ``encoding='...'`` - depends on Windows version and settings typically ``windows-*``


Reader Object
=============
.. code-block:: python
    :caption: Read data from CSV file using ``csv.reader()``

    import csv

    FILE = r'/tmp/_temporary.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


    with open(FILE) as file:
        result = csv.reader(file)

        for line in result:
            print(line)

    # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    # ['5.4', '3.9', '1.3', '0.4', 'setosa']
    # ['5.9', '3.0', '5.1', '1.8', 'virginica']
    # ['6.0', '3.4', '4.5', '1.6', 'versicolor']


Writer Object
=============
.. code-block:: python
    :caption: Writing data to CSV file using ``csv.writer()``

    import csv

    FILE = r'/tmp/_temporary.csv'

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    with open(FILE, mode='w') as file:
        result = csv.writer(file)
        result.writerows(DATA)

    # Sepal length,Sepal width,Petal length,Petal width,Species
    # 5.8,2.7,5.1,1.9,virginica
    # 5.1,3.5,1.4,0.2,setosa
    # 5.7,2.8,4.1,1.3,versicolor


DictReader
==========
.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``

    import csv

    FILE = r'/tmp/_temporary.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


    with open(FILE) as file:
        result = csv.DictReader(file)

        for line in result:
            print(line)

    # {'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
    # {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
    # {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}

.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``

    import csv

    FILE = r'/tmp/_temporary.csv'
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
        result = csv.DictReader(file, delimiter=';', quotechar="'")

        for line in result:
            print(clean(line))


    # {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'}
    # {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'}
    # {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'}


.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``. While giving custom names note, that first line (typically a header) will be treated like normal data. Therefore we skip it using ``header = file.readline()``

    import csv

    FILE = r'/tmp/_temporary.csv'
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
        result = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=',')
        file.readline()  # skip first line

        for line in result:
            print(line)

    # {'Sepal Length': '5.4', 'Sepal Width': '3.9', 'Petal Length': '1.3', 'Petal Width': '0.4', 'Species': 'setosa'}
    # {'Sepal Length': '5.9', 'Sepal Width': '3.0', 'Petal Length': '5.1', 'Petal Width': '1.8', 'Species': 'virginica'}
    # {'Sepal Length': '6.0', 'Sepal Width': '3.4', 'Petal Length': '4.5', 'Petal Width': '1.6', 'Species': 'versicolor'}


DictWriter
==========
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``

.. code-block:: python

    import csv

    FILE = r'/tmp/_temporary.csv'

    DATA = [
        {'Sepal Length': 5.4, 'Sepal Width': 3.9, 'Petal Length': 1.3, 'Petal Width': 0.4, 'Species': 'setosa'},
        {'Sepal Length': 5.9, 'Sepal Width': 3.0, 'Petal Length': 5.1, 'Petal Width': 1.8, 'Species': 'virginica'},
        {'Sepal Length': 6.0, 'Sepal Width': 3.4, 'Petal Length': 4.5, 'Petal Width': 1.6, 'Species': 'versicolor'},
    ]

    header = DATA[0].keys()

    with open(FILE, mode='w') as file:
        result = csv.DictWriter(file, fieldnames=header)
        result.writeheader()
        result.writerows(DATA)


    # Sepal Length,Sepal Width,Petal Length,Petal Width,Species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


.. code-block:: python
    :caption: Write data to CSV file using ``csv.DictWriter()``

    import csv

    FILE = r'/tmp/_temporary.csv'

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
        result = csv.DictWriter(
            f=file,
            fieldnames=FIELDNAMES,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        result.writeheader()
        result.writerows(DATA)

    # "sepal_length","sepal_width","petal_length","petal_width","species"
    # "5.4","3.9","1.3","0.4","setosa"
    # "5.9","3.0","5.1","1.8","virginica"
    # "6.0","3.4","4.5","1.6","versicolor"


Parsing Non-CSV Files
=====================
.. code-block:: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

    import csv


    FILE = r'/tmp/_temporary.txt'
    # root:x:0:0:root:/root:/bin/bash
    # watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    # lewis:x:1001:1001:José Jiménez:/home/lewis:/bin/bash
    # twardowski:x:1002:1002:Jan Twardowski:/home/twardowski:/bin/bash

    with open(FILE) as file:
        result = csv.DictReader(
            file,
            fieldnames=['username', 'password', 'uid', 'gid', 'fullname', 'home', 'shell'],
            delimiter=':',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in result:
            print(line)

    # {'username': 'root', 'password': 'x', 'uid': '0',...}
    # {'username': 'watney', 'password': 'x', 'uid': '1000',...}
    # {'username': 'lewis', 'password': 'x', 'uid': '1001',...}
    # {'username': 'twardowski', 'password': 'x', 'uid': '1002',...}

.. code-block:: python
    :caption: Parsing Java properties file with ``csv.DictReader()``

    import csv


    FILE = r'/tmp/_temporary.properties'
    # sonar.projectKey=habitatOS
    # sonar.projectName=habitatOS
    # sonar.language=py
    # sonar.sourceEncoding=UTF-8
    # sonar.verbose=true

    with open(FILE) as file:
        result = csv.DictReader(
            file,
            fieldnames=['property', 'value'],
            delimiter='=',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in result:
            print(line)

    # {'property': 'sonar.projectKey', 'value': 'habitatOS'}
    # {'property': 'sonar.projectName', 'value': 'habitatOS'}
    # {'property': 'sonar.language', 'value': 'py'}
    # {'property': 'sonar.sourceEncoding', 'value': 'UTF-8'}
    # {'property': 'sonar.verbose', 'value': 'true'}


Serialization
=============
.. figure:: img/csv-relations-serialize-dbdump.png
    :scale: 30%
    :align: center

    Relational files or database dump

.. figure:: img/csv-relations-serialize-ffill1.png
    :scale: 30%
    :align: center

    Ffill - Forward fill

.. figure:: img/csv-relations-serialize-ffill2.png
    :scale: 30%
    :align: center

    Fill in specified columns

.. figure:: img/csv-relations-serialize-uniqid.png
    :scale: 30%
    :align: center

    Data duplication with unique ID

.. figure:: img/csv-relations-serialize-colattr.png
    :scale: 30%
    :align: center

    Each relations attribute adds one column

.. figure:: img/csv-relations-serialize-colobj.png
    :scale: 30%
    :align: center

    Each relations instance adds one column

.. figure:: img/csv-relations-serialize-colcls.png
    :scale: 30%
    :align: center

    Each relations class adds one column

.. figure:: img/csv-relations-serialize-split.png
    :scale: 30%
    :align: center

    Relations attributes split into columns

.. figure:: img/csv-relations-serialize-hybrid.png
    :scale: 30%
    :align: center

    Hybrid compact and separate columns


Good Practices
==============
* Always specify:

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)


Assignments
===========

Serialization CSV DictReader
----------------------------
* Assignment: Serialization CSV DictReader
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 6 lines
* Estimated time: 7 min
* Filename: :download:`solution/serialization_csv_dictreader.py`

English:
    #. Use data from "Given" section (see below)
    #. Download :download:`data/iris.csv` file and save as ``iris.csv`` in your script folder
    #. Using ``csv.DictReader`` read the content
    #. Use explicit ``encoding``, ``delimiter`` and ``quotechar``
    #. Replace column names to ``FIELDNAMES``
    #. Skip the first line (header)
    #. Print rows with data
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Pobierz plik :download:`data/iris.csv` i zapisz go jako ``iris.csv`` w katalogu ze skryptami
    #. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
    #. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
    #. Podmień nazwy kolumn na ``FIELDNAMES``
    #. Pomiń pierwszą linię (nagłówek)
    #. Wypisz wiersze z danymi
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        FIELDNAMES = [
            'Sepal Length',
            'Sepal Width',
            'Petal Length',
            'Petal Width',
            'Species',
        ]

Tests:
    .. code-block:: python

        {'Sepal Length': '5.4', 'Sepal Width': '3.9', 'Petal Length': '1.3', 'Petal Width': '0.4', 'Species': 'setosa'}
        {'Sepal Length': '5.9', 'Sepal Width': '3.0', 'Petal Length': '5.1', 'Petal Width': '1.8', 'Species': 'virginica'}
        {'Sepal Length': '6.0', 'Sepal Width': '3.4', 'Petal Length': '4.5', 'Petal Width': '1.6', 'Species': 'versicolor'}
        ...

Serialization CSV DictWriter
----------------------------
* Assignment: Serialization CSV DictWriter
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 7 min
* Filename: :download:`solution/serialization_csv_dictwriter.py`

English:
    #. Use data from "Given" section (see below)
    #. Using ``csv.DictWriter()`` save ``DATA`` to file
    #. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    #. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)
    #. Compare result with "Tests" section (see below)
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz ``DATA`` do pliku
    #. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    #. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

Given:
    .. code-block:: python

        DATA = [
            {'firstname': 'Jan',  'lastname': 'Twardowski'},
            {'firstname': 'José', 'lastname': 'Jiménez'},
            {'firstname': 'Mark', 'lastname': 'Watney'},
            {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
            {'firstname': 'Melissa', 'lastname': 'Lewis'},
        ]

Tests:
    .. code-block:: text

        "firstname","lastname"
        "Jan","Twardowski"
        "José","Jiménez"
        "Mark","Watney"
        "Ivan","Ivanovic"
        "Melissa","Lewis"

Serialization CSV List of Tuples
--------------------------------
* Assignment: Serialization CSV List of Tuples
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 7 lines
* Estimated time: 7 min
* Filename: :download:`solution/serialization_csv_list_of_tuple.py`

English:
    #. Use data from "Given" section (see below)
    #. Convert ``DATA`` to ``list[dict]``
    #. Using ``csv.DictWriter()`` save ``DATA`` to file
    #. Compare result with "Tests" section (see below)
    #. Non functional requirements:

        * Do not use quotes in output CSV file
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Przekonwertuj ``DATA`` do ``list[dict]``
    #. Za pomocą ``csv.DictWriter()`` zapisz ``DATA`` do pliku
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Nie używaj cudzysłowów w wynikowym pliku CSV
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

Given:
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

Tests:
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
* Assignment: Serialization CSV Schemaless
* Last update: 2020-10-01
* Complexity: medium
* Lines of code: 8 lines
* Estimated time: 7 min
* Filename: :download:`solution/serialization_csv_schemaless.py`

English:
    #. Use data from "Given" section (see below)
    #. Using ``csv.DictWriter()`` write variable schema data to CSV file
    #. ``fieldnames`` must be automatically generated from ``DATA``
    #. ``fieldnames`` must always be in the same order
    #. Compare result with "Tests" section (see below)
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``;`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
    #. ``fieldnames`` musi być generowane automatycznie na podstawie ``DATA``
    #. ``fieldnames`` ma być zawsze w takiej samej kolejności
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

Given:
    .. code-block:: python

        DATA = [
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

Tests:
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
* Assignment: Serialization CSV Objects
* Last update: 2020-10-01
* Complexity: medium
* Lines of code: 7 lines
* Estimated time: 13 min
* Filename: :download:`solution/serialization_csv_objects.py`

English:
    #. Use data from "Given" section (see below)
    #. Using ``csv.DictWriter()`` save data to CSV file
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``,`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz dane do pliku CSV
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``,`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

Given:
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
* Assignment: Serialization CSV Relations
* Last update: 2020-10-01
* Complexity: hard
* Lines of code: 18 lines
* Estimated time: 21 min
* Filename: :download:`solution/serialization_csv_relations.py`

English:
    #. Use data from "Given" section (see below)
    #. Using ``csv.DictWriter()`` save contacts from addressbook to CSV file
    #. How to write relations to CSV file (contact has many addresses)?
    #. Recreate object structure from CSV file
    #. Non functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``;`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline
Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
    #. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    #. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``;`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

Given:
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
