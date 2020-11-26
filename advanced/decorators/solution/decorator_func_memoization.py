"""
* Assignment: Decorator Function Memoization
* Filename: decorator_func_memoization.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator `@cache`
    3. Decorator must check before running function, if for given argument the computation was already done:
        a. if yes, return from `_cache`
        b. if not, calculate new result, update cache and return computed value
    4. Compare execution time using `timeit`

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Stwórz dekorator `@cache`
    3. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego argumentu wynik został już wcześniej obliczony:
        a. jeżeli tak, to zwraca dane z `_cache`
        b. jeżeli nie, to oblicza, aktualizuje `_cache`, a następnie zwraca wartość
    4. Porównaj prędkość działania za pomocą `timeit`

Tests:
    TODO: Doctests
"""

# Given
import sys
from timeit import timeit

sys.setrecursionlimit(5000)


def cache(func):
    _cache = {}
    raise NotImplementedError


@cache
def fn1(n):
    if n == 0:
        return 1
    else:
        return n * fn1(n - 1)


def fn2(n):
    if n == 0:
        return 1
    else:
        return n * fn2(n - 1)


duration_cache = timeit(stmt='fn1(500); fn1(400); fn1(450); fn1(350)',
                        globals=globals(), number=100_000)
duration_nocache = timeit(stmt='fn2(500); fn2(400); fn2(450); fn2(350)',
                          globals=globals(), number=100_000)
duration_ratio = duration_nocache / duration_cache

print(f'With Cache time: {duration_cache:.4f} seconds')
print(f'Without Cache time: {duration_nocache:.3f} seconds')
print(f'Cached solution is {duration_ratio:.1f} times faster')

# Solution
import sys
from timeit import timeit
sys.setrecursionlimit(5000)


def cache(func):
    _cache = {}
    def wrapper(n):
        if n not in _cache:
            _cache[n] = func(n)
        return _cache[n]
    return wrapper


@cache
def fn1(n):
    if n == 0:
        return 1
    else:
        return n * fn1(n-1)


def fn2(n):
    if n == 0:
        return 1
    else:
        return n * fn2(n-1)


duration_cache = timeit(stmt='fn1(500); fn1(400); fn1(450); fn1(350)', globals=globals(), number=100_000)
duration_nocache = timeit(stmt='fn2(500); fn2(400); fn2(450); fn2(350)', globals=globals(), number=100_000)
duration_ratio = duration_nocache / duration_cache

print(f'With Cache time: {duration_cache:.4f} seconds')
print(f'Without Cache time: {duration_nocache:.3f} seconds')
print(f'Cached solution is {duration_ratio:.1f} times faster')
