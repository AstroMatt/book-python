.. _OOP Relations:

*********
Relations
*********


Relations
=========
* :ref:`OOP Argument Mutability`

.. code-block:: python

    from typing import Sequence


    class Mission:
        def __init__(self, year: int, name: str) -> None:
            self.year: int = year
            self.name: str = name

    class Astronaut:
        def __init__(self, name: str, experience: Sequence[Mission] = ()) -> None:
            self.name: str = name
            self.experience: list[Mission] = list(experience)


    result = [
        Astronaut('Jan Twardowski', experience=[
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3')]),

        Astronaut('Mark Watney', experience=[
            Mission(2035, 'Ares 3')]),

        Astronaut('Melissa Lewis'),
    ]


Serialization
=============
* ``pickle`` - has relations
* ``json`` - has relations
* ``csv`` - non-relational format

.. figure:: img/oop-relations-serialize-dbdump.png
    :scale: 30%
    :align: center

    Relational files or database dump

.. figure:: img/oop-relations-serialize-ffill1.png
    :scale: 30%
    :align: center

    Ffill - Forward fill

.. figure:: img/oop-relations-serialize-ffill2.png
    :scale: 30%
    :align: center

    Fill in specified columns

.. figure:: img/oop-relations-serialize-uniqid.png
    :scale: 30%
    :align: center

    Data duplication with unique ID

.. figure:: img/oop-relations-serialize-colattr.png
    :scale: 30%
    :align: center

    Each relations attribute adds one column

.. figure:: img/oop-relations-serialize-colobj.png
    :scale: 30%
    :align: center

    Each relations instance adds one column

.. figure:: img/oop-relations-serialize-colcls.png
    :scale: 30%
    :align: center

    Each relations class adds one column

.. figure:: img/oop-relations-serialize-split.png
    :scale: 30%
    :align: center

    Relations attributes split into columns

.. figure:: img/oop-relations-serialize-hybrid.png
    :scale: 30%
    :align: center

    Hybrid compact and separate columns


Assignments
===========

OOP Relations Model
-------------------
* Assignment name: OOP Relations Model
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_relations_model.py`

:English:
    #. Use data from "Input" section (see below)
    #. In ``DATA`` we have two classes
    #. Model data using classes and relations
    #. Create instances dynamically based on ``DATA``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. W ``DATA`` mamy dwie klasy
    #. Zamodeluj problem wykorzystując klasy i relacje między nimi
    #. Twórz instancje dynamicznie na podstawie ``DATA``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:The whys and wherefores:
    * OOP modeling
    * working with objects
    * nesting objects and relations
    * casting objects to ``str``

:Input:
    .. code-block:: json
        :caption: Python list[dict] or JSON?

        DATA = [
            {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
                {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},
            {"firstname": "José", "lastname": "Jiménez", "addresses": [
                {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
                {"street": "", "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
            {"firstname": "Mark", "lastname": "Watney", "addresses": [
                {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
                {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
            {"firstname": "Иван", "lastname": "Иванович", "addresses": [
                {"street": "", "city": "Космодро́м Байкону́р", "postcode": "", "region": "Кызылординская область", "country": "Қазақстан"},
                {"street": "", "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
            {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
            {"firstname": "Alex", "lastname": "Vogel", "addresses": [
                {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
        ]

:Output:
    .. code-block:: text

        >>> assert type(result) is list

        >>> assert all(type(astro) is Astronaut
        ...            for astro in result)

        >>> assert all(type(addr) is Address
        ...            for astro in result
        ...            for addr in astro.addresses)

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [Astronaut(firstname='Jan', lastname='Twardowski', addresses=[Address(street='Kamienica Pod św. Janem Kapistranem', city='Kraków', postcode='31-008', region='Małopolskie', country='Poland')]),
         Astronaut(firstname='José', lastname='Jiménez',
                   addresses=[Address(street='2101 E NASA Pkwy', city='Houston', postcode=77058, region='Texas', country='USA'),
                              Address(street='', city='Kennedy Space Center', postcode=32899, region='Florida', country='USA')]),
         Astronaut(firstname='Mark', lastname='Watney',
                   addresses=[Address(street='4800 Oak Grove Dr', city='Pasadena', postcode=91109, region='California', country='USA'),
                              Address(street='2825 E Ave P', city='Palmdale', postcode=93550, region='California', country='USA')]),
         Astronaut(firstname='Иван', lastname='Иванович',
                   addresses=[Address(street='', city='Космодро́м Байкону́р', postcode='', region='Кызылординская область', country='Қазақстан'),
                              Address(street='', city='Звёздный городо́к', postcode=141160, region='Московская область', country='Россия')]),
         Astronaut(firstname='Alex', lastname='Vogel',
                   addresses=[Address(street='Linder Hoehe', city='Köln', postcode=51147, region='North Rhine-Westphalia', country='Germany')])]

OOP Relations Flatten
---------------------
* Assignment name: OOP Relations Flatten
* Last update: 2020-10-01
* Complexity level: hard
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/oop_relations_flatten.py`

:English:
    #. Use code from "Input" section (see below)
    #. Using ``csv.DictWriter()`` save contacts from addressbook to CSV file
    #. How to write relations to CSV file (contact has many addresses)?
    #. Recreate object structure from CSV file
    #. Non-functional requirements:

        * All fields must be enclosed by double quote ``"`` character
        * Use ``;`` to separate columns
        * Use ``utf-8`` encoding
        * Use Unix ``\n`` newline

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
    #. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    #. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku
    #. Wymagania niefunkcjonalne:

        * Wszystkie pola muszą być otoczone znakiem cudzysłowu ``"``
        * Użyj ``;`` do oddzielenia kolumn
        * Użyj kodowania ``utf-8``
        * Użyj zakończenia linii Unix ``\n``

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        class Astronaut:
            def __init__(self, firstname, lastname, missions=()):
                self.firstname = firstname
                self.lastname = lastname
                self.missions = list(missions)


        class Mission:
            def __init__(self, year, name):
                self.year = year
                self.name = name


        DATA = [
            Astronaut('Jan', 'Twardowski', missions=[
                Mission(1969, 'Apollo 11'),
                Mission(2024, 'Artemis 3')]),

            Astronaut('Mark', 'Watney', missions=[
                Mission(2035, 'Ares 3')]),

            Astronaut('Melissa', 'Lewis'),
        ]

:Output:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'firstname': 'Jan', 'lastname': 'Twardowski', 'missions': '1969,Apollo 11;2024,Artemis 3'},
         {'firstname': 'Mark', 'lastname': 'Watney', 'missions': '2035,Ares 3'},
         {'firstname': 'Melissa', 'lastname': 'Lewis', 'missions': ''}]

OOP Relations Nested
--------------------
* Assignment name: OOP Relations Nested
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 45 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_relations_nested.py`

:English:
    #. Client can open a bank account
    #. Client can have many accounts
    #. Bank has many clients
    #. Each account has unique number generated when opening an account
    #. Client can ask about number of all of his accounts
    #. Client can add money to the account
    #. Client can withdraw money from the account
    #. Compare result with "Output" section (see below)

:Polish:
    #. Klient może otworzyć konto w banku
    #. Klient może mieć wiele kont
    #. Bank może mieć wielu klientów
    #. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
    #. Klient może odpytać o numery wszystkich swoich kont
    #. Klient może wpłacić pieniądze na swoje konto
    #. Klient może wybrać pieniądze z bankomatu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)
