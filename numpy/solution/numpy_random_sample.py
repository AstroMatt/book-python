import numpy as np
np.random.seed(0)


np.random.choice(np.arange(1, 50), size=6, replace=False)


## Alternative Solution
np.random.choice(np.random.randint(49), size=6, replace=False)


## Alternative Solution
a = np.random.randint(1, 49, size=100)
np.random.choice(np.unique(a), size=6, replace=False)


## Alternative Solution
np.random.choice(range(1, 50), size=6, replace=False)


## Alternative Solution
lotto = set()
while len(lotto) < 6:
    lotto.add(np.random.randint(1, 49))
print(lotto)


## Alternative Solution - not working!! (sometimes 0, sometimes repetition)
np.random.choice(np.random.randint(1,49), size=6, replace=False)



