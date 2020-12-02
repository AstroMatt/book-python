def even_numbers(x):
    return x % 2 == 0


NUMBERS = [1, 2, 3, 4]


even1 = filter(even_numbers, NUMBERS)
print(list(even1))
# [2, 4]

even2 = filter(lambda x: x % 2 == 0, NUMBERS)
print(list(even2))
# [2, 4]
