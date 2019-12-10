****
Exam
****


Dragon (version beta)
=====================
* Complexity level: medium
* Lines of code to write: 120 lines
* Estimated time of completion: 30 min (±10 min), then 30 min live coding with instructor
* Filename: :download:`solution/intermediate_dragon.py`
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Zaimportuj smoka z poprzedniej części zadania ("Part 1")
#. Wykorzystaj mechanizm dziedziczenia dla Smoka
#. Nie modyfikuj klasy smoka z poprzedniej części
#. Smok nie może wyjść poza obszar ekranu (1024x768) + napisz ``doctest``
#. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
#. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
#. Stwórz bohatera "Jan Twardowski":

    * losowe punkty życia (200-250)
    * zadaje losowe obrażenia (1-15)
    * klasa postaci (domyślnie "Warrior")
    * Bohater może przyjmować obrażenia
    * Bohater może zginąć
    * Bohater może poruszać się po planszy

#. Wszystkie istoty mają statusy:

    * "Full Health" - gdy punkty życia 100% (zastąp status "alive")
    * "Injured" - gdy punkty życia 99% - 75%
    * "Badly Wounded" - gdy punkty życia 74% - 25%
    * "Near Death" - gdy punkty życia 24% - 1%
    * "Dead" - gdy punkty życia poniżej lub równe 0%

#. Bohater przejmuje złoto smoka, jeżeli go zabije
#. Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie
#. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

:Hint:
    * Aby zaimportować trzeba najpierw w katalogu stworzyć pusty plik ``__init__.py``
