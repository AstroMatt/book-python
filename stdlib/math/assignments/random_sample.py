from random import sample

result = sample(range(1, 49), 6)
print(result)


# Alternative solution
from random import randint

MAX_VALUE = 49
MIN_VALUE = 1
REPETITIONS = 6

result = set()

while len(result) < REPETITIONS:
    number = randint(MIN_VALUE, MAX_VALUE)
    result.add(number)

print(sorted(result))

