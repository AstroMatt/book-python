***********
Code Smells
***********


Source :cite:`CodeSmells`


#. Using globals - but that is a code smell in any language.
#. Using ``eval`` and ``exec`` unless the input is tightly controlled.
#. Using ``range`` over the ``length`` of a container to iterate over the container, or get the index.
#. Creating a ``list`` of values, when you don’t need to keep the ``list`` - a generator is often better.
#. Having getter and setter methods rather than using properties.
#. Having named methods with similar semantics to existing operators, instead of overriding the magic methods those operators use (eg. having an add method rather than overriding ``__add__()`` and ``__iadd__()`` ) .
#. Using nested loops to combine two iterables rather than using something out of ``itertools``.
#. Having lots of code and classes in a single module rather than having a sensible split of code into well named modules.
#. Unit tests that don’t use mock (or similar).
#. Modules, classes, methods and functions with no ``docstring``
#. Methods and functions which return a value to signify an error rather raising an exception.
#. Using open and similar without using ``with``.
#. Using mutable values as a default arguments value (without a clear comment stating it is deliberate)
#. Using explicit loop to build a ``list``/``set``/``dict`` rather than a comprehension.
#. Using system to call OS commands rather than using ``shutil`` methods.
#. Using ``str`` manipulation (slicing etc) to build file paths rather than use ``os.path`` or ``pathlib``.
#. You code has a function which is a reimplementation of code in the standard library.
#. You have started a new Project in 2019 (or late 2018) which uses Python2, without a good technical reason. It being what you learnt is not a good technical reason - if you learnt Python2 then you can learn Python3.


Bad practice
============

``range(len())``
----------------
* Very common bad practice
* poor variable naming and readability
* ``range(len(...))`` will evaluate generator to calculate length
* ``DATA[i]`` lookups has ``O(n)`` complexity!!
* Does not use generator at all!

.. code-block:: python
    :caption: Bad practice

    DATA = ['a', 'b', 'c']

    for i in range(len(DATA)):
        print(DATA[i])

    # a
    # b
    # c

.. code-block:: python
    :caption: Better solution

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # a
    # b
    # c

Example 1
---------
* Fixing to only valid solution

.. code-block:: python

    a = 'UL. JANA III SOBIESKIEGO 1/2'
    b = 'ulica Jana III Sobieskiego 1 apt 2'
    c = 'os. Jana III Sobieskiego'
    d = 'plac Jana III SobieSKiego 1/2'
    e = 'aleja JANA III Sobieskiego'
    f = 'alei Jana III Sobieskiego 1/2'
    g = 'ul. jana III SOBIESKIEGO 1 m. 2'
    h = 'os. Jana Iii Sobieskiego 1 apt 2'

    a_prim=a[4:-4].title().replace(a[9:12],a[9:12].upper())
    a_prim=a_prim.replace(a_prim[6:9],a_prim[6:9].upper())

    dl=len(a_prim)


    b_prim=b[6:6+dl]
    c_prim=c[4:4+dl]
    d_prim=d[5:5+dl].replace('SK','sk')
    e_prim=e[6:6+dl]
    e_prim=e_prim.replace(e_prim[1:4],e_prim[1:4].lower())
    f_prim=f[5:5+dl]
    g_prim=g[4:4+dl]
    g_prim=g_prim[0].upper() + g_prim[1:9]+ g_prim[9:].title()
    h_prim=h[4:4+dl]
    h_prim=h_prim.replace(h_prim[5:8],h_prim[5:8].upper())
    #%%
    print(a_prim)
    print(b_prim)
    print(c_prim)
    print(d_prim)
    print(e_prim)
    print(f_prim)
    print(g_prim)
    print(h_prim)

Example 2
---------
* Adding strings ?!

.. code-block:: python

    DATA = [
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa'),
     (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

    features=[]
    species=[]

    for i in DATA:
        fet=(str(i)[1:19],)
        spe=str(i)[22:-2]
        features.append(fet)
        species.append(spe)

    print(features)
    print(species)

Example 3
---------
* Try to change: not power of two, but power of three
* How to do that?

.. code-block:: python

    import numpy as np
    import pandas as pd


    np.random.seed(0)

    A=np.random.randint(0, 1025, 50*50).reshape((50,50))
    B=[]

    for i in A:
        for j in i:
            if (j & (j-1))==0 and j!=0 and j not in B:
                B.append(j)

    B=np.asarray(B)
    B=np.sort(B)

    df_A=pd.DataFrame(A)
    mask=df_A>=10

    df_A[mask]=np.nan
    df_A_clean=df_A.dropna(how='all')
    df_A_clean.fillna(0, inplace=True)
    df_A_clean
    df_A_clean.describe()

Example 4
---------
* Using ``numpy`` everywhere
* Methods?!
* Passing all variables to ``__init__()`` instead of ``*args``, ``**kwargs``

.. code-block:: python

    """
    Napisz metody total() oraz average(), które będą wyliczały
    odpowiednio sumę lub średnią z wszystkich pomiarów sepal_length,
    sepal_width, petal_length, petal_width dla danego obiektu.
    """

    import numpy as np


    class Iris():
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width

        def __repr__(self):
            return f'{self.sepal_length}, {self.sepal_width}, {self.petal_length}, {self.petal_width}, {self.species}'


    class Virginica(Iris):
        def __init__(self, sepal_length,sepal_width, petal_length, petal_width):
            Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
            self.species='virginica'

    class Versicolor(Iris):
        def __init__(self, sepal_length,sepal_width, petal_length, petal_width):
            Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
            self.species='versicolor'

    class Setosa(Iris):
        def __init__(self, sepal_length,sepal_width, petal_length, petal_width):
            Iris.__init__(self, sepal_length,sepal_width, petal_length, petal_width)
            self.species='setosa'


    def ttl(iris):
        tmp = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        return np.sum(tmp)

    def avg(iris):
        tmp = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        return np.mean(tmp)

    a = Setosa(1,2,3,4)
    print(a)

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
     (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

    DATA_2=DATA[1:]
    for item in DATA_2:
        if item[4]=='virginica':
            v1=Virginica(item[0], item[1], item[2], item[3])
        elif item[4]=='versicolor':
            v1=Versicolor(item[0], item[1], item[2], item[3])
        elif item[4]=='setosa':
            v1=Setosa(item[0], item[1], item[2], item[3])


        print(item[4])
        print(v1.total())
        print(v1.average())

Example 6
---------
* Very common bad practice
* poor variable naming and readability
* ``range(len(...))`` will evaluate generator to calculate length
* ``DATA[i]`` lookups has ``O(n)`` complexity!!
* Does not use generator at all!
* Use ``.startswith()`` to check not ``str[0]``

.. code-block:: python
    :caption: Bad practice

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
        (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
        (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
        (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
        (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
        (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
        (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
        (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
        (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
    ]

    for i in range(1, len(DATA)):
        if DATA[i][-1]['species'][0] == 'v':
            print(DATA[i][-1]['species'])

.. code-block:: python
    :caption: Pythonic way

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
        (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
        (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
        (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
        (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
        (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
        (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
        (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
        (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
    ]

    header, *data = DATA

    for *measurements, species in data:
        species = species['species']

        if species.startswith('v'):
            print(species)
