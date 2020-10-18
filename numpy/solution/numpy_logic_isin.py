import numpy as np
np.random.seed(0)


a = np.random.randint(0, 100, size=50)

# %%timeit -r 10 -n 1_000_000
b = 2 ** np.arange(7)
# 1.73 µs ± 36.4 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)


# Alternative solution
# %%timeit -r 10 -n 1_000_000
b = np.array([np.power(2, x) for x in range(0, 7)])
# 10 µs ± 122 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

print(np.isin(a, b))
# [False False  True False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False  True False False False False
#  False False False False False  True False False False  True False False
#  False False]

print(np.isin(b, a))
# [False False False False False  True  True]

a[ np.isin(a, b) ]
# array([64, 64, 32, 32])

b[ np.isin(b, a) ]
# array([32, 64])
