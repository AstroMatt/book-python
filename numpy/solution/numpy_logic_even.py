import numpy as np
np.random.seed(0)


a = np.random.randint(0, 100, size=9)
# array([44, 47, 64, 67, 67,  9, 83, 21, 36, 87])

b = np.logical_and(a < 50, a % 2 == 0)
# array([ True, False, False, False, False, False, False, False,  True])

b.all()
# False

b.any()
# True
