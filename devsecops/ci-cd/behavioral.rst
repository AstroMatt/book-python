******************
Behavioral Testing
******************

``behave``
==========
* https://github.com/behave/behave

FILE: features/example.feature

    .. code-block:: text

        Feature: Showing off behave

          Scenario: Run a simple test
            Given we have behave installed
             When we implement 5 tests
             Then behave will test them for us!

FILE: features/steps/example_steps.py:

    .. code-block:: python

        from behave import given, when, then, step

        @given('we have behave installed')
        def step_impl(context):
            pass

        @when('we implement {number:d} tests')
        def step_impl(context, number):  # -- NOTE: number is converted into integer
            assert number > 1 or number == 0
            context.tests_count = number

        @then('behave will test them for us!')
        def step_impl(context):
            assert context.failed is False
            assert context.tests_count >= 0

Output:
    .. code-block:: console

        $ behave
        Feature: Showing off behave # features/example.feature:2

          Scenario: Run a simple test          # features/example.feature:4
            Given we have behave installed     # features/steps/example_steps.py:4
            When we implement 5 tests          # features/steps/example_steps.py:8
            Then behave will test them for us! # features/steps/example_steps.py:13

        1 feature passed, 0 failed, 0 skipped
        1 scenario passed, 0 failed, 0 skipped
        3 steps passed, 0 failed, 0 skipped, 0 undefined
