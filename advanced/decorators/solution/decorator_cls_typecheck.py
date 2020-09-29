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

from typing import Callable, Any, NoReturn


class TypeCheck:
    def __init__(self, func: Callable) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_arguments(*args, **kwargs)
        result = self._func(*args, **kwargs)
        self.check_result(result)
        return result

    def check_arguments(self, *args, **kwargs):
        for argname, argval in self.merge(*args, **kwargs):
            self.valid(argname, argval)

    def check_result(self, result):
        self.valid('return', result)

    def merge(self, *args, **kwargs):
        """Convert args to named arguments and merge with kwargs"""
        arguments = zip(self._func.__annotations__.keys(), args)
        return {**kwargs, **dict(arguments)}.items()

    def valid(self, argname: str, argval: Any) -> NoReturn:
        argtype = type(argval)
        expected = self._func.__annotations__[argname]

        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')


@TypeCheck
def echo(a: str, b: int, c: float = 0.0) -> bool:
    return bool(a * b)
