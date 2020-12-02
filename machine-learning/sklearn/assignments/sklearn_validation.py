import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


with open('../_contrib/pima-diabetes.csv') as file:
    data = np.loadtxt(file, delimiter=',')
    features = data[:, :-1]
    labels = data[:, -1]


# Normalize the features so that it does not affect the learning algorithm
normalized_X = preprocessing.normalize(features)
standardized_X = preprocessing.scale(features)

# Fit the Tree algorithm
# This class implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and use averaging to improve the predictive accuracy and control over-fitting.
model = ExtraTreesClassifier()
model.fit(features, labels)

# display the relative importance of each attribute
print(model.feature_importances_)


model = LogisticRegression()
model.fit(features, labels)
print(model)

predicted = model.predict(features)

# summarize the fit of the model
print(metrics.classification_report(labels, predicted))
