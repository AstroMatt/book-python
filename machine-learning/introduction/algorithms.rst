.. _Machine Learning Algorithms:

***************************
Machine Learning Algorithms
***************************

.. figure:: img/algorithms-cheat-sheet.png
    :width: 75%
    :align: center

    Machine Learning Algorithms Cheat Sheet

.. figure:: img/algorithms-classes.png
    :width: 75%
    :align: center

    Machine Learning Algorithms Classes and Classification

Algorithms are often grouped by similarity in terms of their function (how they work). For example, tree-based methods, and neural network inspired methods.

I think this is the most useful way to group algorithms and it is the approach we will use here.

This is a useful grouping method, but it is not perfect. There are still algorithms that could just as easily fit into multiple categories like Learning Vector Quantization that is both a neural network inspired method and an instance-based method. There are also categories that have the same name that describe the problem and the class of algorithm such as Regression and Clustering.

We could handle these cases by listing algorithms twice or by selecting the group that subjectively is the “best” fit. I like this latter approach of not duplicating algorithms to keep things simple.

In this section, I list many of the popular machine learning algorithms grouped the way I think is the most intuitive. The list is not exhaustive in either the groups or the algorithms, but I think it is representative and will be useful to you to get an idea of the lay of the land.

Please Note: There is a strong bias towards algorithms used for classification and regression, the two most prevalent supervised machine learning problems you will encounter.

If you know of an algorithm or a group of algorithms not listed, put it in the comments and share it with us. Let’s dive in.

Regression Algorithms
=====================
Regression is concerned with modeling the relationship between variables that is iteratively refined using a measure of error in the predictions made by the model.

Regression methods are a workhorse of statistics and have been co-opted into statistical machine learning. This may be confusing because we can use regression to refer to the class of problem and the class of algorithm. Really, regression is a process.

.. figure:: img/algorithms-regression.png
    :width: 75%
    :align: center

    Regression Algorithms

The most popular regression algorithms are:

    * Ordinary Least Squares Regression (OLSR)
    * Linear Regression
    * Logistic Regression
    * Stepwise Regression
    * Multivariate Adaptive Regression Splines (MARS)
    * Locally Estimated Scatterplot Smoothing (LOESS)

Instance-based Algorithms
=========================
Instance-based AlgorithmsInstance-based learning model is a decision problem with instances or examples of training data that are deemed important or required to the model.

Such methods typically build up a database of example data and compare new data to the database using a similarity measure in order to find the best match and make a prediction. For this reason, instance-based methods are also called winner-take-all methods and memory-based learning. Focus is put on the representation of the stored instances and similarity measures used between instances.

.. figure:: img/algorithms-instance-based.png
    :width: 75%
    :align: center

    Instance-based Algorithms

The most popular instance-based algorithms are:

    * k-Nearest Neighbor (kNN)
    * Learning Vector Quantization (LVQ)
    * Self-Organizing Map (SOM)
    * Locally Weighted Learning (LWL)
    * Regularization Algorithms

Regularization Algorithms
=========================
An extension made to another method (typically regression methods) that penalizes models based on their complexity, favoring simpler models that are also better at generalizing.

I have listed regularization algorithms separately here because they are popular, powerful and generally simple modifications made to other methods.

.. figure:: img/algorithms-regularization.png
    :width: 75%
    :align: center

    Regularization Algorithms

The most popular regularization algorithms are:

* Ridge Regression
* Least Absolute Shrinkage and Selection Operator (LASSO)
* Elastic Net
* Least-Angle Regression (LARS)
* Decision Tree Algorithms

Decision Tree Algorithms
========================
Decision tree methods construct a model of decisions made based on actual values of attributes in the data.

Decisions fork in tree structures until a prediction decision is made for a given record. Decision trees are trained on data for classification and regression problems. Decision trees are often fast and accurate and a big favorite in machine learning.

.. figure:: img/algorithms-decision-tree.png
    :width: 75%
    :align: center

    Decision Tree Algorithms

The most popular decision tree algorithms are:

    * Classification and Regression Tree (CART)
    * Iterative Dichotomiser 3 (ID3)
    * C4.5 and C5.0 (different versions of a powerful approach)
    * Chi-squared Automatic Interaction Detection (CHAID)
    * Decision Stump
    * M5
    * Conditional Decision Trees
    * Bayesian Algorithms

Bayesian Algorithms
===================
Bayesian methods are those that explicitly apply Bayes' Theorem for problems such as classification and regression.

.. figure:: img/algorithms-bayesian.png
    :width: 75%
    :align: center

    Bayesian Algorithms

The most popular Bayesian algorithms are:

    * Naive Bayes
    * Gaussian Naive Bayes
    * Multinomial Naive Bayes
    * Averaged One-Dependence Estimators (AODE)
    * Bayesian Belief Network (BBN)
    * Bayesian Network (BN)
    * Clustering Algorithms

Clustering Algorithms
=====================
Clustering, like regression, describes the class of problem and the class of methods.

Clustering methods are typically organized by the modeling approaches such as centroid-based and hierarchical. All methods are concerned with using the inherent structures in the data to best organize the data into groups of maximum commonality.

.. figure:: img/algorithms-clustering.png
    :width: 75%
    :align: center

    Clustering Algorithms

The most popular clustering algorithms are:

    * k-Means
    * k-Medians
    * Expectation Maximisation (EM)
    * Hierarchical Clustering
    * Association Rule Learning Algorithms

Association Rule Learning Algorithms
====================================
Association rule learning methods extract rules that best explain observed relationships between variables in data.

These rules can discover important and commercially useful associations in large multidimensional datasets that can be exploited by an organization.

.. figure:: img/algorithms-assoication-rule-learning.png
    :width: 75%
    :align: center

    Association Rule Learning Algorithms

The most popular association rule learning algorithms are:

    * Apriori algorithm
    * Eclat algorithm
    * Artificial Neural Network Algorithms

Artificial Neural Network Algorithms
====================================
Artificial Neural Networks are models that are inspired by the structure and/or function of biological neural networks.

They are a class of pattern matching that are commonly used for regression and classification problems but are really an enormous subfield comprised of hundreds of algorithms and variations for all manner of problem types.

Note that I have separated out Deep Learning from neural networks because of the massive growth and popularity in the field. Here we are concerned with the more classical methods.

.. figure:: img/algorithms-artificial-neural-network.png
    :width: 75%
    :align: center

    Artificial Neural Network Algorithms

The most popular artificial neural network algorithms are:

    * Perceptron
    * Back-Propagation
    * Hopfield Network
    * Radial Basis Function Network (RBFN)
    * Deep Learning Algorithms

Deep Learning Algorithms
========================
Deep Learning methods are a modern update to Artificial Neural Networks that exploit abundant cheap computation.

They are concerned with building much larger and more complex neural networks and, as commented on above, many methods are concerned with semi-supervised learning problems where large datasets contain very little labeled data.

.. figure:: img/algorithms-deep-learning.png
    :width: 75%
    :align: center

    Deep Learning Algorithms

The most popular deep learning algorithms are:

    * Deep Boltzmann Machine (DBM)
    * Deep Belief Networks (DBN)
    * Convolutional Neural Network (CNN)
    * Stacked Auto-Encoders
    * Dimensionality Reduction Algorithms

Dimensional Reduction Algorithms
================================
Like clustering methods, dimensionality reduction seek and exploit the inherent structure in the data, but in this case in an unsupervised manner or order to summarize or describe data using less information.

.. figure:: img/algorithms-dimensional-reduction.png
    :width: 75%
    :align: center

    Dimensional Reduction Algorithms

This can be useful to visualize dimensional data or to simplify data which can then be used in a supervised learning method. Many of these methods can be adapted for use in classification and regression.

    * Principal Component Analysis (PCA)
    * Principal Component Regression (PCR)
    * Partial Least Squares Regression (PLSR)
    * Sammon Mapping
    * Multidimensional Scaling (MDS)
    * Projection Pursuit
    * Linear Discriminant Analysis (LDA)
    * Mixture Discriminant Analysis (MDA)
    * Quadratic Discriminant Analysis (QDA)
    * Flexible Discriminant Analysis (FDA)
    * Ensemble Algorithms

Ensemble Algorithms
===================
Ensemble methods are models composed of multiple weaker models that are independently trained and whose predictions are combined in some way to make the overall prediction.

.. figure:: img/algorithms-ensemble.png
    :width: 75%
    :align: center

    Ensemble Algorithms

Much effort is put into what types of weak learners to combine and the ways in which to combine them. This is a very powerful class of techniques and as such is very popular.

* Boosting
* Bootstrapped Aggregation (Bagging)
* AdaBoost
* Stacked Generalization (blending)
* Gradient Boosting Machines (GBM)
* Gradient Boosted Regression Trees (GBRT)
* Random Forest

Other Algorithms
================
Many algorithms were not covered.

For example, what group would Support Vector Machines go into? Its own?

I did not cover algorithms from specialty tasks in the process of machine learning, such as:

* Feature selection algorithms
* Algorithm accuracy evaluation
* Performance measures

I also did not cover algorithms from specialty subfields of machine learning, such as:

* Computational intelligence (evolutionary algorithms, etc.)
* Computer Vision (CV)
* Natural Language Processing (NLP)
* Recommender Systems
* Reinforcement Learning
* Graphical Models
* And more...


.. note:: Source: http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/
