***********************
Method Resolution Order
***********************


Inheritance Method Resolution
=============================
.. code-block:: python
    :caption: Method Resolution Order

    class A:
        def show(self):
            print('a')

    class B:
        def show(self):
            print('b')

    class C:
        def show(self):
            print('c')

    class D(A, B, C):
        pass


    obj = D()

    obj.show()
    # a

    print(D.__mro__)
    # (<class '__main__.D'>,
    #  <class '__main__.A'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class 'object'>)


Inheritance Diamond
===================
.. figure:: img/inheritance-diamond.jpg
    :width: 75%
    :align: center

    Inheritance Diamond

.. code-block:: python
    :caption: Inheritance Diamond

    class A:
        def show(self):
            print('a')


    class B(A):
        def show(self):
            print('b')


    class C(A):
        def show(self):
            print('c')


    class D(B, C):
        pass


    obj = D()

    obj.show()
    # b

    print(D.__mro__)
    # (<class '__main__.D'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class '__main__.A'>,
    #  <class 'object'>)


Assignments
===========
.. todo:: Create assignments
