***
FTP
***


Connect to FTP Server (insecure)
================================
.. literalinclude:: src/ftp-connect-insecure.py
    :language: python
    :caption: Connect to FTP Server (insecure)


Connect to FTP Server (secure)
==============================
.. literalinclude:: src/ftp-connect-secure.py
    :language: python
    :caption: Connect to FTP Server (secure)


Download file
=============
.. literalinclude:: src/ftp-download.py
    :language: python
    :caption: Download file from FTP Server


Methods
=======
.. csv-table:: FTP Methods
    :header-rows: 1
    :widths: 10, 10, 80
    :file: data/ftp-api.csv


Assignments
===========

FTP Download
------------
* Assignment: FTP Download
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Filename: :download:`solution/ftp_download.py`

English:
    .. todo:: English Translation

Polish:
    #. Stwórz na swoim komputerze plik o nazwie ``imie-nazwisko.txt``, gdzie:

        * zamiast ``imie`` wpisz swoje imię
        * zamiast ``nazwisko`` wpisz swoje nazwisko

    #. Do pliku wklej treść tekstu :pep:`20` (wynik polecenia ``import this``)
    #. Połącz się z serwerem podanym przez prowadzącego
    #. Pobierz plik ``README.txt`` z głównego folderu
    #. Do katalogu ``files`` uploaduj plik ``imie-nazwisko.txt``
    #. Skorzystaj z Context Managera do połączenia

FTP Upload
----------
* Assignment: FTP Upload
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Filename: :download:`solution/ftp_upload.py`

English:
    .. todo:: English Translation

Polish:
    #. Pobierz na swój komputer plik :download:`http://python.astrotech.io/_static/favicon.png`
    #. Nazwij plik ``imie-nazwisko.png``, gdzie:

        * zamiast ``imie`` wpisz swoje imię
        * zamiast ``nazwisko`` wpisz swoje nazwisko

    #. Połącz się z serwerem podanym przez prowadzącego
    #. Do katalogu ``img`` uploaduj plik pobrany w poprzednim kroku
    #. Skorzystaj z Context Managera do połączenia
    #. Przesyłanie danych ma odbywać się w trybie binarnym
