"""
* Assignment: Decorator Class Type Check
* Filename: decorator_cls_typecheck.py
* Complexity: medium
* Lines of code to write: 15 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator class `TypeCheck`
    3. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    4. Decorator checks return type
    5. In case when received type is not expected throw an exception `TypeError` with:
        a. argument name
        b. actual type
        c. expected type
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator klasę `TypeCheck`
    3. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
    4. Dekorator sprawdza typ zwracany
    5. W przypadku gdy otrzymany typ nie jest równy oczekiwanemu wyrzuć wyjątek `TypeError` z:
        a. nazwa argumentu
        b. aktualny typ
        c. oczekiwany typ
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `echo.__annotations__`

Tests:
    >>> @TypeCheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return bool(a * b)

    >>> echo('one', 1)
    True
    >>> echo('one', 1, 1.1)
    True
    >>> echo('one', b=1)
    True
    >>> echo('one', 1, c=1.1)
    True
    >>> echo('one', b=1, c=1.1)
    True
    >>> echo(a='one', b=1, c=1.1)
    True
    >>> echo(c=1.1, b=1, a='one')
    True
    >>> echo(b=1, c=1.1, a='one')
    True
    >>> echo('one', c=1.1, b=1)
    True
    >>> echo(1, 1)
    Traceback (most recent call last):
    TypeError: "a" is <class 'int'>, but <class 'str'> was expected

    >>> echo('one', 'two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected

    >>> echo('one', 1, 'two')
    Traceback (most recent call last):
    TypeError: "c" is <class 'str'>, but <class 'float'> was expected

    >>> echo(b='one', a='two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected

    >>> echo('one', c=1.1, b=1.1)
    Traceback (most recent call last):
    TypeError: "b" is <class 'float'>, but <class 'int'> was expected
"""


# Given
def decorator(func):
    def validate(argname, argval):
        argtype = type(argval)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')

    def merge(*args, **kwargs):
        args = dict(zip(func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def wrapper(*args, **kwargs):
        for argname, argval in merge(*args, **kwargs).items():
            validate(argname, argval)

        result = func(*args, **kwargs)
        validate('return', result)
        return result
    return wrapper


# Solution
class TypeCheck:
    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_arguments(*args, **kwargs)
        result = self._func(*args, **kwargs)
        self.check_result(result)
        return result

    def check_arguments(self, *args, **kwargs):
        for argname, argval in self.merge(*args, **kwargs).items():
            self.validate(argname, argval)

    def check_result(self, result):
        self.validate('return', result)

    def merge(self, *args, **kwargs):
        args = dict(zip(self._func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def validate(self, argname, argval):
        argtype = type(argval)
        expected = self._func.__annotations__[argname]

        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')
