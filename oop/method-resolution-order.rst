.. _OOP Method Resolution Order:

***********************
Method Resolution Order
***********************


Inheritance Method Resolution
=============================
.. code-block:: python

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

.. code-block:: python

    from inspect import getmro


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


    getmro(D)
    # (<class '__main__.D'>,
    #  <class '__main__.A'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class 'object'>)


Inheritance Diamond
===================
.. figure:: img/oop-mro-inheritance-diamond.png

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


    class E(B):
        def show(self):
            print('e')


    class F(C):
        def show(self):
            print('f')


    class G(E, F):
        pass


    obj = G()

    obj.show()
    # e

    print(G.__mro__)
    # (<class '__main__.G'>,
    #  <class '__main__.E'>,
    #  <class '__main__.B'>,
    #  <class '__main__.F'>,
    #  <class '__main__.C'>,
    #  <class '__main__.A'>,
    #  <class 'object'>)



Assignments
===========
.. todo:: Create assignments
