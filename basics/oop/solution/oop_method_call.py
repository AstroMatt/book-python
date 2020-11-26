"""
* Assignment: OOP Method Call
* Filename: oop_method_call.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Stats`
    3. Define method `mean()` in `Stats` class
    4. Method takes `data: list[float]` as an argument
    5. Method returns arithmetic mean of the `data`
    6. Returned value must me rounded to one decimal places
    7. Create instance of `Stats` class
    8. Iterate over `DATA` skipping header
    9. Separate features from label
    10. Call `mean()` method of `Stats` class passing list of features as an argument
    11. Define `result: list[float]` with list of means from each row
    12. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Stats`
    3. Zdefiniuj metodę `mean()` w klasie `Stats`
    4. Metoda przyjmuje `data: list[float]` jako argument
    5. Metoda zwraca średnią arytmetyczną z `data`
    6. Zwracana value ma być zaokrąglona do jednego miejsca po przecinku
    7. Stwórz instancję klasy `Stats`
    8. Iteruj po `DATA` pomijając nagłówek
    9. Rozdziel cechy od etykiety
    10. Wywołuj metodę `mean()` klasy `Stats` przekazując listę features jako argument
    11. Zdefiniuj `result: list[float]` z listą średnich każdego z wierszy
    12. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `round()`

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is float for x in result)
    >>> result
    [3.9, 2.5, 3.5, 4.1, 3.9, 2.4]
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


# Solution
class Stats:
    def mean(self, data):
        mean = sum(data) / len(data)
        return round(mean, 1)


stats = Stats()

# Solution 1
result = [stats.mean(X) for *X,y in DATA[1:]]

# Solution 2
# result = []
# for *features, label in DATA[1:]:
#     result.append(stats.mean(features))

