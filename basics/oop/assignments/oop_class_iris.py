"""
* Assignment: OOP Class Iris
* Filename: oop_class_iris.py
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 3 min

English:
    1. Define class `Iris`
    2. Create instance `setosa` of a class `Iris`
    3. Create instance `virginica` of a class `Iris`
    4. Create instance `versicolor` of a class `Iris`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Iris`
    2. Stwórz instancję `setosa` klasy `Iris`
    3. Stwórz instancję `virginica` klasy `Iris`
    4. Stwórz instancję `versicolor` klasy `Iris`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Iris)
    >>> assert isinstance(setosa, Iris)
    >>> assert isinstance(versicolor, Iris)
    >>> assert isinstance(virginica, Iris)
"""


# Solution
class Iris:
    pass


setosa = Iris()
versicolor = Iris()
virginica = Iris()
