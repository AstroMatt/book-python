from statistics import median_low
import pandas as pd
import numpy as np
np.random.seed(0)


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

data = np.random.randint(10, 100, size=26)
alphabet = list(ascii_lowercase)
letter_position = median_low(alphabet)
position = alphabet.index(letter_position)

s = pd.Series(data, alphabet)
result = s[position-3:position+4].sum()

print(result)
