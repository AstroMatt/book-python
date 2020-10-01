"""
>>> from inspect import isclass
>>> assert isclass(Venus)
>>> assert isclass(Woman)
>>> assert isclass(Mars)
>>> assert isclass(Man)
>>> assert issubclass(Woman, Venus)
>>> assert issubclass(Man, Mars)
"""


class Venus:
    pass


class Woman(Venus):
    pass


class Mars:
    pass


class Man(Mars):
    pass
