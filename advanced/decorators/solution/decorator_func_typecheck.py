"""
* Assignment: Decorator Function Type Check
* Filename: decorator_func_typecheck.py
* Complexity: hard
* Lines of code to write: 15 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator function `typecheck`
    3. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    4. Decorator checks return type
    5. In case when received type is not expected throw an exception `TypeError` with:
        a. argument name
        b. actual type
        c. expected type
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator funkcję `typecheck`
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
    >>> @typecheck
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

# Solution
from typing import NoReturn, Any, Callable


def typecheck(func: Callable):
    def valid(argname: str, argval: Any) -> NoReturn:
        argtype = type(argval)
        expected = func.__annotations__[argname]

        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')

    def merge(*args, **kwargs):
        arguments = zip(func.__annotations__.keys(), args)
        return {**kwargs, **dict(arguments)}.items()

    def wrapper(*args, **kwargs):
        # Check if all arguments are valid types
        for argname, argval in merge(*args, **kwargs):
            valid(argname, argval)

        result = func(*args, **kwargs)

        # Check result
        valid('return', result)

        # Return function result
        return result
    return wrapper
