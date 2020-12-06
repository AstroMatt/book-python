.. _Machine Learning Logistic Regression:

*******************
Logistic Regression
*******************

.. todo:: Zrobić aby wykorzystywało szablon ``_template.rst``

Co to jest Logistic Regression?
===============================
In general when we make a machine learning based program, we are trying to come up with a function that can predict for future inputs based on the experience it has gained through the past inputs and their outputs (training set).

Logistic Regression is - coming up with a probability function that can give us 'the chance, for an input to belong to any one of the various classes' we have (classification).

Since the logistic function has two different asymptotes, it can be used to divide data into "yes/no" categories -- the low side being "no" and the high side being "yes."

* :math:`transformed = 1 / (1 + e^-x)`

.. figure:: img/logistic-regression-curve.png

    The standard logistic function :math:`\sigma (t)`; note that :math:`\sigma (t) \in (0,1)` for all :math:`t`.


Linear vs Logistics
===================
.. figure:: img/regression-linear-vs-logistic.png

    Linear vs Logistics

Podstawowe pojęcia
==================
.. glossary::
    Binary Model
        Model który ma dwa typy wartości (przykład: spam, nie spam)

    logit
        logistic function

    logistic-sigmoid function
        Funkcja sigmoidalna

    Softmax function
        takes logits and transforms them to probability distributions

.. todo::
    Bias term

    Cost function

    Entropy

    Cross Entropy

Przykład zastosowania
=====================
* whether an email is SPAM(y=1) OR NOT(y=0)

* whether a person will vote or not in upcoming elections

* classifying a set of words as nouns, pronouns, adjectives etc.

* application in Information extraction

* in speech recognition systems

* Life insurance actuaries use logistic regression to predict, based on given data on a policy holder (e.g. age, gender, results from a physical examination) the chances that the policy holder will die before the term of the policy expires.

* Political campaigns try to predict the chances that a voter will vote for their candidate (or do something else desirable, such as donate to the campaign).

* Bankers use it to predict the chances that a loan applicant will default on the loan.

* Marketers use it to predict whether a customer will respond to a particular ad (whether by clicking on a link or sending back a self-enclosed mailer).

* Weather forecasters use it to predict the "chance of rain" you see every morning.


Assignments
===========

