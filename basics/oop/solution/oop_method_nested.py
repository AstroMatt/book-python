"""
* Assignment: OOP Method Nested
* Filename: oop_method_nested.py
* Complexity: medium
* Lines of code to write: 15 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class ``Iris``
    3. ``Iris`` has:
        a. "Sepal length" type ``float``
        b. "Sepal width" type ``float``
        c. "Petal length" type ``float``
        d. "Petal width" type ``float``
        e. "Species" type ``str``
    4. ``Iris`` can:
        a. Return number of ``float`` type attributes
        b. Return list of all ``float`` type attributes
        c. Return sum of values of all ``float`` type attributes
        d. Return mean of all ``float`` type attributes
    5. Use ``self.__dict__`` iteration to return values of numeric fields
    6. Create ``setosa`` object with attributes set at the initialization
    7. Create ``virginica`` object with attributes set at the initialization
    8. Print sum, mean and species name of each objects
    9. Do not use ``@dataclass``
    10. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę ``Iris``
    3. ``Iris`` ma:
        a. "Sepal length" typu ``float``
        b. "Sepal width" typu ``float``
        c. "Petal length" typu ``float``
        d. "Petal width" typu ``float``
        e. "Species" typu ``str``
    4. ``Iris`` może:
        a. Zwrócić liczbę pól typu ``float``
        b. Zwrócić listę wartości wszystkich pól typu ``float``
        c. Zwrócić sumę wartości pól typu ``float``
        d. Zwrócić średnią arytmetyczną wartość pól typu ``float``
    5. Użyj iterowania po ``self.__dict__`` do zwrócenia wartości pól numerycznych
    6. Stwórz obiekt ``setosa`` z atrybutami ustawionymi przy inicjalizacji
    7. Stwórz obiekt ``virginica`` z atrybutami ustawionymi przy inicjalizacji
    8. Wypisz sumę, średnią oraz nazwę gatunku każdego z obiektów
    9. Nie używaj ``@dataclass``
    10. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * ``isinstance(value, float)``
    * ``self.__dict__.items()``

Tests:
    >>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
    >>> setosa.show()
    'total=10.20 mean=2.55 setosa'
    >>> virginica.show()
    'total=15.50 mean=3.88 virginica'
"""

# Given
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


# Solution
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_numeric_values(self):
        return [v for k,v in self.__dict__.items() if isinstance(v, float)]

    def total(self):
        return sum(self.get_numeric_values())

    def length(self):
        return len(self.get_numeric_values())

    def mean(self):
        return self.total() / self.length()

    def show(self):
        return f'total={self.total():.2f} mean={self.mean():.2f} {self.species}'

