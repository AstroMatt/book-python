****************
Pre-Intermediate
****************


Select
======
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/nested_select.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write header (first line) to ``header`` variable
    #. Convert to ``list`` data from row 2, 6, 9 and add to ``result``
    #. Convert to ``tuple`` data from row 12, 15, 16 and add to ``result``
    #. Convert to ``dict`` data from row 18, 21 and add to ``result``:

        * key -> index number (18 or 21)
        * value -> species name

    #. Add empty ``set`` to ``result``
    #. Use only indexes
    #. Do not use ``for``, ``while`` or ``slice()``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    #. Przekonwertuj do ``list`` dane z wierszy 2, 6, 9 i dodaj do ``result``
    #. Przekonwertuj do ``tuple`` dane z wierszy 12, 15, 16 i dodaj do ``result``
    #. Przekonwertuj do ``dict`` dane z wierszy 18, 21 i dodaj do ``result``:

        * klucz -> numer indeksu (18 or 21)
        * wartość -> nazwa gatunku

     #. Dodaj pusty ``set`` do ``result``
     #. Użyj tylko indeksów
     #. Nie używaj ``for``, ``while`` lub ``slice()``

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:The whys and wherefores:
    * Using nested data structures
    * Using indexes
    * Type casting


Iris dataset
============
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/slice_iris.py`

:English:
    #. Use data from "Input" section (see below)
    #. Use only ``slice``
    #. Extract list ``features`` with measurements (every row must be tuple)
    #. Extract species name (every fifth element) and write to ``labels`` list
    #. Write unique species names to ``species`` set
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj tylko ``slice``
    #. Wyodrębnij listę ``features`` w pomiarami (każdy wiersz ma być krotką)
    #. Wyodrębnij nazwę gatunku (co piąty element) i zapisz do listy ``labels``
    #. Zapisz unikalne nazwy gatunków do zbioru ``species``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = (
            5.8, 2.7, 5.1, 1.9, 'virginica',
            5.1, 3.5, 1.4, 0.2, 'setosa',
            5.7, 2.8, 4.1, 1.3, 'versicolor',
            6.3, 2.9, 5.6, 1.8, 'virginica',
            6.4, 3.2, 4.5, 1.5, 'versicolor',
            4.7, 3.2, 1.3, 0.2, 'setosa',
        )

:Output:
    .. code-block:: python

        features = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2),
        ]

        labels = [
            'virginica',
            'setosa',
            'versicolor',
            'virginica',
            'versicolor',
            'setosa',
        ]

        species = {
            'versicolor',
            'setosa',
            'virginica',
        }

:The whys and wherefores:
    * Defining and using ``list``, ``tuple``, ``set``
    * Slicing sequences


``List[tuple]`` to ``List[dict]``
=================================
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/loop_dict_to_list.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header and data
    #. Print ``List[dict]``

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek i dane
    #. Wypisz ``List[dict]``

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        result: List[dict] = [
            {'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            ...
        ]

:The whys and wherefores:
    * Working with nested data structures
    * Iterating over dict and lists


Get elements from nested data structure
=======================================
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/for_nested.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Iterate over data
    #. Print species names ending with "ca" or "osa"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Oddziel nagłówek od danych
    #. Iteruj po danych
    #. Wypisz nazwy gatunków kończące się na "ca" lub "osa"

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'setosa'}),
        ]

:The whys and wherefores:
    * Accessing ``dict`` keys
    * Iterating over nested structure

Label encoder
=============
* Complexity level: medium
* Lines of code to write: 13 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/loop_label_encoder.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define:

        * ``features: List[tuple]`` - measurements
        * ``labels: List[int]`` - species

    #. Separate header from data
    #. To encode and decode ``labels`` (species) we need ``label_encoder: Dict[int, str]``:

        * key - id (incremented integer value)
        * value - species name

    #. ``label_encoder`` must be generated from ``DATA``
    #. For each row add appropriate data to ``features``, ``labels`` and ``label_encoder``
    #. Print ``features``, ``labels`` and ``label_encoder``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj:

        * ``features: List[tuple]`` - pomiary
        * ``labels: List[int]`` - gatunki
        * ``label_encoder: Dict[int, str]`` - słownik podmiany nazw gatunków

    #. Odseparuj nagłówek od danych
    #. Aby móc zakodować i odkodować ``labels`` (gatunki) potrzebny jest ``label_encoder: Dict[int, str]``:

        * key - identyfikator (kolejna liczba rzeczywista)
        * value - nazwa gatunku

    #. ``label_encoder`` musi być wygenerowany z ``DATA``
    #. Dla każdego wiersza dodawaj odpowiednie dane do ``feature``, ``labels`` i ``label_encoder``
    #. Wypisz ``feature``, ``labels`` i ``label_encoder``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        from typing import List, Dict


        features: List[tuple] = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2), ...]

        labels: List[int] = [0, 1, 2, 1, 2, 0, ...]

        label_encoder: Dict[int, str] = {
            0: 'virginica',
            1: 'setosa',
            2: 'versicolor'}


:The whys and wherefores:
    * ``dict`` lookups
    * Dynamic ``dict`` generating
    * ``dict`` reversal
