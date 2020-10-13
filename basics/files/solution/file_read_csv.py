FILE = r'/tmp/_temporary.csv'
features = []
label = []


with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *X,y = line.strip().split(',')
        X = [float(x) for x in X]
        # X = map(float, X)

        features.append(tuple(X))
        label.append(y)


print(header)
print(features)
print(label)
