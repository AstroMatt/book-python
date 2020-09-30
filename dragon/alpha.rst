.. _Dragon Alpha:

**********************
Dragon (version alpha)
**********************

.. figure:: img/dragon.gif
    :width: 75%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

* Complexity level: medium
* Lines of code to write: 100 lines
* Estimated time of completion: 60 min, then 90 min live coding with instructor
* Solution (basic): :download:`solution/dragon_alpha_basic.py`
* Solution (advanced): :download:`solution/dragon_alpha_adv.py`
* Last update: 2020-10-01
* Warning: Don't delete code, assignment will be continued

:English:
    #. Dragon has (attributes):

        #. name
        #. position ``x`` on the screen
        #. position ``y`` on the screen
        #. texture file name, default ``img/dragon/alive.png``
        #. health points, default random ``int`` in range from 50 to 100

    #. Dragon can (methods):

        #. have position set to any place on the screen
        #. make damage in range from 5 to 20
        #. take damage
        #. move in any direction by specified value

    #. Assume left-top screen corner as a initial coordinates position:

        #. going right add to ``x``
        #. going left subtract from ``x``
        #. going up subtract from ``y``
        #. going down add to ``y``

    #. When dragon receives damage:

        * print name of the Dragon
        * health points which left

    #. When health points drop to, and below zero:

        #. Dragon is dead
        #. Set object status to dead
        #. Print ``XXX is dead``, where XXX is the name of the dragon
        #. Change texture file name to  ``img/dragon/dead.png``
        #. Print position where dragon died
        #. Return gold dropped by Dragon (random in range from 1 to 100)
        #. Dragon cannot take any more damage
        #. Dragon cannot make any more damage
        #. Dragon cannot move or have position set

    #. Run the game:

        #. Create dragon at x=50, y=120 position and name it "Wawelski"
        #. Set new position to x=10, y=20
        #. Move dragon left by 10 and down by 20
        #. Move dragon left by 10 and right by 15
        #. Move dragon right by 15 and up by 5
        #. Move dragon down by 5
        #. Dragon makes damage
        #. Make 10 points damage to the dragon
        #. Make 5 points damage to the dragon
        #. Make 3 points damage to the dragon
        #. Make 2 points damage to the dragon
        #. Make 15 points damage to the dragon
        #. Make 25 points damage to the dragon
        #. Make 75 points damage to the dragon

    #. Non-functional requirements:

        #. This is a simulation of development process
        #. Trainer act as Product Owner with little technical knowledge
        #. You are the software engineer who need to decide and live with consequences of your choices
        #. Task is a narrative story telling to demonstrate OOP and good engineering practices
        #. Calculated last position of the game should be x=20, y=40
        #. You can introduce new fields, methods, functions, variables, constants, classes, objects, whatever you want
        #. Don't use modules form outside the Python Standard Library
        #. Task is business requirements specification, not a technical documentation, i.e. "what Dragon has to do, not how to do it"
        #. You don't have to keep order of business specification while writing code
        #. This is ``alpha`` version, so no new functionality like negative position checking etc.
        #. Do not read solution or any future iterations of this exercise.
        #. If you read future tasks, you will spoil fun and what is the most important: learning.

:Polish:
    #. Smok ma (atrybuty):

        #. nazwę
        #. pozycję ``x`` na ekranie
        #. pozycję ``y`` na ekranie
        #. nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
        #. punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

    #. Smok może (metody):

        #. być ustawiony w dowolne miejsce ekranu
        #. zadawać komuś losowe obrażenia z przedziału od 5 do 20
        #. otrzymywać obrażenia
        #. być przesuwany o zadaną liczbę punktów w którymś z kierunków

    #. Przyjmij górny lewy róg ekranu za punkt początkowy:

        #. idąc w prawo dodajesz ``x``
        #. idąc w lewo odejmujesz ``x``
        #. idąc w górę odejmujesz ``y``
        #. idąc w dół dodajesz ``y``

    #. Gdy smok otrzymuje obrażenia:

        * wypisz nazwę smoka,
        * pozostałe punkty życia

    #. Kiedy punkty życia Smoka spadną do, lub poniżej zera:

        #. Smok jest martwy
        #. Ustaw status obiektu na dead
        #. Wypisz napis ``XXX is dead`` gdzie XXX to nazwa smoka
        #. Zmień nazwę pliku tekstury na ``img/dragon/dead.png``
        #. Wypisz pozycję gdzie smok zginął
        #. Zwróć ile złota smok wyrzucił (losowa 1-100)
        #. Nie można zadawać mu obrażeń
        #. Smok nie może zadawać obrażeń
        #. Smok nie może się poruszać

    #. Przeprowadź grę:

        #. Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
        #. Ustaw nową pozycję na x=10, y=20
        #. Przesuń smoka w lewo o 10 i w dół o 20
        #. Przesuń smoka w lewo o 10 i w prawo o 15
        #. Przesuń smoka w prawo o 15 i w górę o 5
        #. Przesuń smoka w dół o 5
        #. Smok zadaje obrażenia
        #. Zadaj 10 obrażeń smokowi
        #. Zadaj 5 obrażeń smokowi
        #. Zadaj 3 obrażeń smokowi
        #. Zadaj 2 obrażeń smokowi
        #. Zadaj 15 obrażeń smokowi
        #. Zadaj 25 obrażeń smokowi
        #. Zadaj 75 obrażeń smokowi

    #. Wymagania niefunkcjonalne:

        #. Zadanie jest symulacją procesu developmentu
        #. Trener zachowuje się jak Product Owner z niewielką techniczną wiedzą
        #. Ty jesteś inżynierem oprogramowania, który musi podejmować decyzje i ponosić ich konsekwencje
        #. Zadanie jest tylko narracją do demonstracji OOP i dobrych praktyk programowania
        #. Wyliczona pozycja Smoka na końcu gry powinna być x=20, y=40
        #. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stały, klasy, obiekty, co tylko chcesz
        #. Nie korzystaj z modułów spoza standardowej biblioteki Pythona
        #. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
        #. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
        #. Jest to wersja ``alpha`` więc bez dodatkowych funkcjonalności (np. sprawdzanie koordynatów, wychodzenia poza planszę itp.)
        #. Nie przeglądaj rozwiązań ani treści kolejnych (przyszłych) części zadania.
        #. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i co najważniejsze naukę.

:The whys and wherefores:
    * Object oriented thinking
    * Data modeling in OOP
    * Designing and working with objects
    * Nested objects
    * Interface specification
    * MVC architecture
    * Good Engineering Practices
    * Keep it Simple
    * Open to extensions, close for modifications

:Hints:
    * ``from random import randint``
    * ``randint`` returns random integer in range [a, b], including both end point
