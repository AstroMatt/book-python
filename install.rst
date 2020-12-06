.. _Install:

**************
Python Install
**************


General Requirements
====================
#. Można korzystać ze swojego komputera i dowolnego systemu operacyjnego
#. Materiały szkoleniowe dostosowane są do Python 3.7 i 3.8 (nowsza wersja jest preferowana)
#. Python może być zainstalowany albo za pomocą oficjalnej dystrybucji albo z pakietu Anaconda
#. Wybór dystrybucji Python nie będzie miał wpływu na przebieg szkolenia
#. Podczas szkolenia trener będzie korzystał z PyCharm jako środowisko programistyczne (IDE)
#. Można korzystać z innego IDE, ale proszę zaznajomić się z nim przed szkoleniem
#. Niestety nie będzie czasu na rozwiązywanie problemów technicznych z IDE
#. Podczas instalacji PyCharm zaznacz opcję: "powiąż z rozszerzeniem plików ``.py``" (nie jest to konieczne ale ułatwia pracę)
#. Proszę o zainstalowanie Git i założenie darmowego konta na Github oraz potwierdzenie linka aktywacyjnego na mailu
#. Odnośniki do pobierania oprogramowania:

    * Python: https://www.python.org/downloads/
    * Git: https://git-scm.com/download/
    * PyCharm: https://www.jetbrains.com/pycharm/download/

#. Dla szkolenia z Analizy Numerycznej lub Machine Learning dodatkowo trzeba:

    * Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
    * Do instalacji pakietów konieczny jest dostęp do internetu (zapewniany przez organizatora szkolenia)
    * Instalacja: ``pip3 install --upgrade jupyter numpy pandas matplotlib scikit-learn statsmodels seaborn bokeh``


Install on macOS
================
#. macOS domyślnie ma zainstalowaną starą wersję Pythona 2 (nie będziemy z niej korzystać)
#. Pobierz i zainstaluj najnowszą wersję Pythona
#. Alternatywnie użyj Brew (https://brew.sh) i zainstaluj Python za pomocą: ``brew install python3``
#. Wykonaj w terminalu ``python --version`` - powinno wyświetlić wersję Python zgodną z wymaganiami kursu
#. Wykonaj w terminalu ``pip --version`` - wersja ``pip`` w nie ma większego znaczenia, ale ważne aby polecenie nie wyrzuciło błędu (tzn. ``pip`` by był poprawnie zainstalowany)


Install on Linux
================
#. Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona
#. Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
#. Alternatywnie zainstaluj używając managera pakietów dla dystrybucji z której korzystasz:

    * ``apt`` - Debian, Ubuntu
    * ``snap`` - Ubuntu
    * ``yum`` - SuSe
    * ``emerge`` - Gentoo
    * ``rpm`` - RedHat, Fedora

#. Wykonaj w terminalu ``python3 --version`` - powinno wyświetlić wersję Python zgodną z wymaganiami kursu
#. Wykonaj w terminalu ``pip3 --version`` - wersja ``pip`` w nie ma większego znaczenia, ale ważne aby polecenie nie wyrzuciło błędu (tzn. ``pip`` by był poprawnie zainstalowany)

.. note:: W Ubuntu może nie być ``pip`` wtedy trzeba uruchomić ``sudo apt update; sudo apt install --yes python3-pip``


Install on Windows
==================
.. figure:: _img/python-install-1c.png

    Podczas instalacji Python zaznacz opcję (1) "Add Python to ``PATH``" a następnie kontynuuj instalację z zalecanymi opcjami (2).

#. Pobierz zgodną z wymaganiami kursu wersję Pythona
#. Podczas instalacji Python zaznacz opcję "Add Python to ``PATH``"
#. Zainstaluj Python używając opcji "Install now", która ustawi domyślne opcje
#. Wykonaj w terminalu ``python --version`` - powinno wyświetlić wersję Python zgodną z wymaganiami kursu
#. Wykonaj w terminalu ``pip --version`` - wersja ``pip`` w nie ma większego znaczenia, ale ważne aby polecenie nie wyrzuciło błędu (tzn. ``pip`` by był poprawnie zainstalowany)

.. note:: Uwaga, jeżeli opcja "Add Python to ``PATH``" nie została zaznaczona podczas instalacji:

    * ``cmd`` nie wykryje polecenia ``python`` oraz ``pip``
    * Trzeba będzie to dodać Python do ``PATH`` ręcznie:

        #. Kliknij przycisk start
        #. Kliknij prawym przyciskiem myszy na "Komputer" i wybierz z menu: "Właściwości"
        #. Z menu po lewej stronie wybierz: "Zaawansowane ustawienia systemu" (wymaga uprawnień administracyjnych)
        #. Na zakładce "Zaawansowane" kliknąć przycisk "Zmienne środowiskowe..." (na dole po prawej)
        #. Z okienka "Zmienne systemowe" (dolne okienko - ważne!) wybrać zmienną ``Path`` (na dole listy) i kliknąć "Edytuj..."
        #. Na końcu pola "Wartość zmiennej" dopisać poniższe wartości
        #. Uwaga, nie kasować tego co już jest tylko dopisać na koniec
        #. Ścieżki muszą być rozdzielone średnikiem ";", tzn. dopisać na końcu pola, za pozostałymi wpisami treść ``;ścieżka1;ścieżka2``
        #. Ścieżki do dopisania:

            * ``%USERPROFILE%\AppData\Local\Programs\Python\Python38\``
            * ``%USERPROFILE%\AppData\Local\Programs\Python\Python38\Scripts\``

        #. Sprawdź ścieżki przed dodaniem, gdyż w zależności od wersji katalog instalacji może się nieznacznie różnić (np. katalog ``Python38`` w ścieżce)
        #. Po wprowadzeniu modyfikacji kliknij "OK", następnie "OK" dla okienka ze zmiennymi środowiskowymi oraz "OK" w okienku "Właściwości systemu"
        #. Trzeba zamknąć i uruchomić ``cmd`` ponownie
        #. Starsze wersje Windows wymagają wylogowania użytkownika i zalogowania się ponownie

    * Można to też zrobić z poziomu ``cmd``: ``setx PATH "%PATH%;ścieżka1;ścieżka2"``
    * Instrukcja z obrazkami: https://www.computerhope.com/issues/ch000549.htm
