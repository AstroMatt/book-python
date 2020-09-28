def mean(*values):
    """
    >>> mean(7.3, 2.9, 6.3, 1.8)
    4.575
    >>> row = [5.9, 3.0, 5.1, 1.8]
    >>> mean(*row)
    3.95
    >>> row = {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4},
    >>> mean(*row.values())
    3.875
    """
    return sum(values) / len(values)


FILE = r'../data/iris.csv'
result = []

with open(FILE) as file:
    *header, _ = file.readline().strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(header, measurements)
        result.append(dict(pairs))


for row in result:
    avg = mean(*row.values())
    print(avg)


## Alternative
# list(map(lambda row: mean(*row.values()), result))
