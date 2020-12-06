.. _Machine Learning Classifiers:

***********
Classifiers
***********

Co to jest Classifier?
======================
A mapping from unlabeled instances to (discrete) classes. Classifiers have a form (e.g., decision tree) plus an interpretation procedure (including how to handle unknowns, etc.). Some classifiers also provide probability estimates (scores), which can be threshold to yield a discrete class decision thereby taking into account a utility function.


Schemat działania classifier
============================
#. Collect Training Data
#. Train Classifier
#. Make Predictions

.. figure:: img/classification-spam.png

    Schemat działania classifier. Wiadomości email przechodząc przez classifier są oznaczane jako spam, lub nie spam.
