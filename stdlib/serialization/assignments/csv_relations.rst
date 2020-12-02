#. powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi

    .. csv-table::
        :header: "id", "First Name", "Last Name", "Location", "City"

        "1", "Jan", "Twardowski", "Johnson Space Center", "Houston, TX"
        "2", "Jan", "Twardowski", "Kennedy Space Center", "Merritt Island, FL"
        "3", "Jan", "Twardowski", "Jet Propulsion Laboratory", "Pasadena, CA"
        "4", "Mark", "Watney", "", ""
        "5", "Melissa", "Lewis", "", ""

#. powtarzanie rekordów (bez usera - user to rekord z góry) z innymi danymi adresowymi

    .. csv-table::
        :header: "id", "First Name", "Last Name", "Location", "City"

        "1", "Jan", "Twardowski", "Johnson Space Center", "Houston, TX"
        "2", "", "", "Kennedy Space Center", "Merritt Island, FL"
        "3", "", "", "Jet Propulsion Laboratory", "Pasadena, CA"
        "4", "Mark", "Watney", "", ""
        "5", "Melissa", "Lewis", "", ""

#. dodawanie kolumn (Address1_Location", "Address1_City", "Address2_Location) i automatyczne generowanie fieldnames

    .. csv-table::
        :header: "id", "First Name", "Last Name", "Address1_Location", "Address1_City", "Address2_Location", "Address2_City", ...

        "1", "Jan", "Twardowski", "Johnson Space Center", "Houston, TX", "Kennedy Space Center", "Merritt Island, FL", ...
        "2", "Mark", "Watney", "", ""
        "3", "Melissa", "Lewis", "", ""

#. wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')

    .. csv-table::
        :header: "id", "First Name", "Last Name", "Address1", "Address2", ...

        "1", "Jan", "Twardowski", "Johnson Space Center;Houston, TX", "Kennedy Space Center;Merritt Island, FL", ...
        "2", "Mark", "Watney", "", ""
        "3", "Melissa", "Lewis", "", ""


#. jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane pionową kreską "|")

    .. csv-table::
        :header: "id", "First Name", "Last Name", "Address"

        "1", "Jan", "Twardowski", "Johnson Space Center;Houston, TX|Kennedy Space Center;Merritt Island, FL"
        "2", "Mark", "Watney", "", ""
        "3", "Melissa", "Lewis", "", ""

#. Dump danych jeden do jeden z bazy wraz z relacjami
