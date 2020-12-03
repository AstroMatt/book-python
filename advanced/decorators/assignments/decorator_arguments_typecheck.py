"""
* Assignment: Decorator Arguments Type Check
* Filename: decorator_arguments_typecheck.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator function `typecheck`
    3. Decorator checks return type only if `check_return` is `True`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator funkcję `typecheck`
    3. Dekorator sprawdza typ zwracany tylko gdy `check_return` jest `True`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `echo.__annotations__`

Tests:
    >>> @typecheck(check_return=True)
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
def typecheck(check_return: bool = True):
    def decorator(func):
        def validate(argname, argval):
            argtype = type(argval)
            expected = func.__annotations__[argname]
            if argtype is not expected:
                raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')

        def merge(*args, **kwargs):
            args = dict(zip(func.__annotations__.keys(), args))
            return kwargs | args  # Python 3.9
            # return {**args, **kwargs)}  # Python 3.7, 3.8

        def wrapper(*args, **kwargs):
            for argname, argval in merge(*args, **kwargs).items():
                validate(argname, argval)

            result = func(*args, **kwargs)
            if check_return:
                validate('return', result)
            return result
        return wrapper
    return decorator
