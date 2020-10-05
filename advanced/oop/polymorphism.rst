.. _OOP Polymorphism:

************
Polymorphism
************


Switch
======
.. code-block:: python
    :caption: Switch moves business logic to the execution place

    watney = 'Astronaut'

    if watney == 'Astronaut':
        print('Hello')
    elif watney == 'Cosmonaut':
        print('Привет!')
    elif watney == 'Taikonaut':
        print('你好')
    else:
        print('Default Value')

    # Hello

.. code-block:: python

    def say_hello(key=None):
        return {
            'Astronaut': 'Hello',
            'Cosmonaut': 'Привет!',
            'Taikonaut': '你好',
        }.get(key, 'Default Value')


    watney = 'Astronaut'
    ivanovic = 'Cosmonaut'
    twardowski = 'Sorcerer'

    say_hello(watney)
    # Hello

    say_hello(ivanovic)
    # Привет!

    say_hello(twardowski):
    # 'Default Value'


Polymorphism in a Function
==========================
.. code-block:: python
    :caption: Polymorphism on Function

    class Sorcerer:
        pass

    class Astronaut:
        def say_hello(self):
            return 'Hello'

    class Cosmonaut:
        def say_hello(self):
            return 'Привет!'


    def say_hello(spaceman):
        if hasattr(spaceman, 'say_hello')
            return spaceman.say_hello()
        else:
            return 'Default Value'


    watney = Astronaut()
    ivanovic = Cosmonaut()
    twardowski = Sorcerer()

    say_hello(watney)
    # Hello

    say_hello(ivanovic)
    # Привет!

    say_hello(twardowski)
    # 'Default Value'


Polymorphism on a Class
=======================
.. code-block:: python
    :caption: Polymorphism on Classes

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            return 'Hello'


    class Cosmonaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            return 'Привет!'


    crew = [
        Astronaut('Mark Watney'),
        Cosmonaut('Иван Иванович'),
        Astronaut('Matt Kowalski'),
        Cosmonaut('Jan Twardowski'),
    ]

    for member in crew:
        print(member.say_hello())
    # Hello
    # Привет!
    # Hello
    # Привет!


Factory
=======
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


    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width

        def __repr__(self):
            name = self.__class__.__name__
            values = tuple(self.__dict__.values())
            return f'\n {name}{values}'

    class Setosa(Iris):
        pass

    class Virginica(Iris):
        pass

    class Versicolor(Iris):
        pass


    def factory(species: str):
        if species == 'setosa':
            return Setosa
        if species == 'virginica':
            return Virginica
        if species == 'versicolor':
            return Versicolor

        # species = species.capitalize()
        # classes = globals()
        # return classes[species]


    result = []

    for *features, species in DATA[1:]:
        iris = factory(species)
        i = iris(*features)
        result.append(i)

    print(result)
    # [Virginica(5.8, 2.7, 5.1, 1.9),
    #  Setosa(5.1, 3.5, 1.4, 0.2),
    #  Versicolor(5.7, 2.8, 4.1, 1.3),
    #  Virginica(6.3, 2.9, 5.6, 1.8),
    #  Versicolor(6.4, 3.2, 4.5, 1.5),
    #  Setosa(4.7, 3.2, 1.3, 0.2),
    #  Versicolor(7.0, 3.2, 4.7, 1.4),
    #  Virginica(7.6, 3.0, 6.6, 2.1),
    #  Setosa(4.9, 3.0, 1.4, 0.2),
    #  Virginica(4.9, 2.5, 4.5, 1.7),
    #  Virginica(7.1, 3.0, 5.9, 2.1),
    #  Setosa(4.6, 3.4, 1.4, 0.3),
    #  Setosa(5.4, 3.9, 1.7, 0.4),
    #  Versicolor(5.7, 2.8, 4.5, 1.3),
    #  Setosa(5.0, 3.6, 1.4, 0.3),
    #  Versicolor(5.5, 2.3, 4.0, 1.3),
    #  Virginica(6.5, 3.0, 5.8, 2.2),
    #  Versicolor(6.5, 2.8, 4.6, 1.5),
    #  Virginica(6.3, 3.3, 6.0, 2.5),
    #  Versicolor(6.9, 3.1, 4.9, 1.5),
    #  Setosa(4.6, 3.1, 1.5, 0.2)]

.. code-block:: python

    from dataclasses import dataclass

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


    @dataclass
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float

    class Setosa(Iris):
        pass

    class Virginica(Iris):
        pass

    class Versicolor(Iris):
        pass


    def factory(species: str):
        species = species.capitalize()
        classes = globals()
        return classes[species]


    result = [
        factory(species)(*features)
        for *features, species in DATA[1:]
    ]

    print(result)
    # [Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
    #  Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
    #  Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
    #  Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
    #  Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
    #  Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2),
    #  Versicolor(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4),
    #  Virginica(sepal_length=7.6, sepal_width=3.0, petal_length=6.6, petal_width=2.1),
    #  Setosa(sepal_length=4.9, sepal_width=3.0, petal_length=1.4, petal_width=0.2),
    #  Virginica(sepal_length=4.9, sepal_width=2.5, petal_length=4.5, petal_width=1.7),
    #  Virginica(sepal_length=7.1, sepal_width=3.0, petal_length=5.9, petal_width=2.1),
    #  Setosa(sepal_length=4.6, sepal_width=3.4, petal_length=1.4, petal_width=0.3),
    #  Setosa(sepal_length=5.4, sepal_width=3.9, petal_length=1.7, petal_width=0.4),
    #  Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.5, petal_width=1.3),
    #  Setosa(sepal_length=5.0, sepal_width=3.6, petal_length=1.4, petal_width=0.3),
    #  Versicolor(sepal_length=5.5, sepal_width=2.3, petal_length=4.0, petal_width=1.3),
    #  Virginica(sepal_length=6.5, sepal_width=3.0, petal_length=5.8, petal_width=2.2),
    #  Versicolor(sepal_length=6.5, sepal_width=2.8, petal_length=4.6, petal_width=1.5),
    #  Virginica(sepal_length=6.3, sepal_width=3.3, petal_length=6.0, petal_width=2.5),
    #  Versicolor(sepal_length=6.9, sepal_width=3.1, petal_length=4.9, petal_width=1.5),
    #  Setosa(sepal_length=4.6, sepal_width=3.1, petal_length=1.5, petal_width=0.2)]


Assignments
===========
.. todo:: Create assignments
