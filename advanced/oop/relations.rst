*********
Relations
*********


Relations
=========
.. code-block:: python

    from typing import List


    class Astronaut:
        def __init__(self, name: str, experience: List[Missions] = ()) -> None:
            self.name = name
            self.experience = experience

    class Mission:
        def __init__(self, year: int, name: str) -> None:
            self.year = year
            self.name = name


    CREW = [
        Astronaut('Jan Twardowski', experience=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'))),

        Astronaut('Mark Watney', experience=(
            Mission(2035, 'Ares 3'))),

        Astronaut('Melissa Lewis'),
    ]


Assignments
===========

OOP Relations
-------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_relations.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create Address Book
    #. Model data using classes and relations
    #. We should have three classes, name it

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Napisz książkę adresową
    #. W zadaniu mamy do czynienia z trzema klasami, wymień je.
    #. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi

:The whys and wherefores:
    * OOP modeling
    * working with objects
    * nesting objects and relations
    * casting objects to ``str``

:Input:
    .. code-block:: json
        :caption: Address Book

        [
            {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
                {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

            {"firstname": "José", "lastname": "Jiménez", "addresses": [
                {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
                {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

            {"firstname": "Mark", "lastname": "Watney", "addresses": [
                {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
                {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

            {"firstname": "Иван", "lastname": "Иванович", "addresses": [
                {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
                {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

            {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

            {"firstname": "Alex", "lastname": "Vogel", "addresses": [
                {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
        ]

OOP Relations Flatten
---------------------
* Complexity level: hard
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min
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

OOP Relations Nested
--------------------
* Complexity level: medium
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_relations_nested.py`

:English:
    #. Client can open a bank account
    #. Client can have many accounts
    #. Bank has many clients
    #. Each account has unique number generated when opening an account
    #. Client can ask about number of all of his accounts
    #. Client can add money to the account
    #. Client can withdraw money from the account

:Polish:
    #. Klient może otworzyć konto w banku
    #. Klient może mieć wiele kont
    #. Bank może mieć wielu klientów
    #. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
    #. Klient może odpytać o numery wszystkich swoich kont
    #. Klient może wpłacić pieniądze na swoje konto
    #. Klient może wybrać pieniądze z bankomatu
