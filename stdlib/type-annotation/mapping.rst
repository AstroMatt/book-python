*******
Mapping
*******


Dict
====
* Before Python 3.9 you need ``from typing import Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections

.. code-block:: python

    data: dict = {
        'a': 'a',
        2: 2,
        3.3: 3.3}

.. code-block:: python

    data: dict[str, int] = {
        'a': 1,
        'b': 2,
        'c': 3,}


TypedDict
=========
* Since Python 3.8: :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

.. code-block:: python

    from typing import TypedDict


    class Movie(TypedDict):
        name: str
        year: int


    movie: Movie = {
        'name': 'Blade Runner',
        'year': 1982
    }

    def record_movie(movie: Movie) -> None:
        ...

    record_movie({'name': 'Blade Runner', 'year': 1982})

The code below should be rejected, since 'title' is not a valid key, and the 'name' key is missing:

.. code-block:: python

    from typing import TypedDict


    class Movie(TypedDict):
        name: str
        year: int

    movie2: Movie = {
        'title': 'Blade Runner',
        'year': 1982
    }

.. code-block:: python

    from typing import TypedDict


    class Movie(TypedDict):
        name: str
        year: int

    m = Movie(name='Blade Runner', year=1982)

.. code-block:: python

    from typing import TypedDict


    class Movie(TypedDict):
        name: str
        year: int

    m: Movie = dict(
        name='Alien',
        year=1979,
        director='Ridley Scott')  # error: Unexpected key 'director'


.. code-block:: python

    from typing import TypedDict


    class Movie(TypedDict):
        name: str
        year: int

    class BookBasedMovie(Movie):
        based_on: str

.. code-block:: python

    from typing import TypedDict


    class X(TypedDict):
        x: int

    class Y(TypedDict):
        y: str

    class XYZ(X, Y):
        z: bool
