"""
* Assignment: Decorator Function Syntax
* Filename: decorator_func_syntax.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 5 min

English:
    1. Create decorator `mydecorator`
    2. Decorator should have `wrapper` with `*args` and `**kwargs` parameters
    3. Wrapper should call original function with it's original parameters,
       and return its value
    4. Decorator should return `wrapper` function
    5. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz dekorator `mydecorator`
    2. Dekorator powinien mieć `wrapper` z parametrami `*args` i `**kwargs`
    3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
       parametrami i zwracać jej wartość
    4. Decorator powinien zwracać funckję `wrapper`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(mydecorator)
    >>> assert isfunction(mydecorator(lambda: None))

    >>> @mydecorator
    ... def echo(text):
    ...     return text

    >>> echo('hello')
    'hello'
"""


# Solution
def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

