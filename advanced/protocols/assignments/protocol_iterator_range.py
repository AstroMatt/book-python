"""
* Assignment: Protocol Iterator Range
* Filename: protocol_iterator_range.py
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Range` with parameters: `start`, `stop`, `step`
    3. Write own implementation of a built-in `range(start, stop, step)` function
    4. Use Iterator protocol
    5. How to implement passing only stop argument (`range(start=0, stop=???, step=1)`)?
    6. All tests must pass
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Range` z parametrami: `start`, `stop`, `step`
    3. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range(start, stop, step)`
    4. Użyj protokołu Iterator
    5. Jak zaimplementować możliwość podawania tylko końca (`range(start=0, stop=???, step=1)`)?
    6. Wszystkie testy muszą przejść
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
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
    ValueError: Invalid arguments

    >>> list(Range(1,2,3,4))
    Traceback (most recent call last):
    ValueError: Invalid arguments

    >>> Range(stop=2)
    Traceback (most recent call last):
    TypeError: Range() takes no keyword arguments

    >>> Range(start=1, stop=2)
    Traceback (most recent call last):
    TypeError: Range() takes no keyword arguments

    >>> Range(start=1, stop=2, step=2)
    Traceback (most recent call last):
    TypeError: Range() takes no keyword arguments
"""


# Solution
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
