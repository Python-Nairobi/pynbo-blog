---
Title: Python parametrized unit testing with Pytest
Date: 2017-08-01 13:00
Tags: python, pytest
Category: unit testing
Slug: test parameterization
Author: Paul Upendo
Summary: Create pythonic parametrized tests with pytest
about_author: Upendo is a Software Developer at Andela Kenya
email: lovepaul46@outlook.com
---

## Pre-requisites
 > - Beginner level Python
 > - Python2* or Python3* installed
 > - Basic knowledge on TDD and python UnitTesting
 > - Pytest installed

# Intro
I really did not get a hang of TDD the first time I heard about it. I saw it as an acronym that was maybe too difficult to fathom. A few months down the line I have a clear and better perspective towards it, and even better a more pythonic way to use TDD in my software development. Hang on as we methodically dive into it.

TDD (Test Driven Development) is a software design methodology. This generally means writing UnitTests for your code even before you write it yourself. TDD, now that you are farmiliar with the acronym, is not limited to a particular language stack but for this instance we will stick to python as our language of choice. 

# Parametrizing your tests with Pytest
There are a couple of UnitTesting frameworks in python:
- Python Unittest (that comes with the standard python library distribution)
- Python Pytest 
- Python-nose

Python UnitTest framework is a member of the XUnit family of testing tools that use a similar pattern for defining testCases. With UnitTest following XUnit Conventions, it makes Pytest and Python-nose a more - Pythonic way to write tests that follow Pep8 style guide. I will focus on paramet`rization of tests using Pytest. 

#### Why parametrize my tests?
Let's think of a scenario where we have to write tests for a particular function but with multiple input values/arguments. Rewriting my assertion statements with the different arguments works quite well but what if we could simplify this to only one assertion statement for that function? Then run the test multiple times with an array of parameters? Smart right? Python's Pytest provides an excellent Pythonic way to achieve this.

`@pytest.mark.parametrize` allows one to define multiple sets of arguments and fixtures at the test function or class.

Let us write parametrized tests for a function that accepts integer input from the user and determines whether the input is odd or even.
```python
# File test_parametrization.py
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (3, "odd"),
    (4, "even"),
    (9, "even"),
])

def test_even_and_odd_numbers(test_input, expected):
    assert (runOddEvenCheck(test_input)) == expected

```
To run this, use the command `pytest`, which executes the pytest test runner for us. The result for this would be a series of failing tests as we can see below. The beautiful thing about this is that by implementing test parameterization, Pytest created 3 individual tests for us from our test function :smile: .
```python
# Commandline output
(pytest_blog) ~/D/t/p/parameterized_testing ❯❯❯ pytest                                                                                                                                                                                                                       ⏎ develop ✱ ◼
=================================================================================================================================== test session starts ===================================================================================================================================
platform darwin -- Python 3.6.1, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/Upendo/Documents/tech_blogs/pytest_blog/parameterized_testing, inifile:
collected 3 items

test_parametrization.py FFF

======================================================================================================================================== FAILURES =========================================================================================================================================
____________________________________________________________________________________________________________________________ test_even_and_odd_numbers[3-odd] _____________________________________________________________________________________________________________________________

test_input = 3, expected = 'odd'

    @pytest.mark.parametrize("test_input,expected", [
        (3, "odd"),
        (4, "even"),
        (9, "even"),
    ])

    def test_even_and_odd_numbers(test_input, expected):
>       assert (runOddEvenCheck(test_input)) == expected
E       NameError: name 'runOddEvenCheck' is not defined

test_parametrization.py:11: NameError
____________________________________________________________________________________________________________________________ test_even_and_odd_numbers[4-even] ____________________________________________________________________________________________________________________________

test_input = 4, expected = 'even'

    @pytest.mark.parametrize("test_input,expected", [
        (3, "odd"),
        (4, "even"),
        (9, "even"),
    ])

    def test_even_and_odd_numbers(test_input, expected):
>       assert (runOddEvenCheck(test_input)) == expected
E       NameError: name 'runOddEvenCheck' is not defined

test_parametrization.py:11: NameError
____________________________________________________________________________________________________________________________ test_even_and_odd_numbers[9-even] ____________________________________________________________________________________________________________________________

test_input = 9, expected = 'even'

    @pytest.mark.parametrize("test_input,expected", [
        (3, "odd"),
        (4, "even"),
        (9, "even"),
    ])

    def test_even_and_odd_numbers(test_input, expected):
>       assert (runOddEvenCheck(test_input)) == expected
E       NameError: name 'runOddEvenCheck' is not defined

test_parametrization.py:11: NameError
================================================================================================================================ 3 failed in 0.07 seconds =================================================================================================================================
(pytest_blog) ~/D/t/p/parameterized_testing ❯❯❯           
```
This just made the process to write our tests less time consuming, not that this will always be the case as it also depends on the complexity or requirements of the project/code  we plan to write after the tests for. 
Let us get back to fixing our failing tests as per the output we have received form Pytest test runner :bowtie:
All our asserts fail as a NameError exception is raised. So let's fix that by creating a function `runOddEvenCheck` to check for number state whether odd or even when user input is provided. Then import the function for our tests to use.
``` python
# File numberWork.py
def runOddEvenCheck(nums):
    return "even" if nums % 2 == 0 else "odd"

```
Then let us import this function to our test file:
``` python
import pytest
from numberWork import runOddEvenCheck


@pytest.mark.parametrize("test_input,expected", [
    (3, "odd"),
    (4, "even"),
    (9, "even"),
])
def test_even_and_odd_numbers(test_input, expected):
    assert (runOddEvenCheck(test_input)) == expected

``` 
And we can finally run our tests with `pytest`:
``` python
(pytest_blog) ~/D/t/p/parameterized_testing ❯❯❯ pytest                                                                                                                                                                                                                       ⏎ develop ✱ ◼
=================================================================================================================================== test session starts ===================================================================================================================================
platform darwin -- Python 3.6.1, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/Upendo/Documents/tech_blogs/pytest_blog/parameterized_testing, inifile:
collected 3 items

test_parametrization.py ..F

======================================================================================================================================== FAILURES =========================================================================================================================================
____________________________________________________________________________________________________________________________ test_even_and_odd_numbers[9-even] ____________________________________________________________________________________________________________________________

test_input = 9, expected = 'even'

    @pytest.mark.parametrize("test_input,expected", [
        (3, "odd"),
        (4, "even"),
        (9, "even"),
    ])
    def test_even_and_odd_numbers(test_input, expected):
>       assert (runOddEvenCheck(test_input)) == expected
E       AssertionError: assert 'odd' == 'even'
E         - odd
E         + even

test_parametrization.py:11: AssertionError
=========================================================================================================================== 1 failed, 2 passed in 0.06 seconds ============================================================================================================================
(pytest_blog) ~/D/t/p/parameterized_testing ❯❯❯ 
```
Wow, we do have passing and failing tests now from our Pytest report. Two tests pass, with one failing test (Fact being that 9 is not an even number from the AssertionError message above).
From these example we are now able to give parametrized testing a try I hope :smile:. The topic is quite vast, this is just but a sneak peak at the good we can do with the Pythonic Pytest.
If you would like to try this example out, [here is a link to the source code on github](https://github.com/paulupendo/parametrized_testing/tree/master). `Fork`, `Clone`, `install requirements` and `pytest` :smile:. 

Happy coding!






