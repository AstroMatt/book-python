******************
Generowanie grafów
******************

PyDotPlus
=========
PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz’s Dot language.

* https://github.com/carlos-jenkins/pydotplus
* http://pydotplus.readthedocs.io/


Graphviz
========
Graphviz is open source graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks. It has important applications in networking, bioinformatics, software engineering, database and web design, machine learning, and in visual interfaces for other technical domains.

The Graphviz layout programs take descriptions of graphs in a simple text language, and make diagrams in useful formats, such as images and SVG for web pages; PDF or Postscript for inclusion in other documents; or display in an interactive graph browser.  Graphviz has many useful features for concrete diagrams, such as options for colors, fonts, tabular node layouts, line styles, hyperlinks, and custom shapes.

* http://www.graphviz.org/

.. code-block:: python

    import graphviz
    import pandas as pd
    from sklearn import linear_model, neighbors, svm, tree, datasets
    from sklearn.model_selection import train_test_split


    iris_ds = datasets.load_iris()
    iris = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names).assign(target=iris_ds.target)
    iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']
    iris_train, iris_test = train_test_split(iris, test_size=0.2)

    features = ['sepal_length', 'sepal_width']
    dtc = tree.DecisionTreeClassifier()
    dtc.fit(iris_train[features], iris_train['target'])

    dot_data = tree.export_graphviz(dtc,
        out_file=None,
        feature_names=features,
        class_names=iris_ds.target_names,
        filled=True,
        rounded=True,
        special_characters=True)

    graph = graphviz.Source(dot_data, )