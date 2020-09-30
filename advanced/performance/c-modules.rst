*********
C Modules
*********


Code
====
.. code-block:: C
    :name: listing-c-modules
    :caption: Przykład kodu w C wykorzystującego *C modules*

    #include <Python.h>

    /* Implementation */

    static PyObject* say_hello(PyObject* self, PyObject* args) {
        const char* name;

        if (!PyArg_ParseTuple(args, "s", &name))
            return NULL;

        printf("Hello %s!\n", name);
        Py_RETURN_NONE;
    }

    static PyObject* version(PyObject* self) {
        return Py_BuildValue("s", "Version 1.0");
    }


    /* Python Binding Definitions */

    static PyMethodDef HelloMethods[] = {
         {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
         {"version", (PyCFunction)version, METH_NOARGS, "returns the version"},
         {NULL, NULL, 0, NULL}
    };

    static struct PyModuleDef hello = {
        PyModuleDef_HEAD_INIT,
        "hello",			/* name of module */
        "",					/* module documentation, may be NULL */
        -1,					/* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        HelloMethods
    };

    PyMODINIT_FUNC PyInit_hello(void) {
        return PyModule_Create(&hello);
    }

Compile
=======

``setup.py``
------------
.. code-block:: python

    import sys
    from distutils.core import setup, Extension

    print('Building for Python 3')
    module = Extension('hello', sources = ['mylib-cmodules.c'])

    setup(
        name = 'hello',
        version='1.0',
        description = 'Ehlo World!',
        ext_modules = [module])

Execute
-------
.. code-block:: console

    $ python setup.py build
    $ cd build/lib*
    $ python

Run
===
.. code-block:: python

    import hello

    hello.say_hello('José Jiménez')
    # José Jiménez


Assignments
===========

C Modules
---------
* Assignment name: C Modules
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/cmodules_datetime.py`
* Last update: 2020-10-01

:English:
    .. todo:: English Translation

:Polish:
    #. Wykorzystując C Modules wypisz datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``
