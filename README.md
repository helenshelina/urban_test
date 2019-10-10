# urban_test
test project for Urban

## Setup

Tests are written in Python and make use of `pipenv` to make dependency management easier.

### Basic requirements

  * Python 3.6+
  * A working browser and [Selenium](https://www.seleniumhq.org/) driver (for [Firefox](https://github.com/mozilla/geckodriver), [Chrome](http://chromedriver.chromium.org/) or [other browsers](https://www.seleniumhq.org/download/))

pipenv run pytest tests/foo


IDEs tested:

  * [IntelliJ IDEA](https://www.jetbrains.com/idea/) with [Python Community Edition](https://plugins.jetbrains.com/plugin/7322-python-community-edition)
  * [PyCharm](https://www.jetbrains.com/pycharm/)
  * [Visual Studio Code](https://code.visualstudio.com/) with Python extension

#### Setup instructions for IntelliJ and PyCharm

You need to setup `pipenv` as an SDK for current module:

 1. Open module settings, go so `SDKs` in `Platform Settings`
 2. Add new `Python SDK` of `Pipenv Environment` type
 3. Select the new interpreter/SDK as the default for all modules in `Project Settins` -> `Project` -> `Project SDK`

#### Setup instructions for Visual Studio Code

VSS requires only selecting auto-detected interpreter, so first run `pipenv sync` and then using `Python: Select Interpreter` from command palette select the new `pipenv` environment.

### Crash course

  * `pipenv run black` - reformat all Python code using `black`
  

### Run 
`pipenv run pytest`
or (in my case) 
`PYTHONPATH=. pipenv run pytest`
or (for having nice reports)
`PYTHONPATH=. pipenv run pytest --html=report.html -v`
or using `run` button in IDE

## Project directory structure

### `pages`

This directory holds the *non-test* portions of the code: POM classes, supporting code, etc. The organization is very simple:

### `tests`

Tests modules

### `support`
Contains useful data necessary for assertions but not directly related to pages or tests

#### `conftest.py`

`conftest.py` provides fixtures and additional configuration for tests, 

## Links

  * [Selenium Python bindings](https://seleniumhq.github.io/selenium/docs/api/py/index.html)
  * [pytest](https://docs.pytest.org/en/latest/contents.html)
  * [pytest HTML reports](https://pypi.org/project/pytest-html/)
  * [pipenv](https://pipenv.readthedocs.io/en/latest/)
  * [Python Function Annotations](https://www.python.org/dev/peps/pep-3107/) and [Function Annotations in Python](https://www.geeksforgeeks.org/function-annotations-python/) with more examples and less-reference style
  * [CSS Selector Reference](https://www.w3schools.com/cssref/css_selectors.asp)
  * [Black - Code Formatter](https://github.com/psf/black)
