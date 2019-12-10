**************
OOP Basic Exam
**************


Dragon (version alpha)
======================
* Complexity level: medium
* Lines of code to write: 120 lines
* Estimated time of completion: 60 min (±15 min), then 60 min live coding with instructor
* Filename: :download:`solution/basic_dragon_foundation.py` or :download:`solution/basic_dragon_advanced.py`
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

:English:
    #. Dragon has:

        #. name
        #. position ``x`` on the screen
        #. position ``y`` on the screen
        #. texture file name, default ``img/dragon/alive.png``
        #. health points, default random ``int`` in range from 50 to 100

    #. Dragon can:

        #. have position set to any place on the screen
        #. make damage in range from 5 to 20
        #. take damage
        #. move in any direction by specified value

    #. Assume left-top screen corner as a initial coordinates position:

        #. going right add to ``x``
        #. going left subtract from ``x``
        #. going up subtract from ``y``
        #. going down add to ``y``

    #. After each hit, print on the screen: name of the Dragon, damage taken, current health points
    #. When health points drop to, and below zero:

        #. Dragon is dead
        #. Set object status to dead
        #. Print on the screen ``XXX is dead``, where XXX is the name of the dragon
        #. Change texture file name to  ``img/dragon/dead.png``
        #. Print on the screen how much gold Dragon dropped (random in range from 1 to 100)
        #. Print on the screen position where dragon died
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
        #. Make 10 points damage to the dragon
        #. Make 5 points damage to the dragon
        #. Make 3 points damage to the dragon
        #. Make 2 points damage to the dragon
        #. Make 15 points damage to the dragon
        #. Make 25 points damage to the dragon
        #. Make 75 points damage to the dragon

:Non-functional requirements:
    * Task is a narrative story telling to demonstrate OOP and good engineering practices
    * Last position should be x=20, y=40
    * You can introduce new fields, methods, functions, variables, constants, classes, objects, whatever you want
    * Task is business requirements specification, not a technical documentation, i.e. "what Dragon has to do, not how to do it"
    * You don't have to keep order of business specification while writing code
    * This is ``alpha`` version, so no new functionality like negative position checking
    * Do not read any future iterations of this exercise. This is a simulation of development process. If you read future tasks, you will spoil fun and learning.

:Polish:
    #. Smok ma:

        #. nazwę
        #. pozycję ``x`` na ekranie
        #. pozycję ``y`` na ekranie
        #. nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
        #. punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

    #. Smok może:

        #. być ustawiony w dowolne miejsce ekranu
        #. zadawać komuś losowe obrażenia z przedziału od 5 do 20
        #. otrzymywać obrażenia
        #. być przesuwany o zadaną liczbę punktów w którymś z kierunków

    #. Przyjmij górny lewy róg ekranu za punkt początkowy:

        #. idąc w prawo dodajesz ``x``
        #. idąc w lewo odejmujesz ``x``
        #. idąc w górę odejmujesz ``y``
        #. idąc w dół dodajesz ``y``

    #. Przy każdym obrażeniu wypisz na ekranie nazwę Smoka, ilość obrażeń i pozostałe punkty życia
    #. Kiedy punkty życia Smoka spadną do, lub poniżej zera:

        #. Smok jest martwy
        #. ustaw status obiektu na dead
        #. na ekranie ma pojawić się napis ``XXX is dead`` gdzie XXX to nazwa smoka
        #. zmień nazwę pliku tekstury na ``img/dragon/dead.png``
        #. na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
        #. na ekranie pojawi się informacja o pozycji gdzie smok zginął
        #. Nie można zadawać mu obrażeń
        #. Smok nie może zadawać obrażeń
        #. Smok nie może się poruszać

    #. Przeprowadź grę:

        #. Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
        #. Ustaw nową pozycję na x=10, y=20
        #. Przesuń smoka w lewo o 10 i w dół o 20
        #. Przesuń smoka w lewo o 10 i w prawo o 15
        #. Przesuń smoka w prawo o 15 i w górę o 5
        #. Przesuń smoka w dół o 5
        #. Zadaj 10 obrażeń smokowi
        #. Zadaj 5 obrażeń smokowi
        #. Zadaj 3 obrażeń smokowi
        #. Zadaj 2 obrażeń smokowi
        #. Zadaj 15 obrażeń smokowi
        #. Zadaj 25 obrażeń smokowi
        #. Zadaj 75 obrażeń smokowi

:Wymagania niefunkcjonalne:
    * Zadanie jest tylko narracją do demonstracji OOP i dobrych praktyk programowania
    * Pozycja Smoka na końcu powinna być x=20, y=40
    * Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stały, klasy, obiekty, co tylko chcesz
    * Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
    * Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
    * Jest to wersja ``alpha`` więc bez dodatkowych funkcjonalności (np. sprawdzanie koordynatów)
    * Nie przeglądaj kolejnych (przyszłych) części zadania. Zadanie jest symulacją procesu developmentu. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę.

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

:Hint:
    * ``from random import randint``
