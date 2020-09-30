*******
Mapping
*******


Dict
====
* Python 3.9 introduced :pep:`585` -- Type Hinting Generics In Standard Collections
* Before Python 3.9 you need ``from typing import Dict``

.. code-block:: python

    my_dict: dict = {
        'a': 'a',
        2: 2,
        3.3: 3.3
    }

.. code-block:: python

    my_dict: dict[str, int] = {
        'a': 1,
        'b': 2,
        'c': 3,
    }


TypedDict
=========
.. versionadded:: Python 3.8
    See :pep:`589`

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

.. code-block:: python
    :caption: The code below should be rejected, since 'title' is not a valid key, and the 'name' key is missing

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
