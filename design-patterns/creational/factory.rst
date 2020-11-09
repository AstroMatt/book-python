*******
Factory
*******


.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    file2 = Document('myfile.docx')

    print(file1)
    # <__main__.PDF object at 0x10f89afa0>

    print(file2)
    # <__main__.Docx object at 0x10f6fe9a0>

.. literalinclude:: src/design-patterns-factory-1.py
    :language: python
    :caption: Factory Design Pattern

.. literalinclude:: src/design-patterns-factory-2.py
    :language: python
    :caption: Factory Design Pattern

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        cls = {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'virginica': Virginica,
        }.get(species, None)

        if not cls:
            raise NotImplementedError

        return cls

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        return {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'virginica': Virginica,
        }.get(species, None)

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    import sys


    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        try:
            CURRENT_MODULE = sys.modules[__name__]
            return getattr(CURRENT_MODULE, species.capitalize())
        except AttributeError:
            raise NotImplementedError


    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>
