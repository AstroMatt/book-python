"""
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
...
TypeError: "a" is <class 'int'>, but <class 'str'> was expected

>>> echo('one', 'two')
Traceback (most recent call last):
...
TypeError: "b" is <class 'str'>, but <class 'int'> was expected

>>> echo('one', 1, 'two')
Traceback (most recent call last):
...
TypeError: "c" is <class 'str'>, but <class 'float'> was expected

>>> echo(b='one', a='two')
Traceback (most recent call last):
...
TypeError: "b" is <class 'str'>, but <class 'int'> was expected

>>> echo('one', c=1.1, b=1.1)
Traceback (most recent call last):
...
TypeError: "b" is <class 'float'>, but <class 'int'> was expected
"""

from typing import NoReturn, Any, Callable


def typecheck(check_return: bool = True):
    def decorator(func: Callable):
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
            if check_return:
                valid('return', result)

            # Return function result
            return result
        return wrapper
    return decorator


@typecheck(check_return=True)
def echo(a: str, b: int, c: float = 0.0) -> bool:
    return bool(a * b)
