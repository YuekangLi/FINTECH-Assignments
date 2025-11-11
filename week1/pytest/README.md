# Python Testing

In FinTecch 510, we covered testing and using `unittest` in this [Python notebook](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/22-Testing.html).  For 512, we will build upon those concepts, but utilize another testing framework, [pytest](https://docs.pytest.org/). You'll see that `pytest` tests can be a bit more natural to write as they do not have to placed into a class that descends from `unittest.TestCase`.  Flask, the primary web application we'll use in 512, uses `pytest` as its testing framework as well.

The following tutorial has been adapted from https://www.pythontutorial.net/python-unit-testing/python-unittest/.

*Summary:* In this tutorial, you’ll learn about the unit test concept and how to use the `pytest` module to perform unit testing.

## What is a Unit Test?
A unit test is an automated test that:
- Verifies a small piece of code called a unit. A unit can be a [function](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/07-Functions.html) or a method of a [class](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/24-ClassesAndObjects.html).
- Runs very fast.
- Executes in an isolated manner.

The idea of unit testing is to check each small piece of your program to ensure it works properly. It’s different from integration testing which tests that different parts of the program work well together.

The goal of a unit test is to find bugs. Also, a unit test can help refactor existing code to make it more testable and robust.

While Python provides you with a built-in module `unittest` that allows you to carry out unit testing effectively, other testing frameworks are also available.

## xUnit Terminology
The unittest module follows the xUnit philosophy. It has the following major components:
- System under test is a function, a class, a method that will be tested.
- Test cases.  In `pytest`, thse are functions that start with a `test_` prefix. We can also use classes to
  group tests.  Such classes need their name to be prefixed with "Test", but unlike `unittest` do no need to inherit from a specific class.
- Test fixtures are methods that execute before and after a test method executes.
- Assertions are methods that check the behavior of the component being tested.
- Test suite is a group of related tests executed together.
- Test runner is a program that runs the test suite.

# Example
Suppose you have `Square` class that has a property called `length` and a method `area()` that returns the area of the square. The Square class is in the square.py module:
```python
class Square:
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length * self.length
```

We'll then create a separate file(module), `test_square.py` to contain our tests of the `Square` class.
```python
from square import Square

def test_area():
    square = Square(10)
    area = square.area()
    assert area == 99
```
As compared with `unittest`, we did not need to create a specific class to hold our tests nor include our testing framework package. Additionally, `pytest` just uses Python [assert](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/21-Validation,ExceptionsAndErrorHandling.html?highlight=assert#preconditions-postconditions-invariants-and-assertions) statements.

To be able to reference `Square` class, we had to import the class from the `square.py` module.

In the `test_area()` method:
- First, create a new instance of the Square class and initialize its radius with the number 10.
- Second, call the `area()` method that returns the area of the square.
- Third, use an `assert` statment to check if the result returned by the `area()` method is equal to an expected area (100).

If the area is equal to 100, the assert will pass the test. Otherwise, the assert will fail the test.

To execute this test, you will need to navigate to the appropriate folder in a terminal window and simply
execute
```bash
$ pytest
```
This produces the following: 
```
==================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 1 item                                                                                               

test_square.py .                                                                        [100%]

===================================== 1 passed in 0.00s ======================================
```

The output indicates that one test has passed denoted by the dot (.) If a test failed, you would see the letter F instead of the dot (.) along with additional messages:

```
================================= test session starts ==================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 1 item                                                                       

test_square.py F                                                                 [100%]

======================================= FAILURES =======================================
______________________________________ test_area _______________________________________

    def test_area():
        square = Square(10)
        area = square.area()
>       assert area == 99
E       assert 100 == 99

test_square.py:6: AssertionError
=============================== short test summary info ================================
FAILED test_square.py::test_area - assert 100 == 99
================================== 1 failed in 0.01s ===================================
```

`pytest` has a large number of command-line options.  Use the `--help` flag to list these.
```
$ pytest --help
```

## Runing `pytest` Programmatically
You can invoke `pytest` from Python code directly:
```python
import pytest
pytest.main()
```
A common approach would be to define a [main](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/20-Modules.html#the-main-method) section:

```python
import pytest

from square import Square

def test_area():
    square = Square(10)
    area = square.area()
    assert area == 100
    
if __name__ == "__main__":
    pytest.main()  # include arguments within a list  
```

Then, from the command-line(terminal), execute `python test_square.py` to perform the testing.

## Discovery
`pytest` performs *test discovery* in which the framework identifies and collects test files and functions in a project, making it easy to run tests without explicitly specifying each one. pytest uses a combination of conventions and heuristics for automatic test discovery. Here's an overview of how pytest discovery works:

1. *Test File Naming Convention:* By default, `pytest` identifies test files by looking for files that match the pattern `test_*.py` or `*_test.py` in the specified directories.
2. *Test Function Naming Convention:* Test functions within these test files should be named with the prefix `test_`. For example, a test function might be named `test_my_function()`.
3. *Directory Structure:* `pytest` looks for test files in the specified directories and their subdirectories. This allows for a flexible directory structure where tests can be organized based on modules or features.
4. *Python Modules and Classes:* `pytest` can also discover and run tests defined as methods within Python classes. Test methods should be named with the prefix `test_`. Classes should be named with the prefix `Test`. Classes do not need to inherit from any specific test base class.

## Testing Expected Expectations
The `Square` constructor accepts a `length` parameter. The `length` parameter should be either an `int` or `float`. If you pass the value that is not in these types, the Square constructor should raise a `TypeError`` exception.

To test if the `Squar`e constructor raises the `TypeError` exception, you use the `pytest.raises()` method in a context manager like this:
```python
import pytest

from square import Square

def test_area():
    square = Square(10)
    area = square.area()
    assert area == 100
    
def test_length_with_wrong_type():
    with pytest.raises(TypeError):
        square = Square('10')
```
If you run the test again, it will fail:
```
$ pytest
```
Output:
```
==================================== test session starts ====================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 2 items                                                                           

test_square.py .F                                                                     [100%]

========================================= FAILURES ==========================================
________________________________ test_length_with_wrong_type ________________________________

    def test_length_with_wrong_type():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

test_square.py:11: Failed
================================== short test summary info ==================================
FAILED test_square.py::test_length_with_wrong_type - Failed: DID NOT RAISE <class 'TypeError'>
================================ 1 failed, 1 passed in 0.01s ================================
```
The `test_length_with_wrong_type()` method expected that the `Square` constructor raises a `TypeError` exception. However, it didn’t.

To pass the test, you need to raise an exception if the type of the `length` property is not `int` or `float` in the Square constructor:
```python
class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')

        self.length = length

    def area(self):
        return self.length * self.length
```
Now, all of the tests pass:
```
$ pytest
```
Output:
```
======================================= test session starts ========================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 2 items                                                                                  

test_square.py ..                                                                            [100%]

======================================== 2 passed in 0.00s =========================================
```
The following example adds a test that expects a `ValueError` exception if the `length` is zero or negative:
```python
import pytest

from square import Square

def test_area():
    square = Square(10)
    area = square.area()
    assert area == 100
    
def test_length_with_wrong_type():
    with pytest.raises(TypeError):
        square = Square('10')
        
def test_length_with_zero_or_negative():
    with pytest.raises(ValueError):
        square = Square(0)
        square = Square(-1)
```
If you run the test, it will fail:
```
$ pytest
```
Output:
```
========================================== test session starts ===========================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 3 items                                                                                        

test_square.py ..F                                                                                 [100%]

================================================ FAILURES ================================================
___________________________________ test_length_with_zero_or_negative ____________________________________

    def test_length_with_zero_or_negative():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

test_square.py:15: Failed
======================================== short test summary info =========================================
FAILED test_square.py::test_length_with_zero_or_negative - Failed: DID NOT RAISE <class 'ValueError'>
====================================== 1 failed, 2 passed in 0.01s =======================================
```
To make the test pass, you add another check to the `Square()` constructor:
```python
class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')
        if length < 0:
            raise ValueError('Length must not be negative')

        self.length = length

    def area(self):
        return self.length * self.length
```
Now, all three tests pass:
```
$ pytest
```
Output:
```
========================================== test session starts ==========================================
platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
rootdir: /home/jbs108/fintech512/fintech-512-assignments/week1/pytest
collected 3 items                                                                                       

test_square.py ...                                                                                [100%]

=========================================== 3 passed in 0.00s ===========================================
```

*Note:* This section also demonstrates [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) in 
which test cases are written before actual features are written.

## Summary
- A unit test is an automated test that verifies a small piece of code, executes fast, and executes in an isolated manner.
- In addition the the Python supplied `unittest` module, we can also use `pytest` to perform unit testing.
- Follow `pytest`'s discovery rules when naming test functions and classes.
- Use the `assert` statement to validate if a particular condition holds or not.
- Use the `pytest.raises(Exception)` method in a context manager to test expected exceptions.
- Use the `pytest` command to discover and execute tests.
