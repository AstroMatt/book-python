***********
Mini Botnet
***********


Assignments
===========

Mini Botnet
-----------
* Complexity level: medium
* Lines of code to write: 45 lines
* Estimated time of completion: 21 min
* Solution: TODO
* Last update: 2020-10-01

#. Stwórz mini botnet o architekturze podanej :numref:`figure-botnet`. Mini botnet składa się z trzech części:

    * Heartbeat Receiver - server przyjmujący informacje o ofiarach (czy wciąż żyją i jakie mają backdoory),
    * Victim - ofiara,
    * Attacket - atakujący.

.. figure:: img/botnet.png
    :name: figure-botnet
    :width: 75%
    :align: center

    Architektura botnet

:Hints:
    * Do weryfikacji czy port jest otwarty możesz użyć ``telnet`` albo ``netcat``

Heartbeat Receiver
------------------
* Complexity level: medium
* Lines of code to write: 45 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/botnet_heartbeat_receiver.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Server ma przyjmować komunikaty UDP na porcie 1337
    #. Datę UTC przyjścia pakietu, IP i port backdoora zapisuje do bazy danych ``sqlite3`` jako pola:

        * ``datetime DATETIME``,
        * ``host TEXT``,
        * ``port INTEGER``.

:Hints:
    * ``socketserver.UDPServer``

Victim
------
* Complexity level: medium
* Lines of code to write: 150 lines
* Estimated time of completion: 34 min
* Solution: :download:`solution/botnet_victim.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Po zainfekowaniu otwiera randomowy port TCP (backdoor) z przedziału 1025-65535 na którym nasłuchuje komunikatów
    #. Dlaczego taki zakres portów?
    #. Co 5 sekund wysyła informację ze swoim numerem portu backdoor oraz swoim adresem IP do Heartbeat Receivera
    #. Po otrzymaniu komunikatu XML na port backdoora wykonuje operację w nim zawarte
    #. Ofiara ma przesyłać JSON atakującemu w formacie:

        * ``date: datetime`` (UTC),
        * ``host: str``,
        * ``port: int``,
        * ``stdout: str``,
        * ``stderror: str``.

    #. Stwórz dekorator ``is_valid_xml``, który sprawdzi czy XML się waliduje (czy ma poprawną strukturę) i tylko wtedy wykona polecenia
    #. Stwórz dekorator ``log_incoming_requests``, który zapisze do pliku ``botnet.log`` logi w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS`` dla każdego polecenia wykonywanego na systemie ofiary

:Hints:
    * ``random``
    * ``logging``
    * ``socket``
    * ``socketserver.TCPServer``
    * ``subprocess.run()``
    * ``json.dumps()``, ``json.loads()``
    * ``xml.etree.ElementTree``

Attacker
--------
* Complexity level: medium
* Lines of code to write: 150 lines
* Estimated time of completion: 34 min
* Solution: :download:`solution/botnet_attacker.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Skopiuj zawartość :numref:`listing-botnet-commands` do pliku ``botnet-commands.xml``
    #. Skrypt można wywoływać z parametrami linii poleceń:

        * ``--xml FILENAME``, domyślnie ``botnet-commands.xml``, opcjonalny (jeżeli podano inne parametry),
        * ``--exec COMMAND`` - opcjonalny,
        * ``--cat FILENAME`` - opcjonalny,
        * ``--ls PATH`` - opcjonalny,
        * ``--eval CODE`` - opcjonalny.

    #. Skrypt ma do wszystkich botów (ofiar), które pingnęły serwer heartbeat w ciągu godziny wysyłać (IP ofiary, port backdoor) polecenia do wykonania
    #. Polecenia są:

        * w pliku XML podanym jako parametr (jeżeli podano flagę ``--xml``),
        * podane jako parametr do ``--exec``,
        * wyświetlanie zawartości pliku podanego jako parametr ``--cat``,
        * listowanie zawartości katalogu podanego jako parametr ``--ls``,
        * wykonywanie kodu Python i zwracanie wyników, jeżeli podano ``--eval``.

    #. Polecenia do wykonania bez względu na flagę muszą być przesłane za pomocą komunikatów XML
    #. Datę, komunikat XML, oraz listę hostów do których poszło zapytanie zapisuj w bazie ``sqlite3`` w charakterze logów
    #. Wyniki, które przyjdą od ofiar zapisuj w bazie danych ``sqlite3`` wraz z datą otrzymania, adresem IP ofiary, portem (backdoor), stdout i stderr
    #. Do obsługi parametrów z linii poleceń wykorzystaj ``argparse``
    #. Przetwarzanie requestów jest nieblokujące, tzn. otwieraj wątek dla każdego zapytania
    #. Wykorzystaj ``os.path.join`` (łączenie ścieżki) oraz ``os.walk`` (wyświetlanie zawartości).

:Input:
    .. literalinclude:: src/botnet-commands.xml
        :name: listing-botnet-commands
        :language: python
        :caption: Komunikat XML z listą poleceń do wykonania na komputerze ofiary

:Hints:
    * ``argparse``
    * ``socket``
    * ``json.dumps()``, ``json.loads()``

:Extra task:
    Za pomocą ``Django`` stwórz panel administracyjny dla botnetu:

    * Wyszukiwanie aktywnych hostów
    * ``command``
