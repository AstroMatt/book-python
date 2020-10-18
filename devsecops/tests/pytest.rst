******
Pytest
******


Rationale
=========
* Detailed info on failing assert statements (no need to remember self.assert* names);
* Auto-discovery of test modules and functions;
* Modular fixtures for managing small or parametrized long-lived test resources;
* Can run unittest (including trial) and nose test suites out of the box;
* Python 3.5+ and PyPy 3;
* Rich plugin architecture, with over 315+ external plugins and thriving community;

.. code-block:: python

    def my_func(number):
        return number + 1

    def test():
        assert my_func(3) == 4

Running
=======
.. code-block:: python

    python -m pytest my_file.py
    python -m pytest -v my_file.py
    python -m pytest -v -s my_file.py

Skip
====
.. code-block:: python

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_the_unknown():
        ...

.. code-block:: python

    def test_function():
        if not valid_config():
            pytest.skip("unsupported configuration")

.. code-block:: python

    import sys
    import pytest

    if not sys.platform.startswith("win"):
        pytest.skip("skipping windows-only tests", allow_module_level=True)

Skipif
------
.. code-block:: python

    import sys


    @pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
    def test_function():
        ...

* Skip all test functions of a class or module

.. code-block:: python

    @pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
    class TestPosixCalls:
        def test_function(self):
            "will not be setup or run under 'win32' platform"

``pytest.raises``
=================
.. code-block:: python

    with raises(ZeroDivisionError):
        1/0

    with raises(ValueError, match='must be 0 or None'):
        raise ValueError("value must be 0 or None")

    with raises(ValueError, match=r'must be \d+$'):
        raise ValueError("value must be 42")

Fixtures
========
* Fixtures are requested by test functions or other fixtures by declaring them as argument names.
* It’s to think of fixtures as a set of resources that need to be set up before a test starts, and cleaned up after.
* ``@pytest.fixture(scope='module')``

.. code-block:: python

    import pytest

    @pytest.fixture()
    def setUp():
        print('\nsetup')

    def test_1_that_needs_setup(setUp):
        print('test_1_that_needs_setup()')

    def test_2_that_does_not():
        print('\ntest_2_that_does_not()')

    def test_3_that_does(setUp):
        print('test_3_that_does()')

.. code-block:: console

    $ python -m pytest -v -s tmp7.py
    # ====================================== test session starts ======================================
    # platform darwin -- Python 3.7.4, pytest-5.1.2, py-1.8.0, pluggy-0.13.0 -- /Users/Developer/.venv-3.7.3/bin/python
    # cachedir: .pytest_cache
    # rootdir: /Users/Developer/book-python
    # collected 3 items
    #
    # tmp7.py::test_1_that_needs_setup
    # setup
    # test_1_that_needs_setup()
    # PASSED
    # tmp7.py::test_2_that_does_not
    # test_2_that_does_not()
    # PASSED
    # tmp7.py::test_3_that_does
    # setup
    # test_3_that_does()
    # PASSED
    #
    # ======================================= 3 passed in 0.01s =======================================

