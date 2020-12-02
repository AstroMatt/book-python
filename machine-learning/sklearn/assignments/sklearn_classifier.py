from sklearn import metrics
from scipy.spatial.distance import euclidean as euclidean_distance
from sklearn.model_selection import train_test_split
from sklearn import datasets


class NearestNeighborClassifier:
    def fit(self, features, labels):
        self.features_train = features
        self.labels_train = labels

    def predict(self, features_test):
        predictions = []

        for row in features_test:
            label = self._closest(row)
            predictions.append(label)

        return predictions

    def _closest(self, row):
        current_best_dist = euclidean_distance(row, self.features_train[0])
        best_index = 0

        for i in range(0, len(self.features_train)):
            dist = euclidean_distance(row, self.features_train[i])
            if dist < current_best_dist:
                current_best_dist = dist
                best_index = i

        return self.labels_train[best_index]


dataset = datasets.load_iris()
features = dataset.data
labels = dataset.target

data = train_test_split(features, labels, test_size=0.25, random_state=0)

features_train = data[0]
features_test = data[1]
labels_train = data[2]
labels_test = data[3]

model = NearestNeighborClassifier()
model.fit(features_train, labels_train)
predictions = model.predict(features_test)
accuracy = metrics.accuracy_score(labels_test, predictions)

print(accuracy)
