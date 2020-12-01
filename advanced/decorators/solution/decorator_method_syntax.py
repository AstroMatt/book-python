"""
* Assignment: Decorator Method Syntax
* Filename: decorator_method_syntax.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 5 min

English:
    1. Create method decorator `mydecorator`
    2. Decorator should have `wrapper` with `self`, `*args` and `**kwargs` parameters
    3. Wrapper should call original method with it's original parameters,
       and return its value
    4. Decorator should return `wrapper` method
    5. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz dekorator metod `mydecorator`
    2. Dekorator powinien mieć `wrapper` z parametrami `*args` i `**kwargs`
    3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
       parametrami i zwracać jej wartość
    4. Decorator powinien zwracać metodę `wrapper`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(mydecorator)
    >>> assert isfunction(mydecorator(lambda: None))

    >>> class MyClass:
    ...     @mydecorator
    ...     def echo(text):
    ...         return text

    >>> my = MyClass()
    >>> my.echo('hello')
    'hello'
"""


# Solution
def mydecorator(method):
    def wrapper(self, *args, **kwargs):
        return method(*args, **kwargs)
    return wrapper

