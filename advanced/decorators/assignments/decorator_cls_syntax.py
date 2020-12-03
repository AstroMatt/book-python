"""
* Assignment: Decorator Class Syntax
* Filename: decorator_cls_syntax.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create decorator class `MyDecorator`
    2. `MyDecorator` should have `__init__` which takes function as an argument
    3. `MyDecorator` should have `__call__` with parameters: `*args` and `**kwargs`
    4. `__call__` should call original function with original parameters,
       and return its value
    5. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz dekorator klasę `MyDecorator`
    2. `MyDecorator` powinien mieć `__init__`, który przyjmuje funkcję jako argument
    3. `MyDecorator` powinien mieć `__call__` z parameterami: `*args` i `**kwargs`
    4.`__call__` powinien wywoływać oryginalną funkcję oryginalnymi
       parametrami i zwracać jej wartość
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(MyDecorator)
    >>> assert isinstance(MyDecorator(lambda: None), MyDecorator)

    >>> @MyDecorator
    ... def echo(text):
    ...     return text

    >>> echo('hello')
    'hello'
"""


# Solution
class MyDecorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)
