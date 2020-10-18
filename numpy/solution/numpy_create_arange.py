import numpy as np


## Results with ``%%timeit -n 1_000_000 -r 10``

result = np.arange(0, 100, step=2, dtype=float)
# 756 ns ± 10.3 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result = np.array(range(0, 100, 2), dtype=float)
# 8.28 µs ± 364 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result = np.array([x for x in range(0, 100) if x % 2 == 0], dtype=float)
# 9.76 µs ± 324 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result = np.array([float(x) for x in range(0, 100) if x % 2 == 0])
# 12.7 µs ± 195 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result = np.array([float(x) for x in range(0, 100, 2)])
# 8.35 µs ± 196 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result = np.array([x for x in range(0, 100, 2)], dtype=float)
# 5.89 µs ± 77 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

result: np.ndarray
# array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24.,
#        26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.,
#        52., 54., 56., 58., 60., 62., 64., 66., 68., 70., 72., 74., 76.,
#        78., 80., 82., 84., 86., 88., 90., 92., 94., 96., 98.])
