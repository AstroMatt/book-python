Assignments
===========

Trigonometry
------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/matplotlib_trigonometry.py`

#. Dla ``x`` z przedziału od 0.0 do 1.0 z próbkowaniem co 0.01 przedstaw przebiegi funkcji ``sin``, ``cos`` dla parametrów ``2 * np.pi * x``
#. Stwórz dwa osobne obrazki (figure):

    * Każdy z przebiegów na osobnym subplot
    * Na jednym plot dwa przebiegi funkcji

#. Wykresy (``subplot``) mają być jeden nad drugim
#. Wykresy podpisz nazwą funkcji trygonometrycznej
#. Tekst etykiety osi ``y`` ustaw na "Wartość funkcji"
#. Pokoloruj nazwy thicków ``x`` dla wykresu ``sin`` na czerwono
#. Pokoloruj nazwę (label) dla ``cos`` na kolor zielony
#. Na obu wykresach pokaż grid
#. Narysuj drugi obrazek z nałożonymi na jeden plot wykresami obu funkcji

:Hint:
    * ``np.sin()``
    * ``np.cos()``

Iris scatter
------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/matplotlib_iris.py`
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv

#. Z podanego powyżej adresu URL pobierz dane
#. Dla każdego gatunku
#. Dane stosunku ``sepal_length`` do ``sepal_width`` zwizualizuj w formie ``scatter`` za pomocą ``matplotlib``
#. Każdy gatunek powinien mieć inny kolor

:Hint:
    * ``pd.groupby()``

Random points
-------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/matplotlib_random_points.py`

#. Wygeneruj 100 losowych punktów:

    * rozkład gaussa o średniej 0
    * o odchyleniu standardowym równym 0.2

#. Punkty muszą być wylosowane wokół dwóch wybranych punktów (``A = (0, 1)``, `B = (2, 4)``).
#. Funkcja musi przechodzić ``doctest``

.. code-block:: python

    def random_point(center, std: int = 0.2):
        """
        >>> random.seed(1); random_point((0,0), std=0.2)
        (0.2576369506310926, 0.2898891217399542)

        >>> random.seed(1); random_point((0,0))
        (0.2576369506310926, 0.2898891217399542)

        >>> random.seed(1); random_point((2,5), std=10)
        (14.881847531554628, 19.494456086997708)

        >>> random.seed(1); random_point((2,5), std=(0.1, 12))
        (2.1288184753155464, 22.393347304397253)
        """
        pass


#. Wyrysuj te punkty na wykresie (możesz użyć funkcji ``plt.axis('equal')`` żeby osie wykresu były w tej samej skali).
#. Punkt A i punkty wygenerowane na jego podstawie wyrysuj kolorem czerwonym
#. punkt B i punkty wygenerowane na jego podstawie wyrysuj kolorem niebieskim
#. Możesz do tego celu napisać funkcję ``plot_point(point, color)``, która przyjmuje punkt (dwuelementowy tuple, lub listę, z czego pierwszy element to współrzędna x, a druga to y), i kolor i doda ten punkt do aktualnie aktywnego rysunku.
#. Korzystając z funkcji napisanej w ćwiczeniu powyżej oblicz odległość od każdego z punktów do punktów A i B
#. Na podstawie tej odległości zaklasyfikuj te punkty

    * jeżeli punkt jest bliżej punktu A to należy do zbioru A
    * jeżeli jest bliżej do zbioru B to należy do zbioru B

#. Narysuj nowy wykres, na którym:

    * punkty ze zbioru A będą narysowane kolorem czerwonym,
    * punkty ze zbioru B będą narysowane kolorem niebieskim.

#. Czy dwa wykresy są takie same?
#. Co się stanie jeżeli będziemy zwiększali odchylenie standardowe przy generacji punktów?
#. Albo przybliżymy do siebie punkty A i B?

:Hints:
    * argument ``color='red'`` w funkcji ``plt.plot``

Color graph
-----------
#. Dokonano pomiarów z urządzeń temperatury
#. Wygeneruj listę ``dict`` z datami z ostatniego miesiąca oraz wartością pomiarów losowo 10-15 plus szum na poziomie 0.5 stopnia celsiusza (wykrzystaj ``np.gauss()``)
#. Mając do dyspozycji szereg czasowy, gdzie dla każdego dnia wykonano pomiar temperatury
#. Przedstaw na wykresie dane szeregu czasowego
#. Oś z datami przedstaw przekrzywioną o 45 stopni
#. Na osi y przedstawiaj tylko pełne ``int``
#. Dodaj Colorbar ze skalą temperatur zimno-ciepło
#. Użyj kolorów niebieski (zimno), czerwony (ciepło)
#. Wykres ma mieć grid
