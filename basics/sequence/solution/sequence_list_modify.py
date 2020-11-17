"""
>>> assert type(a) is list
>>> assert type(b) is list
>>> assert type(c) is list
>>> a
['versicolor', 4.7, 3.2, 1.3, 0.2]
>>> b
[7.0, 3.2, 4.7, 1.4, 'setosa']
>>> c
[7.6, 3.0, 6.6, 2.1]
"""

a = [4.7, 3.2, 1.3, 0.2, 'setosa']
b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
c = [7.6, 3.0, 6.6, 2.1, 'virginica']

a.insert(0, b.pop())
b.append(a.pop())
del c[4]
