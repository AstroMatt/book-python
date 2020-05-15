class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_numeric_values(self):
        return [
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width]

    def total(self):
        return sum(self.get_numeric_values())

    def length(self):
        return len(self.get_numeric_values())

    def mean(self):
        return self.total() / self.length()


setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
print(f'total={setosa.total():.2f} mean={setosa.mean():.2f} {setosa.species}')

virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
print(f'total={virginica.total():.2f} mean={virginica.mean():.2f} {virginica.species}')
