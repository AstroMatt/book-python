.. _Dragon RC:

*********
Exit Exam
*********


Dragon (version release candidate)
==================================
* Complexity level: hard
* Lines of code to write: 50 lines
* Estimated time of completion: 30 min
* Solution: :download:`solution/dragon_rc.py`

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Dodaj możliwość poruszania się smoka i bohatera w 3 wymiarach
#. Bohater może należeć do drużyny, który może składać się maks z 6 postaci (różnych klas)
#. Żadna z istot na planszy nie może wyjść poza zakres ekranu
#. Bohater może dodatkowo założyć ekwipunek i może być to wiele obiektów na raz
#. Każdy z przedmiotów ma swoją nazwę, typ oraz modyfikator

    * zbroję (dodatkowe punkty obrony, np. +10%)
    * tarczę (dodatkowe punkty obrony, np. +5%)
    * miecz (dodatkowe punkty ataku, np. +5%)

#. Zbroja i tarcza chroni przed uderzeniami obniżając ilość obrażeń o wartość obrony
#. Miecz zwiększa ilość zadawanych obrażeń
#. Obrażenia smoka maleją z sześcianem odległości (zianie ogniem)
#. Bohater nie może zadawać obrażeń jak jest dalej niż 50 punktów od przeciwnika
#. Wszystkie istoty mogą levelować a bazowe punty życia i obrażeń się zmieniają z poziomem
#. Przeprowadź symulację walki. Kto zginie pierwszy?
