"""
>>> from inspect import isclass, ismethod
>>> assert isclass(Range)

>>> r = Range(0, 0, 0)
>>> assert hasattr(r, '__iter__')
>>> assert hasattr(r, '__next__')
>>> assert ismethod(r.__iter__)
>>> assert ismethod(r.__next__)

>>> list(Range(0, 10, 2))
[0, 2, 4, 6, 8]

>>> list(Range(0, 5))
[0, 1, 2, 3, 4]

>>> list(Range(5))
[0, 1, 2, 3, 4]

>>> list(Range())
Traceback (most recent call last):
  ...
ValueError: Invalid arguments

>>> list(Range(1,2,3,4))
Traceback (most recent call last):
  ...
ValueError: Invalid arguments

>>> Range(stop=2)
Traceback (most recent call last):
  ...
TypeError: Range() takes no keyword arguments

>>> Range(start=1, stop=2)
Traceback (most recent call last):
  ...
TypeError: Range() takes no keyword arguments

>>> Range(start=1, stop=2, step=2)
Traceback (most recent call last):
  ...
TypeError: Range() takes no keyword arguments
"""


class Range:
    def __init__(self, *args, **kwargs):
        if kwargs:
            raise TypeError('Range() takes no keyword arguments')
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        else:
            raise ValueError('Invalid arguments')

    def __iter__(self):
        self._iter_index = self.start
        return self

    def __next__(self):
        if self._iter_index >= self.stop:
            raise StopIteration

        result = self._iter_index
        self._iter_index += self.step
        return result
