.. _Machine Learning scikit-learn:

************
scikit-learn
************


Loading Sample Datasets
=======================
.. literalinclude:: src/ml-sklearn-datasets.py
    :language: python
    :caption: Loading Sample Datasets


Fit and Predict
===============
.. literalinclude:: src/ml-sklearn-fit-predict.py
    :language: python
    :caption: Fit and Predict


Classifier
==========
.. literalinclude:: src/ml-sklearn-classifier.py
    :language: python
    :caption: Classifier


Feature Selection
=================
* http://scikit-learn.org/stable/modules/feature_selection.html
* :math:`\mathrm{Var}[X] = p(1 - p)`

.. code-block:: python

    from sklearn.feature_selection import VarianceThreshold

    features = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]

    # Remove all features below 80% change variance in the samples
    sel = VarianceThreshold(threshold=(0.8 * (1 - 0.8)))

    sel.fit_transform(features)
    # array([[0, 1],
    #        [1, 0],
    #        [0, 0],
    #        [1, 1],
    #        [1, 0],
    #        [1, 1]])

.. code-block:: python

    from sklearn.datasets import load_iris
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2

    iris = load_iris()
    features = iris.data
    labels = iris.target

    features.shape
    # (150, 4)

    best_features = SelectKBest(chi2, k=2).fit_transform(features, labels)
    # array([[1.4, 0.2],
    #        [1.4, 0.2],
    #        ...
    #        [5.4, 2.3],
    #        [5.1, 1.8]])

    best_features.shape
    # (150, 2)


Evaluation
==========

Score
-----
.. literalinclude:: src/ml-sklearn-score.py
    :language: python
    :caption: Score

Cross Validation
----------------
.. literalinclude:: src/ml-sklearn-cross-validation.py
    :language: python
    :caption: Cross Validation


Label Encoder
=============
.. literalinclude:: src/ml-sklearn-label-encoder.py
    :language: python
    :caption: Label Encoder


Writing Own Classifier
======================

Random Classifier
-----------------

.. code-block:: python

    import random


    class RandomNeighborClassifer:
        def fit(self, features, labels):
            self.features_train = features
            self.labels_train = labels

        def predict(self, features_test):
            predictions = []

            for row in features_test:
                label = random.choice(self.labels_train)
                predictions.append(label)

            return predictions

Accuracy for Iris dataset: 0.346666666667


Zadania praktyczne
==================

Nearest Neighbor Classifier
---------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/sklearn_classifier.py`

#. Napisz klasyfikator najbliższego sąsiada
#. Podziel dane treningowe i testowe pół-na-pół
#. Dla zbioru Iris ma osiągać accuracy na poziomie powyżej 90%
#. Klasa ``NearestNeighborClassifier`` powinna mieć interfejs zgodny z ``scikit-learn``:

    * ``.fit()`` - do uczenia funkcji
    * ``.predict()`` - do predykcji

#. Do porównania użyj ``accuracy = metrics.accuracy_score(labels_test, labels_predicted)``

:Hints:
    * Dla każdego feature sprawdzasz jaka jest najmniejsza odległość
    * Wybierasz najmniejszą odległość ze wszystkich
    * Do obliczania odległości skorzystaj z algorytmu Euclidesa.
    * ``from scipy.spatial.distance import euclidean as euclidean_distance``

    * .. code-block:: python

        from sklearn import metrics
        from scipy.spatial.distance import euclidean as euclidean_distance
        from sklearn.model_selection import train_test_split
        from sklearn import datasets


        class NearestNeighborClassifier:
            def fit(self, features, labels):
                raise NotImplementedError

            def predict(self, features_test):
                raise NotImplementedError

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

Porównanie classifierów
-----------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/sklearn_comparision.py`

* Pobierz dane Brest Cancer Dataset (``datasets.load_breast_cancer()``)
* Podziel zestaw na dane testowe (15%) i dane treningowe (85%) i ustaw ``random_state=0``
* Dla danych przeprowadź analizę wykorzystując różne modele danych
* Wyświetl nazwę, dokładność oraz odchylenie standardowe modelu

.. code-block:: text

   Nearest Neighbors | Accuracy: 71.18% (+/- 3.78%)
          Linear SVM | Accuracy: 76.04% (+/- 2.79%)
             RBF SVM | Accuracy: 64.24% (+/- 0.22%)
    Gaussian Process | Accuracy: 68.58% (+/- 3.07%)
       Decision Tree | Accuracy: 68.24% (+/- 4.53%)
       Random Forest | Accuracy: 73.96% (+/- 3.28%)
          Neural Net | Accuracy: 65.28% (+/- 2.75%)
            AdaBoost | Accuracy: 72.57% (+/- 4.16%)
         Naive Bayes | Accuracy: 73.62% (+/- 2.89%)
                 QDA | Accuracy: 73.97% (+/- 4.42%)

:Hints:
    .. code-block:: python

        classifiers = [
            {'name': "Nearest Neighbors", 'model': KNeighborsClassifier()},
            {'name': "Linear SVM",        'model': SVC(kernel="linear")},
            {'name': "RBF SVM",           'model': SVC(kernel="rbf")},
            {'name': "Gaussian Process",  'model': GaussianProcessClassifier()},
            {'name': "Decision Tree",     'model': DecisionTreeClassifier()},
            {'name': "Random Forest",     'model': RandomForestClassifier()},
            {'name': "Neural Net",        'model': MLPClassifier(max_iter=1500)},
            {'name': "AdaBoost",          'model': AdaBoostClassifier()},
            {'name': "Naive Bayes",       'model': GaussianNB()},
            {'name': "QDA",               'model': QuadraticDiscriminantAnalysis()},
        ]

:Extra task:
    * Zrównoleglij uruchamianie predykcji za pomocą modułu ``threading`` oraz architektury opartej na Workerach.
    * Wyświetl posortowaną malejąco listę wg. dokładności
