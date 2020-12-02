import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


with open("../_contrib/pima-diabetes.csv") as file:
    data = np.loadtxt(file, delimiter=',')
    features = data[:, :-1]
    labels = data[:, -1]


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25, random_state=0)


names = [
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Gaussian Process",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
    "QDA"
]

classifiers = [
    {'name': "Nearest Neighbors", 'model': KNeighborsClassifier()},
    {'name': "Linear SVM",        'model': SVC(kernel="linear")},
    {'name': "RBF SVM",           'model': SVC(kernel="rbf")},
    {'name': "Gaussian Process",  'model': GaussianProcessClassifier()},
    {'name': "Decision Tree",     'model': DecisionTreeClassifier()},
    {'name': "Random Forest",     'model': RandomForestClassifier()},
    {'name': "Neural Net",        'model': MLPClassifier()},
    {'name': "AdaBoost",          'model': AdaBoostClassifier()},
    {'name': "Naive Bayes",       'model': GaussianNB()},
    {'name': "QDA",               'model': QuadraticDiscriminantAnalysis()},
]


for classifier in classifiers:
    model = classifier['model']
    name = classifier['name']

    scores = cross_val_score(model, features_train, labels_train, cv=5)

    accuracy = 100 * scores.mean()
    stdev = 100 * scores.std()

    print(f'{name:>20} | Accuracy: {accuracy:.2f}% (+/- {stdev:.2f}%)')

"""
             RBF SVM | Accuracy: 64.24% (+/- 0.44%)
          Linear SVM | Accuracy: 76.04% (+/- 5.58%)
          Neural Net | Accuracy: 60.06% (+/- 23.16%)
       Decision Tree | Accuracy: 66.85% (+/- 4.62%)
    Gaussian Process | Accuracy: 68.58% (+/- 6.14%)
   Nearest Neighbors | Accuracy: 71.18% (+/- 7.56%)
                 QDA | Accuracy: 73.97% (+/- 8.84%)
            AdaBoost | Accuracy: 72.57% (+/- 8.32%)
         Naive Bayes | Accuracy: 73.62% (+/- 5.78%)
       Random Forest | Accuracy: 73.44% (+/- 3.69%)
"""
