*************
Introspection
*************

.. code-block:: python

    def annotated(x: int, y: str) -> bool:
        return x < y

    print(annotated.__annotations__)
    # {'y': <class 'str'>, 'return': <class 'bool'>, 'x': <class 'int'>}
