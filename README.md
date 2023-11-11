# Example code for the class CSC 485, "Testing for Developers"

## Basic Design

Every homework assignment will involve application code to be tested, and the test code.

The assignment's application code goes in a python package (folder + _ _ init_ _.py file) under the "projects" folder.

The assignment's test code goes in a same-named folder under the "tests" folder.


## Running Code Coverage
In order to run coverage against your project, you need to:
1. install it using ````pip install -U coverage```` from the command line
2. get the version from a ````pip freeze```` command
3. make sure you are in a new local branch!
4. add a line to requirements.txt with the coverage version
5. update your setup.cfg with the following new sections:
````yaml
[coverage:run]
# provide data on branch coverage
branch = True

# ignore the empty __init__.py files
omit = */__init__.py

# just look at the "application" code, not the test code
# this requires that you run your code from your *project* folder
source = suny485/projects

[coverage:report]
exclude_also =
    # don't complain about non-runnable code
    if __name__ == .__main__.:
````

Once code coverage is installed and configured, you can generate your coverage report by running these commands:
````commandline
# use the coverage CLI tool to run pytest
coverage run -m pytest -v --tb=short

# when the tests finish, run the report
coverage report -m

# you should get output that looks like this:

Name                                      Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------------
suny485/projects/hw10/fruit_query.py          5      0      2      0   100%
suny485/projects/hw11/homework11.py          11      0      0      0   100%
suny485/projects/hw12/homework12.py          15      0      4      0   100%
suny485/projects/hw13/homework13.py          18      0      8      0   100%
suny485/projects/hw14/api.py                  9      0      0      0   100%
suny485/projects/hw14/password_utils.py      18      0      8      0   100%
suny485/projects/hw15/api.py                 18      1      2      1    90%   101
suny485/projects/hw15/password_utils.py      18      0      8      0   100%
suny485/projects/hw16/api.py                 18     18      2      0     0%   1-117
suny485/projects/hw16/password_utils.py      18     18      8      0     0%   1-42
suny485/projects/hw16/web.py                 15     15      0      0     0%   1-42
-------------------------------------------------------------------------------------
TOTAL                                       163     52     42      1    69%

````

Documentation on coverage for Python can be found at [Coverage.py](https://coverage.readthedocs.io/en/latest/cmd.html). 


## Github Actions, Checks Made on Creating a Pull Request
Github supports workflow actions, instructions to perform various code-related steps and checks when certain things happen. For more info, see [GitHub Actions documentation](https://docs.github.com/en/actions).

We will build instructions to:
1. run our tests when we create a pull request; these tests will run against that pull request's branch, and will exclude tests that require an API server to be running (because  those will fail)
2. generate a coverage report for the tests that were run.


### Setting up our actions
To configure this, we need to have a new directory structure in the project route; this will look like this:
```text
suny485 (project root)
  |- suny48 (package)
  |- .gitignore
  |- requirements.txt
  |- setup.cfg
  |- README.md
  |- pytest.ini
  |- .github      <-- create this folder
    |- workflows  <-- create this folder
      |- push.yml <-- create this file
```

The push.yml file contains the instructions that github will use to configure and launch a docker container and the specific actions to perform on that container:
```yaml
name: Run pytest on PR

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Switch to Current Branch
      run: |
        git checkout ${{ env.BRANCH }}

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install -U pip
        pip install -r requirements.txt
        pip install -e .
        python setup.py install
        echo "[pwd]: ${PWD}"

    - name: Display Troubleshooting Information
      run: |
        echo "[workspace]: ${{ github.workspace }}"
        echo "[pwd]: ${PWD}"
        echo "[LS]: $(ls -al)"

    - name: Run tests and coverage report
      run: |
        # Note: the following commands have three entirely different instances
        # of the "-m" flag. These are positionally required!
        echo "[pwd]: ${PWD}"
        export PYTHONPATH=$PWD/suny485
        echo "[pythonpath]: ${PYTHONPATH}"
        echo "!! run pytest and exclude any live API tests !!"
        coverage run -m pytest -m 'not live_api' --tb=short
        echo "!! run coverage report"
        coverage report -m
```

### Using the actions
You will still create a pull request exactly as you have been doing. Your worklow is:
1. on your local main branch, pull from origin main to get the latest version of code from github.
2. from local main, create a feature branch. This is where you will make your changes.
3. check out your feature branch!
4. write your new code
5. commit your changes
6. push your code to a feature branch on github
7. look at your new branch on github, then click the "create pull request" button
8. Blam! now github runs your action, and you will see status indicator saying that it is in process
9. If you have no syntax errors, the actions will complete and you will get the prompt to rebase your PR. You can choose to review the logs from your actions, which will show your test results and your coverage report.


